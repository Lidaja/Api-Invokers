import sys
sys.path.append('/usr/lib/python2.7')
from denali.cluster import Cluster


def createZFSPool(pool_name, nodeIPs):
	cluster = Cluster('denaliCluster')
        nodes = []
        for n in nodeIPs.split(","):
                if "-" not in n:
                        nodes.append(n)
                else:
                        m = n.split("-")
                        first = ".".join(m[0].split(".")[:-1])
                        start = m[0].split(".")[-1]
                        end = m[1].split(".")[-1]
                        for i in range(int(start),int(end)+1):
                                nodes.append(first+"."+str(i))
	try:
		cluster.restore()
		zfs_pool_name = pool_name
		zfs_pool_g = cluster.create_group(zfs_pool_name, nodes)
		zfs_pool_r = zfs_pool_g.create_pool(zfs_pool_name)
		zfs_pool_r.layout = '/dev/sa'
		zfs_pool_r.provision()

	except ValueError as e:
		print "We should never reach this point"


if __name__=='__main__':
	createZFSPool(sys.argv[1],sys.argv[2])



