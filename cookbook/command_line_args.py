import sys


print("command line arguments: %s" % repr(sys.argv))

# NOTE: there is always 1 command-line argument when the program is run
# using 'python my_program.py' or 'python3 my_program.py'. The argument
# would be 'my_program.py'.

# Usually, we don't care about the first argument (name of python file).
num_args = len(sys.argv) - 1
if num_args > 0:
    command_args = sys.argv[1:]
else:
    command_args = []

print("useful arguments: %s" % repr(command_args))

# python command_line_args.py 1 2 3
# command line arguments: ['command_line_args.py', '1', '2', '3']
# useful arguments: ['1', '2', '3']
