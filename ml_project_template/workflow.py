# AUTOGENERATED! DO NOT EDIT! File to edit: ../03_workflow.ipynb.

# %% auto 0
__all__ = ['cwd', 'save_notebooks_to']

# %% ../03_workflow.ipynb 5
import papermill
from pathlib import Path
import os

# your code here

# %% ../03_workflow.ipynb 11
"""
A workflow to re-run your machine learning workflow automatically.

This example script will
- rebuild your python module
- run data notebook to reload and clean data
- run model notebook to sw test your model
- run loss notebook to train and evaluate your model with full data,
    and save or deploy it for further use

Feel free to edit!
"""

cwd = Path().cwd()
save_notebooks_to = cwd / "results" / "notebooks"
# Hint! you can also create time or setup -stamped folders to store your results!

# make sure changes are updated to module
# (this will do nothing if you run the workflow from inside a notebook)
os.system("nbdev_build_lib")

# run workflow
for notebook in ["00_data.ipynb", "01_model.ipynb", "02_loss.ipynb"]:
    papermill.execute_notebook(
        notebook,  # this notebook will be executed
        save_notebooks_to
        / ("_" + notebook),  # this is where the executed notebook will be saved
        # (notebooks named with '_' -prefix are ignored by nbdev build_lib & build_docs!)
        parameters={"seed": 1},  # you can change notebook parameters
        kernel_name="python38myenv",
    )  # note: change kernel according to your project setup!
