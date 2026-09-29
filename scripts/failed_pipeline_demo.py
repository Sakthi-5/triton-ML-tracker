import logging

from src.exceptions.errors import ProcessingError
from src.logging_config import configure_logging
from src.pipeline.pipeline import Pipeline


configure_logging()

logger = logging.getLogger(__name__)


class FailingStep:

    def process(self, data):
        raise ValueError("Demo failure: invalid input encountered")


pipeline = Pipeline([FailingStep()])

try:
    pipeline.run(["Alice", "Bob"])
except ProcessingError:
    logger.exception("Pipeline run failed")