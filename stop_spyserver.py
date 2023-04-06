# Python script to stop a running spyserver process
import psutil
import sys

cmdline_str = r'./spyserver'
procname_str = 'spyserver'

pid_list = psutil.pids()

for pid in pid_list:
    p = psutil.Process(pid)
    cmd = p.cmdline()
    pname = p.name()
    if cmdline_str in cmd:
        print('Stopping PID {}'.format(pid))
        p.terminate()
        p.wait()
