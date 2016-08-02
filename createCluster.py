import sys
sys.path.append('/usr/lib/python2.7')
#from denali.cluster import Cluster


def createCluster(node_ip,vip,numNodes):
	nodes = []
	last = node_ip.split(".")[-1]
	first = ".".join(node_ip.split(".")[:-1])+"."
	for i in range(0,int(numNodes)):
		nodes.append(first+str(int(last)+i))
	cluster = Cluster('denaliCluster')
	try:
		cluster.restore()
	except ValueError as e:
		cluster.nodes = nodes
		cluster.vip = vip
		cluster.nic = 'eth0'
		cluster.netmask = '24'
		cluster.initialize()
	return cluster

if __name__=='__main__':
	createCluster(sys.argv[1],sys.argv[2],sys.argv[3])
