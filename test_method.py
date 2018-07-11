class Test(object):
	"""docstring for ClassName"""
	def testaaa(self):
		return "aaa"


def testbbb():
	return 'bbb'

a = Test()

a.testaaa = testbbb

print a.testaaa()

b = Test()
print b.testaaa()
print "this is test"
