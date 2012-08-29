#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'dotpot'
import subprocess, signal, os, sys
if __name__ == "__main__":
    if len(sys.argv) > 1:
        if len(sys.argv[1]) > 0:
            print 'processes containing "{0}" will be killed .)'.format(sys.argv[1])
            p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
            out, err = p.communicate()
            for line in out.splitlines():
                if str(sys.argv[1]) in line:
                    pid = int(line.split(None, 1)[0])
                    print 'pid killed: {0}, line: {1}'.format(pid, line)
                    os.kill(pid, signal.SIGKILL)
    else: print 'You must provide process name'