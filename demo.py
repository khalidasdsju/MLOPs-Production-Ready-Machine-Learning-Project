# demo.py
from HF.pipline.training_pipeline import TrainPipeline
from HF.entity.config_entity import TrainingPipelineConfig

# Initialize the training pipeline configuration
training_pipeline_config = TrainingPipelineConfig()

# Create an instance of TrainPipeline with the training pipeline configuration
obj = TrainPipeline(training_pipeline_config)

# Run the pipeline
obj.run_pipeline()
