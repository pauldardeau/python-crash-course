import os

# online docs: https://docs.python.org/3/library/os.html

# retrieve our pid
our_pid = os.getpid()
print("pid of our process: %d" % our_pid)

# retrieve our real uid
our_uid = os.getuid()
print("real uid for our process: %d" % our_uid)

# stat a file
stat_info = os.stat("using_os.py")
print("%s" % repr(stat_info))

# delete a file
#os.remove("some_file.txt")

# same as above
#os.unlink("some_file.txt")

# create a directory
#os.mkdir("my_subdir")


