class BasePipeline:
    def run(self):
        print("Running pipeline")


class DataPipeline(BasePipeline):
    def load_data(self):
        print("Loading data")


class MLDataPipeline(DataPipeline):
    def train_model(self):
        print("Training model")


class ProductionMLPipeline(MLDataPipeline):
    def deploy_model(self):
        print("Deploying model")


pipeline = ProductionMLPipeline()

pipeline.run()
pipeline.load_data()
pipeline.train_model()
pipeline.deploy_model()