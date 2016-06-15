import sys
sys.path.append('/usr/lib/python2.7')
from denali.cluster import Cluster
from denali.pool import Pool
from denali.target import Target
import denali.volume

def createTargetService():
	target_svc_name = 'iscsi'
	cluster.create_group(target_svc_name).create_target(target_svc_name).provision
