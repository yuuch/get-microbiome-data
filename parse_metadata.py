from bs4 import BeautifulSoup as Soup
import pandas as pd
def parse_XML2Series(file_name):
    #file = sys.argv[1]
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
        # 2172355-1972942
        new_value = 'ERR'+str(int(value[3:])+199413)
        #print('primary_id',value)
        sample_dict[key] = new_value
        #break
    series = pd.Series(sample_dict)
    return series
if __name__ == "__main__":
    init_n = 1972942
    n_sample = 945
    series_array = []
    for i in range(n_sample):
        sample_id = init_n +i
        filename = 'ERS'+str(sample_id)
        series = parse_XML2Series(filename)
        series_array.append(series)
    df = pd.DataFrame(series_array)
    df.to_csv('945metadata.csv',sep='\t')
