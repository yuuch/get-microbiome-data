import requests
from tqdm import tqdm
from bs4 import BeautifulSoup as Soup
import pandas as pd
import os
class EBIDownloader(object):
    def __init__(self,ERR_num, ERS_num,n_sample):
        self.ERR_num = ERR_num
        self.ERS_num = ERS_num
        self.n_sample = n_sample
    def download_metadata(self):
        """download metadatas of every sample in .xml format.
        """
        init_n = self.ERS_num
        for i in range(self.n_sample):
            sample_id = init_n +i
            url = "https://www.ebi.ac.uk/ena/data/view/ERS" + str(sample_id)\
                 +"&display=xml&download=xml&filename=ERS"\
                      + str(sample_id)+".xml"
            response = requests.get(url, stream=True)
            saved_filename = 'ERS' + str(sample_id)
            with open(saved_filename, "wb") as handle:
                for data in tqdm(response.iter_content()):
                    handle.write(data)
    def parse_XML2Series(self, file_name):
        """ parse the .xml to pandas.Series object
        """
        handler = open(file_name).read()
        soup = Soup(handler)
        sample_dict = {}
        for ele in soup.findAll('sample_attribute'):
            key = ele.tag.decode_contents()
            value = ele.value.decode_contents()
            sample_dict[key] = value
        for ele in soup.findAll('primary_id'):
            key = '#SampleID'
            value = ele.decode_contents()
            bias = self.ERR_num -self.ERS_num
            new_value = 'ERR'+str(int(value[3:])+bias)
            sample_dict[key] = new_value
        series = pd.Series(sample_dict)
        return series

    def obtain_metadata_file(self, tsv_file_name):
        """ merge all samples' metadata into table(.tsv format)
        """
        series_array = []
        for i in range(self.n_sample):
            sample_id = self.ERS_num + i
            filename = 'ERS'+str(sample_id)
            series = self.parse_XML2Series(filename)
            series_array.append(series)
        df = pd.DataFrame(series_array)
        df.to_csv(tsv_file_name,sep='\t')

    def generate_seq_urls(self,seq_file_path,paired=True):
        """ generate sequences urls.After ,we can use 'wget -i seq_file_path'
        to download seqs from ENA.
        Args:
            seq_file_path: a path to file who save the urls.
            paired: for paired seqs its True otherwise False.
        """
        f = open(seq_file_path,'w')
        for i in range(self.n_sample):
            id_number = self.ERR_num + i 
            last_number = str(id_number % 10)
            pre_fix ='ERR'+str(self.ERR_num)[:3]
            if paired:
                url_1 = 'ftp://ftp.sra.ebi.ac.uk/vol1/fastq/'+pre_fix+'/00' \
                    +last_number+'/ERR'+str(id_number)\
                    +'/ERR'+str(id_number)+'_1.fastq.gz\n'
                url_2 = 'ftp://ftp.sra.ebi.ac.uk/vol1/fastq/'+pre_fix+'/00' \
                    +last_number+'/ERR'+str(id_number)\
                    +'/ERR'+str(id_number)+'_2.fastq.gz\n'
                f.write(url_1)
                f.write(url_2)
            else:
                url = 'ftp://ftp.sra.ebi.ac.uk/vol1/fastq/'+pre_fix+'/00' \
                    +last_number+'/ERR'+str(id_number)\
                    +'/ERR'+str(id_number)+'.fastq.gz\n'
                f.write(url)
        f.close()
            


if __name__ == "__main__":
    ebid = EBIDownloader(ERR_num=1750995, ERS_num=1469890, n_sample=18)
    #ebid.download_metadata()
    #ebid.obtain_metadata_file('284_metadata.tsv')
    ebid.generate_seq_urls('seq_file_list.txt',paired=True)
        
    




        
