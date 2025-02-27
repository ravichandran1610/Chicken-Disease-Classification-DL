from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.training import Training
from cnnClassifier.components.prepare_callbacks import PrepareCallback
from cnnClassifier.components.evaluation import Evaluation
from cnnClassifier import logger

STAGE_NAME = "Evaluation"

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.save_score()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage: {STAGE_NAME} started <<<<<<")

        obj = EvaluationPipeline()
        obj.main()

        logger.info(f">>>>>> stage: {STAGE_NAME} completed <<<<<<")

    except Exception as e:
        logger.exception(e)
        raise e
