FROM pytorch/pytorch:2.2.0-cuda12.1-cudnn8-runtime

# Instalar utilidades necesarias
RUN apt-get update && apt-get install -y \
    git \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Crear usuario compatible con VSCode
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME

# Instalar librerías Data Science
RUN pip install --no-cache-dir \
    numpy \
    pandas \
    polars \
    matplotlib \
    seaborn \
    scikit-learn \
    xgboost \
    lightgbm \
    optuna \
    plotly \
    jupyterlab \
    mlflow \
    dvc \
    wandb \
    transformers \
    datasets \
    ipykernel

RUN pip install --upgrade packaging && pip install --upgrade jupyterlab

# Cambiar a usuario normal
USER $USERNAME
WORKDIR /home/$USERNAME

# Registrar kernel
RUN python -m ipykernel install --user --name ds-env