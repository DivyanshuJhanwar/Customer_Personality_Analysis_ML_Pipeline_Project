from customer_personality.exception.exception_handler import AppException
from customer_personality.components.data_ingestion import DataIngestion
from customer_personality.logger import log


obj = DataIngestion()
obj.initiate_data_ingestion()
print("Data Ingestion Completed!")