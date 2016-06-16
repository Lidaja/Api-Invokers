import sys
sys.path.append('/usr/lib/python2.7')
from denali.cluster import Cluster
from denali.pool import Pool
from denali.target import Target
import denali.volume

def createTargetPortalGroup(portal_name, portal_ip):
	cluster = Cluster()
	tpg_name = portal_name
	tpg_r = cluster.create_group(tpg_name, [portal_ip]).create_tpg(target_svc_g,tpg_name)
	tpg_r.iqn = 'iqn.2016-04.com.istuary.denali-poc.001'	
	tpg_r.acls = ['iqn.2016-04.com.istuary.denali-poc.client.001', 'iqn.2016-04.com.istuary.denali-poc.client.002']
	tpg_r.portals = [porta_ip]
	tpg_r.provision()

if __name__=='__main__':
	createTargetPortalGroup()
