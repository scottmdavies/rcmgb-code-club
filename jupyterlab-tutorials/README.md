# Installing Jupyter Labs

virtualenv venv
pip3 install jupyterlab

jupyter lab --ip=0.0.0.0 --port=8080

jupyter nbconvert notebook.ipynb --to slides # reveal.js presentation, requires access to internet for CDN
