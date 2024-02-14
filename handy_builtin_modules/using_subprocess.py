import subprocess


# the following function is very useful to use as is.
def run_command(command):
    p = subprocess.run(command,
                       shell=True,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
    exit_code = p.returncode
    stdout = p.stdout.decode("utf-8") 
    stderr = p.stderr.decode("utf-8")
    return exit_code, stdout, stderr


exit_code, stdout, stderr = run_command("uname")
if exit_code == 0:
    print("%s" % stdout)
else:
    print("%s" % stderr)

