import sys
sys.path.append('/usr/lib/python2.7')
from denali.cluster import Cluster
from denali.pool import Pool
from denali.target import Target
import denali.volume
from createCluster import createCluster
import pickle

def createZFSPool():
	cluster = createCluster()
	zfs_pool_name = 'denali-pool-proto'
	zfs_pool_g = cluster.create_group(zfs_pool_name, ['cluster'])
	zfs_pool_r = zfs_pool_g.create_pool(zfs_pool_name)
	zfs_pool_r.layout = '/dev/sa'
	pickle.dump(zfs_pool_g,open("pool.p","wb"))
	zfs_pool_r.provision()
	return zfs_pool_r
if __name__=='__main__':
	createZFSPool();



