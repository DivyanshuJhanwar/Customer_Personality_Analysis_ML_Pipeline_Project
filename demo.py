from customer_personality.exception import AppException
from customer_personality.components.data_ingestion import DataIngestion


obj = DataIngestion()
obj.initiate_data_ingestion()
print("Data Ingestion Completed!")