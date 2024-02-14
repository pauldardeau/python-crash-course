
# write some stuff to a file
file_path = "test.txt"
file_contents = "This is line 1\nThis is line 2\nThis is line 3\n"
with open(file_path, 'w') as f:
    f.write(file_contents)

