from src.logging_config import configure_logging
from src.pipeline.pipeline import Pipeline
from src.pipeline.steps import (
    CleanStep,
    FilterStep,
    NormalizeStep,
    PrefixStep,
)


configure_logging()

data = [
    " Alice ",
    "",
    "Bob",
    " Charlie ",
    "Ethan",
]

pipeline = Pipeline(
    [
        CleanStep(),
        FilterStep(),
        NormalizeStep(),
        PrefixStep(),
    ]
)

result = pipeline.run(data)

print("Input:", data)
print("Output:", result)