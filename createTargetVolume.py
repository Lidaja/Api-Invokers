import sys
sys.path.append('/usr/lib/python2.7')
from denali.cluster import Cluster
from denali.pool import Pool
from denali.target import Target
import denali.volume

def createTargetVolume(volume_name,volume_ip,size,tag, pool_name):
	cluster = Cluster('denaliCluster')
	try:
		cluster.restore()
		zfs_pool_g = cluster.groups[pool_name]
		target_vol_name = volume_name
		target_vol_g = cluster.create_group(target_vol_name, [volume_ip])
		target_vol_r = target_vol_g.create_target_volume(zfs_pool_g, target_vol_name, size)
		target_vol_r.tag = tag
		target_vol_r.provision()
	except ValueError as e:
		print "We should never reach this point"
	
if __name__=='__main__':
	createTargetVolume(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])
