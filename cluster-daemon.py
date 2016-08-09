#!/usr/bin/env python

import sys, time, select, os
from daemon import Daemon
sys.path.append('/usr/lib/python2.7')
from denali.cluster import Cluster
from denali.pool import Pool
from denali.target import Target
import denali.volume


class ClusterDaemon(Daemon):
	def __init__(self,pidfile, stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
		Daemon.__init__(self,pidfile,stdin,stdout,stderr)
		self.cluster = None
		self.files2funcs = {'cluster':self.createCluster,'zfs':self.createZFSPool,'service':self.createTargetService,'volume':self.createTargetVolume,'portal':self.createPortalGroup,'lun':self.createTargetLUN}
		
	def run(self):
		while True:
			time.sleep(1)
			for n in self.files2funcs.keys():
				name = '/tmp/'+n+'.txt'
				if (os.path.isfile(name)):
					f = open(name)
					params = f.readline().split(" ")
					self.files2funcs[n](*params)
					os.remove(name)
					
	
	def getNodes(self,nodeIPs):
		nodes = []
		for n in nodeIPs.split(","):
			if "-" not in n:
				if n not in nodes:
					nodes.append(n)
			else:
				m = n.split("-")
				first = ".".join(m[0].split(".")[:-1])
				start = m[0].split(".")[-1]
				end = m[1]
				s = int(start)-int(end)
				s = s/abs(s)
				for i in range(int(start),int(end)-s,-s):
					if first+"."+str(i) not in nodes:
						nodes.append(first+"."+str(i))
		return nodes

	def createCluster(self,nodeIPs, vip):
		nodes = self.getNodes(nodeIPs)
		self.cluster = Cluster('denaliCluster')
		try:
			self.cluster.restore()
		except ValueError as e:
			self.cluster.nodes = nodes
			self.cluster.vip = vip
			self.cluster.nic = 'eth0'
			self.cluster.netmask = '24'
			self.cluster.initialize()
		
	def createZFSPool(self,zfs_pool_name, nodeIPs):
		nodes = self.getNodes(nodeIPs)
		zfs_pool_g = self.cluster.create_group(zfs_pool_name, nodes)
		zfs_pool_r = zfs_pool_g.create_pool(zfs_pool_name)
		zfs_pool_r.layout = '/dev/sa'
		zfs_pool_r.provision()

	def createTargetService(self,target_svc_name):
		self.cluster.create_group(target_svc_name).create_target(target_svc_name).provision
		target_svc_g = self.cluster.groups[target_svc_name]
		
	def createTargetVolume(self,target_vol_name, volume_ip,size,tag,pool_name):
		zfs_pool_g = self.cluster.groups[pool_name]
		target_vol_g = self.cluster.create_group(target_vol_name, [volume_ip])
		target_vol_r = target_vol_g.create_target_volume(zfs_pool_g, target_vol_name, size)
		target_vol_r.tag = tag
		target_vol_r.provision()

	def createPortalGroup(self,tpg_name, portal_ip, target_svc_name, iqn, acls):
		target_svc_g = self.cluster.group[target_svc_name]
		tpg_r = self.cluster.create_group(tpg_name, [portal_ip]).create_tpg(target_svc_g,tpg_name)
		tpg_r.iqn = iqn
		tpg_r.acls = acls
		tpg_r.portals = [portal_ip]
		tpg_r.provision()

	def createTargetLUN(self,lun_name, lun_ip, tpg_name, volume_name):
		target_vol_r = self.cluster.groups[volume_name]
		lun_r = self.cluster.create_group(lun_name, [lun_ip]).create_lun(cluster.groups[tpg_name], lun_name)
		lun_r.portal = tpg_name
		lun_r.volume = target_vol_r
		lun_r.provision()


if __name__ == "__main__":
	daemon = ClusterDaemon('/tmp/daemon-example.pid','/dev/stdin','/dev/stdout')
	if len(sys.argv) == 2:
		if 'start' == sys.argv[1]:
			daemon.start()
		elif 'stop' == sys.argv[1]:
			daemon.stop()
		elif 'restart' == sys.argv[1]:
			daemon.restart()
		else:
			print "Unknown command"
			sys.exit(2)
		sys.exit(0)
	else:
		print "usage: %s start|stop|restart" % sys.argv[0]
		sys.exit(2)
