class PipelineError(Exception):
    """Base exception for the ML pipeline."""


class DataValidationError(PipelineError):
    """Raised when input data is invalid."""


class ConfigError(PipelineError):
    """Raised when pipeline configuration is invalid."""


class ProcessingError(PipelineError):
    """Raised when a pipeline step fails."""