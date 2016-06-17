import sys
sys.path.append('/usr/lib/python2.7')
from denali.cluster import Cluster
from denali.pool import Pool
from denali.target import Target
import denali.volume

def createTargetPortalGroup(portal_name, portal_ip, target_svc_name, iqn, acls):
	cluster = Cluster('denaliCluster')
	try:
		cluster.restore()
		target_svc_g = cluster.group[target_svc_name]
		tpg_name = portal_name
		tpg_r = cluster.create_group(tpg_name, [portal_ip]).create_tpg(target_svc_g,tpg_name)
		tpg_r.iqn = iqn	
		tpg_r.acls = acls
		tpg_r.portals = [portal_ip]
		tpg_r.provision()
	except ValueError as e:
		print "This point literally cannot be reached, seriously what are you doing here?"
	
if __name__=='__main__':
	createTargetPortalGroup()
