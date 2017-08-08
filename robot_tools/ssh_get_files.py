import paramiko
import os


def get(host, usr, password, path, pattern):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host,username=usr, password=password)

    apath = path
    apattern = pattern
    rawcommand = 'find {path} -name {pattern}'
    command = rawcommand.format(path=apath, pattern=apattern)
    stdin, stdout, stderr = ssh.exec_command(command)
    filelist = stdout.read().splitlines()

    names_list = []
    ftp = ssh.open_sftp()
    for afile in filelist:
        (head, filename) = os.path.split(afile)
        names_list.append(filename[:-4])

    ftp.close()
    ssh.close()
    return names_list
