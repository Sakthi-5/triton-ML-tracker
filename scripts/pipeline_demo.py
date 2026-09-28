from src.pipeline.pipeline import Pipeline
from src.pipeline.steps import CleanStep, FilterStep, PrefixStep


data = [" Alice ", "", "Bob", " Charlie ", "Ethan"]

pipeline = Pipeline([
    CleanStep(),
    FilterStep(),
    PrefixStep()
])

result = pipeline.run(data)

print("Input:", data)
print("Output:", result)