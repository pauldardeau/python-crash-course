import paramiko


# to install: pip3 install paramiko

ssh = paramiko.SSHClient()

if ssh is not None:
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    remote_host = "pavilion"
    user = "paul"

    try:
        ssh.connect(remote_host, username=user)
        stdin, stdout, stderr = ssh.exec_command('ls')
        print(stdout.read().decode())
    except:
        print("error: unable to connect to hose %s" % remote_host)
    finally:
        ssh.close()
