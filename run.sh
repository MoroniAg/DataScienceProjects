#!/bin/bash

source /opt/conda/etc/profile.d/conda.sh && conda activate base
jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root