
def write_text_file(file_path, file_contents):
    with open(file_path, 'w') as f:
        f.write(file_contents)


# first write some stuff to a file
file_path = "test.txt"
file_contents = "This is line 1\nThis is line 2\nThis is line 3\n"
write_text_file(file_path, file_contents)

# now read it
with open(file_path, 'r') as f:
    read_file_contents = f.read()

if file_contents == read_file_contents:
    print("contents written to file matches what was read")
else:
    print("mismatch of what was written and what was read")

