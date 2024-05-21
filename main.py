from src.indi import logger
from src.indi.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from indi.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from indi.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from indi.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline

STAGE_NAME='Data Ingestion stage'

try:
   #Comienzo de la ingesta
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   #Llamar a la clase importada
   data_ingestion = DataIngestionTrainingPipeline()
   #El main esta dentro de la clase, la clase carga y descarga cosas
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Data Validation stage"

try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataValidationTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Data Transformation stage"

try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataTransformationTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Model Trainer stage"

try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = ModelTrainerTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e