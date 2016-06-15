if __name__=='__main__':
	print "This data should not be grabbed"
	print "@*@"
	print "This data should be grabbed"
	print "@*@"
	print "This data should also not be grabbed"
	print "@*@"
	print "This data should be grabbed"
	print "So should this data"
	print "@*@"
	print "But this data should not"
	f = open("test.txt","w")
	f.write("Test")
