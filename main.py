from src.textSummarization.components.data_ingestion import DataIngestion
from src.textSummarization.components.data_transformation import \
    DataTransformation
from src.textSummarization.components.data_validation import DataValidation
from src.textSummarization.config.configuration import ConfrigurationManager

config = ConfrigurationManager()
data_ingestion_config = config.get_data_ingestion_config()
data_ingestion = DataIngestion(config=data_ingestion_config)
data_ingestion.download_file()
data_ingestion.extract_zip_file()
config=ConfrigurationManager()
# print('--')
data_validation_config=config.get_data_validation_config()
# print("--")
data_validation=DataValidation(config=data_validation_config)
data_validation.validate_all_files_exit()


config = ConfrigurationManager()
data_transformation_config = config.get_data_transformation_config()
data_transformation = DataTransformation(config=data_transformation_config)
data_transformation.convert()