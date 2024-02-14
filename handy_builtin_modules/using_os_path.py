import os.path

# online docs: https://docs.python.org/3/library/os.path.html 

file_path = "/etc/resolv.conf"

# is file path a file?
if os.path.isfile(file_path):
    print("%s is a file" % file_path)

# is file path a directory?
if os.path.isdir(file_path):
    print("%s is a directory" % file_path)

# does file path exist?
if os.path.exists(file_path):
    print("%s exists" % file_path)

# retrieve file size
file_size_bytes = os.path.getsize(file_path)
print("file size = %d bytes" % file_size_bytes)

# retrieve file last modified time
file_mtime = os.path.getmtime(file_path)
print("file modify time: %f" % file_mtime)

# join directory and file
full_path = os.path.join("/etc", "resolv.conf")  # returns "/etc/resolv.conf"


