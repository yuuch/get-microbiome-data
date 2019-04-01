init_n = 2172355#1746339
n_sample = 945#683
#ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR217/005/ERR2172355/ERR2172355.fastq.gz
f = open('download_seqs_list_2.txt','w')
for i in range(n_sample):
    id_number = init_n + i 
    last_number = str(id_number % 10)
    url = 'ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR217/00'+last_number+'/ERR'+str(id_number)\
    +'/ERR'+str(id_number)+'.fastq.gz\n'
    f.write(url)
f.close()
