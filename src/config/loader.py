from pydantic import ValidationError

from src.config.settings import PipelineConfig
from src.exceptions.errors import ConfigError


def load_config(**values):
    try:
        return PipelineConfig(**values)
    except ValidationError as error:
        raise ConfigError(
            f"Configuration validation failed: {error}"
        ) from error