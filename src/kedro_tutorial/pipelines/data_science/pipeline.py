"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.2
"""

from kedro.pipeline import Pipeline, node, pipeline

from kedro_tutorial.pipelines.data_science.nodes import (evaluate_model,
                                                         split_data,
                                                         train_model)


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=split_data,
            inputs=["model_input_table", "params:model_options"],
            outputs=["X_train", "X_test", "y_train", "y_test"],
            name="split_data_node",
        ),
        node(
            func=train_model,
            inputs=["X_train", "y_train"],
            outputs="regressor",
            name="train_model_node",
        ),
        node(
            func=evaluate_model,
            inputs=["regressor", "X_test", "y_test"],
            outputs=None,
            name="evaluate_model_node",
        ),
    ])

    # ds_pipeline_1 = pipeline(
    #     pipe=pipeline_instance,
    #     inputs="model_input_table",
    #     namespace="active_modelling_pipeline",
    # )
    # ds_pipeline_2 = pipeline(
    #     pipe=pipeline_instance,
    #     inputs="model_input_table",
    #     namespace="candidate_modelling_pipeline",
    # )
    # return pipeline(
    #     pipe=ds_pipeline_1 + ds_pipeline_2,
    #     inputs="model_input_table",
    #     namespace="data_science",
    # )