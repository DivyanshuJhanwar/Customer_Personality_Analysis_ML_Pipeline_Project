import os

ROOT_DIR = os.getcwd()
# Main config file path
CONFIG_FOLDER_NAME = "config"
CONFIG_FILE_NAME = "config.yaml"
CONFIG_FILE_PATH = os.path.join(ROOT_DIR,CONFIG_FOLDER_NAME,CONFIG_FILE_NAME)


# We are using the same code for Data_Ingestion, Data_Validation and etc. because we have not called Schema.yaml file.