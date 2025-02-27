from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline
from cnnClassifier.pipeline.stage_03_training import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_04_evaluation import EvaluationPipeline


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> stage: {STAGE_NAME} started <<<<<<")

    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()

    logger.info(f">>>>>> stage: {STAGE_NAME} completed <<<<<< \n\n X===================X")

except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Prepare Base Model Stage"

try:
    logger.info(f">>>>>> stage: {STAGE_NAME} started <<<<<<")

    prepare_base_model = PrepareBaseModelPipeline()
    prepare_base_model.main()

    logger.info(f">>>>>> stage: {STAGE_NAME} completed <<<<<< \n\n X===================X")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Training"

try:
    logger.info(f">>>>>> stage: {STAGE_NAME} started <<<<<<")

    model_trainer = ModelTrainingPipeline()
    model_trainer.main()

    logger.info(f">>>>>> stage: {STAGE_NAME} completed <<<<<<")

except Exception as e:
    logger.exception(e)


STAGE_NAME = "Evaluation"

try:
    logger.info(f">>>>>> stage: {STAGE_NAME} started <<<<<<")

    evaluation = EvaluationPipeline()
    evaluation.main()

    logger.info(f">>>>>> stage: {STAGE_NAME} completed <<<<<<")

except Exception as e:
    logger.exception(e)