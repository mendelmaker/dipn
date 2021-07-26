#! /bin/bash

source install_acme.sh
source environment.sh

echo -e '\e[93m \n http://localhost:8888/?token=assistive \n \e[0m'

jupyter notebook \
    --NotebookApp.allow_origin='https://colab.research.google.com' \
    --NotebookApp.token='assistive' \
    --NotebookApp.port_retries=0 \
    --notebook-dir /home/dipn/ \
    --port=8888 \
    --allow-root \
    --no-browser \
    --ip=localhost
