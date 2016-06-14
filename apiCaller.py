import sys
sys.path.append('/usr/lib/python2.7/')
from denali.group import Group
#from denali.pool import Pool
if __name__ == '__main__':
	print "Hello"
	g = Group("GroupName")
	p = g.create_pool("PoolName")
	#r = g.create_volume(p,"VolumeName")
