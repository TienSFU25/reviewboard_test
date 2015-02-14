import pkg_resources
import os

def visit(arg, dirname, names):
	print arg
	print dirname
	print names
	arg.append(5)

li = [1, 2, 3]
os.path.walk(pkg_resources.resource_filename("rbtools", "templates"), visit, li)

print li