# ТиАБД

# Setup jupyter notebook with venv

## Install jupyter & ipykernel dependencies

1. `python3 -m venv .venv`
2. `source .venv/bin/activate`
3. `pip3 install jupyter notebook ipykernel`
4. `deactivate && source .venv/bin/activate` (`which ipython` now prints correct ipython - the one that belongins to the venv)
5. `ipython kernel install --user --name=notebook-venv`

## Install dependencies

1. `pip3 install pandas`
2. `pip3 freeze > requirements.txt`

## Installing from the *requirements.txt*

Similar to the "*Install jupyter & ipykernel from the dependencies*" section.
Except for the `pip3 install -r requirements.txt` command.

## Run jupyter

1. `jupyter notebook`

