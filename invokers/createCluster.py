import sys
sys.path.append('/usr/lib/python2.7')
from denali.cluster import Cluster
from denali.pool import Pool
from denali.target import Target
import denali.volume



cluster = Cluster('denaliCluster')
cluster.add_node('10.10.30.236')
cluster.vip = '10.10.30.235'
cluster.nic = 'eth0'
cluster.netmask = '24'
cluster.initialize()
