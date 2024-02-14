import sys


# see online docs: https://docs.python.org/3/library/sys.html

# command line arguments
num_args = len(sys.argv) - 1
print("%d command line arguments were passed" % num_args)


# exiting program with a return code
# uncomment following line to exit program with exit code 1
#sys.exit(1)


# platform identifier
if sys.platform.startswith('freebsd'):
    # FreeBSD-specific code here...
    print("running on FreeBSD")
elif sys.platform.startswith('linux'):
    # Linux-specific code here...
    print("running on linux")
elif sys.platform.startswith('aix'):
    # AIX-specific code here...
    print("running on aix")
else:
    print("running on something else")



