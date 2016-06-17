import sys
sys.path.append('/usr/lib/python2.7')
from denali.cluster import Cluster


def createZFSPool(pool_name, node_list):
	cluster = Cluster('denaliCluster')

	try:
		cluster.restore()
		zfs_pool_name = pool_name
		zfs_pool_g = cluster.create_group(zfs_pool_name, node_list)
		zfs_pool_r = zfs_pool_g.create_pool(zfs_pool_name)
		zfs_pool_r.layout = '/dev/sa'
		zfs_pool_r.provision()

	except ValueError as e:
		print "We should never reach this point"


if __name__=='__main__':
	createZFSPool(sys.argv[1],sys.argv[2])



