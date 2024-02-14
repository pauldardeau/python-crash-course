
def write_binary_file(file_path, file_contents):
    with open(file_path, 'wb') as f:
        f.write(file_contents)


def read_binary_file(file_path):
    with open(file_path, 'rb') as f:
        return f.read()


# first, create a binary file so we have something to read
file_path = 'example_file.bin'
file_contents = b'\x00\x01\x02\x03\x04\x05'

write_binary_file(file_path, file_contents)

read_file_contents = read_binary_file(file_path)

if read_file_contents == file_contents:
    print("file_contents matches read_file_contents")
else:
    print("mismatch of file_contents and read_file_contents")

