import sys
sys.path.append('/usr/lib/python2.7')
from denali.cluster import Cluster


def createCluster(nodeIPs,vip):
	nodes = []
	for n in nodeIPs.split(","):
        	if "-" not in n:
			if n not in nodes:
                		nodes.append(n)
	        else:
        	        m = n.split("-")
                	first = ".".join(m[0].split(".")[:-1])
                	start = m[0].split(".")[-1]
                	end = m[1]
			s = int(start)-int(end)
			s = s/abs(s) 
			print s
                	for i in range(int(start),int(end)-s,-s):
                        	if first+"."+str(i) not in nodes:
					nodes.append(first+"."+str(i))
	#print nodes
	
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
	createCluster(sys.argv[1],sys.argv[2])
