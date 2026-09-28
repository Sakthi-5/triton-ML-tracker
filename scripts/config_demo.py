from src.config.settings import PipelineConfig


config = PipelineConfig(
    data_path="data/raw/does_not_exist.csv",
    batch_size=32,
    image_size=224,
    mode="train",
    device="cpu",
    threshold=0.8,
)

print("Configuration loaded successfully")
print(config)