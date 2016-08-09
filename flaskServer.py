from flask import Flask
from flask import request
app = Flask(__name__)

def getNodes(nodeIPs):
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
@app.route("/cluster/<params>", methods=['POST'])
def createCluster(params):
	params = params.split("^")
	nodeIPs = params[0]
	vip = params[1]
        nodes = getNodes(nodeIPs)
	print nodes
        cluster = Cluster('denaliCluster')
        try:
                cluster.restore()
        except ValueError as e:
                cluster.nodes = nodes
                cluster.vip = vip
                cluster.nic = 'eth0'
                cluster.netmask = '24'
                cluster.initialize()

@app.route("/zfs/<params>",methods=['POST'])
def createZFSPool(params):
	params = params.split("^")
	zfs_pool_name = params[0]
	nodeIPs = params[1]
        nodes = getNodes(nodeIPs)
        zfs_pool_g = cluster.create_group(zfs_pool_name, nodes)
        zfs_pool_r = zfs_pool_g.create_pool(zfs_pool_name)
        zfs_pool_r.layout = '/dev/sa'
        zfs_pool_r.provision()


@app.route("/service/<target_svc_name>",methods=['POST'])
def createTargetService(target_svc_name): 
        cluster.create_group(target_svc_name).create_target(target_svc_name).provision
        target_svc_g = cluster.groups[target_svc_name]

@app.route("/volume/<params>",methods=['POST'])
def createTargetVolume(params):
	params = params.split('&')
	target_vol_name=params[0]
	volume_ip=params[1]
	size=params[2]
	tag=params[3]
	pool_name=params[4]
        zfs_pool_g = self.cluster.groups[pool_name]
        target_vol_g = self.cluster.create_group(target_vol_name, [volume_ip])
        target_vol_r = target_vol_g.create_target_volume(zfs_pool_g, target_vol_name, size)
        target_vol_r.tag = tag
        target_vol_r.provision()

@app.route("/portal/<params>",methods=['POST'])
def createPortalGroup(params):
	params = params.split("^")
	tpg_name=params[0]
	portal_ip=params[1]
	target_svc_name=params[2]
	iqn=params[3]
	acls=params[4]
        target_svc_g = self.cluster.group[target_svc_name]
        tpg_r = self.cluster.create_group(tpg_name, [portal_ip]).create_tpg(target_svc_g,tpg_name)
        tpg_r.iqn = iqn
        tpg_r.acls = acls
        tpg_r.portals = [portal_ip]
        tpg_r.provision()

@app.route("/lun/<params>",methods=['POST'])
def createTargetLUN(self,lun_name, lun_ip, tpg_name, volume_name):
	params=params.split("^")
	lun_name=params[0]
	lun_ip=params[1]
	tpg_name=params[2]
	volume_name=params[3]
        target_vol_r = self.cluster.groups[volume_name]
        lun_r = self.cluster.create_group(lun_name, [lun_ip]).create_lun(cluster.groups[tpg_name], lun_name)
        lun_r.portal = tpg_name
        lun_r.volume = target_vol_r
        lun_r.provision()

if __name__ == "__main__":
	app.run()
