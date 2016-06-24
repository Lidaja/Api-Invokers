import sys
sys.path.append('/usr/lib/python2.7')
from denali.cluster import Cluster
from denali.pool import Pool
from denali.target import Target
import denali.volume

def createTargetService(service_name):
	cluster = Cluster('denaliCluster')
	try:
		cluster.restore()
		target_svc_name = service_name
		cluster.create_group(target_svc_name).create_target(target_svc_name).provision
		target_svc_g = cluster.groups[target_svc_name]
	except ValueError as e:
		print "This point should never be reached"

if __name__=='__main__':
	createTargetService(sys.argv[1])
