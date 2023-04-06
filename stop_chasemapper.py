# Python script to stop a running chasemapper process
import psutil
import sys

pid_list = psutil.pids()

for pid in pid_list:
    p = psutil.Process(pid)
    cmd = p.cmdline()
    pname = p.name()
    if (len(cmd) > 1):
        if (cmd[0] == 'python'):
            if (cmd[1] == './horusmapper.py'):
                print('Stopping PID {}'.format(pid))
                p.terminate()
                p.wait()
