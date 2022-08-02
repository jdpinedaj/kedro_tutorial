"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline
from kedro_tutorial.pipelines import data_processing as dp


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """
    data_preprocessing_pipeline = dp.create_pipeline()

    return {
        "__default__": data_preprocessing_pipeline,
        "dp": data_preprocessing_pipeline
    }
