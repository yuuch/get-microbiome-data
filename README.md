# get-microbiome-data
here are some script for downloading and parsing data downloaded from EBI-EMBL.
1. Gernerate sample sequences urls from  EBI.(demultiplexed.i.e. without barcodes.) and use wget -i file to download sequences.    
2. Download sample metadata from EBI(.xml format)  
3. Parse these .xml files and generate a .csv format file.  
4. Generate the mainfest file to import these  samples into .qza format file for QIIME. [Fastq manifest” formats](https://docs.qiime2.org/2019.1/tutorials/importing/)
