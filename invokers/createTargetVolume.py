import sys
sys.path.append('/usr/lib/python2.7')
from denali.cluster import Cluster
from denali.pool import Pool
from denali.target import Target
import denali.volume

def createTargetVolume():
	target_vol_name = 'target_vol'
	target_vol_g = cluster.create_group(target_vol_name, ['10.10.30.173'])
	target_vol_r = target_vol_g.create_target_volume(zfs_pool_g, target_vol_name, '1G')
	target_vol_r.tag = 'iscsi:target_vol'
	target_vol_r.provision()
