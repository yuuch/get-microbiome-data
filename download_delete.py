import time

import os

import numpy as np

f = open('seq_file_list.txt')
lines = f.readlines()
n = len(lines)
g = open('download.log','a')
while True:
    i = np.random.randint(0,100)
    time.sleep(i)
    
    try:
        os.system('wget bing.com\n')
        g.write('bing.com\n')
    except:
        pass
    
    line_nums = []
    for j in range(100):
        line = lines[np.random.randint(0,n)]
        try:
            os.system('wget ' + line)
            g.write(line+'\n')
            time.sleep(j*0.01)
        except:
            pass
    try:
        os.system('rm index.html*')
    except:
        pass
    
    try:
        os.system('rm *fastq*')
    except:
        pass
    try:
        os.system('rm *nohup.out*')
    except:
        pass
