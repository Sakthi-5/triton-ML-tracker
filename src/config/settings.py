from enum import Enum
from pathlib import Path

from pydantic import BaseModel, Field, field_validator


class Device(str, Enum):
    CPU = "cpu"
    GPU = "gpu"


class PipelineConfig(BaseModel):
    data_path: Path
    batch_size: int = Field(gt=0)
    image_size: int = Field(gt=0)
    mode: str
    device: Device
    threshold: float = Field(ge=0.0, le=1.0)

    @field_validator("data_path")
    @classmethod
    def validate_data_path(cls, value):
        if not value.exists():
            raise ValueError("Data path does not exist")

        return value

    @field_validator("mode")
    @classmethod
    def validate_mode(cls, value):
        allowed_modes = {"train", "inference"}

        if value not in allowed_modes:
            raise ValueError(
                "Mode must be either 'train' or 'inference'"
            )

        return value