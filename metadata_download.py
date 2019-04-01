import requests
from tqdm import tqdm
"""
url = "http://download.thinkbroadband.com/10MB.zip"
file_name = url.split('/')[-1]
r = requests.get(url)
with open('test_data.zip','wb') as f:
    f.write(r.content)
"""
init_n = 1972942
n_sample = 945
for i in range(n_sample):
    sample_id = init_n +i
    url = "https://www.ebi.ac.uk/ena/data/view/ERS"+str(sample_id)+"&display=xml\
    &download=xml&filename=ERS"+str(sample_id)+".xml"
    response = requests.get(url, stream=True)
    saved_filename = 'ERS'+str(sample_id)
    with open(saved_filename, "wb") as handle:
        for data in tqdm(response.iter_content()):
            handle.write(data)
