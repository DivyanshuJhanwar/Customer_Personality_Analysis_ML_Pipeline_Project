from collections import namedtuple

# namedtuple works as a Dictionary

DataIngestionConfig = namedtuple("DataIngestionConfig", ["dataset_download_url",
                                                   "raw_data_dir",
                                                   "ingested_dir"])

  
 