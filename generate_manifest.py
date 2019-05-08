def generate_mainfest(init_n,sample_n,folder_name,handle):
    for i in range(sample_n):
        id_n = init_n + i
        line = 'ERR'+str(id_n)+',$PWD/' + folder_name + '/ERR'+str(id_n)+'.fastq.gz,forward\n'
        handle.write(line)
if __name__ == "__main__":
    handle = open('se_mainfest_new','a')
    handle.write('# single-end PHRED 33 fastq manifest file for forward reads\n')
    handle.write('sample-id,absolute-filepath,direction\n')
    generate_mainfest(1746339,683,'qiita_id_1629',handle)
    generate_mainfest(1368879,1359,'qiita_id_1939',handle)
    handle.close()
