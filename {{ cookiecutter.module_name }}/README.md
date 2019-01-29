{{cookiecutter.module_name}}
==============================

{{cookiecutter.description}}

Module Organization
------------

    ├── Makefile           <- Makefile with commands like `make test`
    ├── README.md          <- The README for this module.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    └── src                <- Source code for use in this project.
        ├── __init__.py    <- Makes src a Python module
        ├── data.py        <- Download or generate data
        ├── features.py    <- Turn raw data into features for modeling
        ├── models.py      <- Train and use models
        ├── blueprint.py   <- Define routes to extend the webapp, for Flask
        ├── tasks.py       <- Define workflow tasks, for Luigi
        └── visualize.py   <- Create exploratory and results oriented visualizations
