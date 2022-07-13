cd target/generated-sources/swagger
echo $(pwd)
pip install sphinx
pip install sphinx-rtd-theme
export SPHINX_APIDOC_OPTIONS="members,show-inheritance"
sphinx-apidoc -o docs/sources prism_client **/OneOf*/**/*.py **/OneOf*/*.py