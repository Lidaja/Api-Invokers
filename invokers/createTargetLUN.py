import sys
sys.path.append('/usr/lib/python2.7')
from denali.cluster import Cluster
from denali.pool import Pool
from denali.target import Target
import denali.volume

def createTargetLUN(lun_name, lun_ip):
	lun_r = cluster.create_group(lun_name, [lun_ip]).create_lun(cluster.groups[tpg_name], lun_name)
	lun_r.portal = tpg_name
	lun_r.volume = target_vol_r
	lun_r.provision()

if __name__=='__main__':
	createTargetLUN(sys.argv[1],sys.argv[2])

