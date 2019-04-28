import os
from multiprocessing import Pool
def download_single(seq_url):
    os.system('wget '+seq_url)
def download_seqs(seq_urls, dest_dir='.'):
    f = open(seq_urls,'r')
    try:
        os.system('cd '+dest_dir)
    except:
        os.system('mkdir '+dest_dir)
        os.system('cd '+dest_dir)
    lines = f.readlines()
    with Pool() as p:
        p.map(download_single,lines)
if __name__ == "__main__":
    download_seqs('seq_file_list.txt','.')
