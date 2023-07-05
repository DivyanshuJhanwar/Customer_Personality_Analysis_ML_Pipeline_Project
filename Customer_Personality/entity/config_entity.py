from collections import namedtuple

# namedtuple works as a Dictionary

DataIngestionConfig = namedtuple("DataIngestionConfig", ["dataset_download_url",
                                                   "raw_data_dir",
                                                   "ingested_dir"])

DataValidationConfig = namedtuple("DataValidationConfig", ["clean_data_dir",
                                                         "marketing_campaign_csv_file",
                                                         "serialized_objects_dir"])  