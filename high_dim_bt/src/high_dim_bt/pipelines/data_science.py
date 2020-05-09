from typing import Dict

from kedro.pipeline import Pipeline, node

from high_dim_bt.nodes.data_science import fit_model, save_outputs


def create_pipeline(**kwargs) -> Dict[str, Pipeline]:

    fitted_model = node(
        func=fit_model,
        inputs=dict(
            X='X',
            y='y',
            date_col='params:date_col',
            abilities='starting_abilities'),
        outputs='fitted_model')

    save = node(
        func=save_outputs,
        inputs=dict(
            model='fitted_model'
        ),
        outputs=None)

    return Pipeline(
        [
            fitted_model,
            save
        ]
    )
