import sys
sys.path.append('/usr/lib/python2.7')
from denali.cluster import Cluster


def createCluster(node_ip,vip):
	cluster = Cluster('denaliCluster')
	try:
		cluster.restore()
	except ValueError as e:
		cluster.add_node(node_ip)
		cluster.vip = vip
		cluster.nic = 'eth0'
		cluster.netmask = '24'
		cluster.initialize()
	return cluster

if __name__=='__main__':
	createCluster(sys.argv[1],sys.argv[2])
