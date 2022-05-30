#!/usr/bin/env sh

cd target/generated-sources/swagger
echo $(pwd)

python -m pip install --user --upgrade pip
pip install virtualenv
python -m virtualenv .venv

echo "Activating virtual environment in ${SHELL} shell"
source .venv/bin/activate

pip install sphinx
pip install sphinx-rtd-theme
export SPHINX_APIDOC_OPTIONS="members,show-inheritance"
sphinx-apidoc -o docs/sources tasks_client **/OneOf*/**/*.py **/OneOf*/*.py

deactivate
rm -rf .venv
