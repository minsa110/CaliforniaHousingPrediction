FROM jupyter/minimal-notebook

# Set arguments
ARG CONTAINER_USER=jovyan
ARG GIT_URI=https://github.com/minsa110/CaliforniaHousingPrediction.git
ARG REPO_DIR=repo
ARG CONDA_ENV=myenv

# Clone repo
USER ${CONTAINER_USER}
RUN \
    echo "*** cloning repo ${GIT_URI} ***" && \
    git clone --single-branch ${GIT_URI} /home/${CONTAINER_USER}/${REPO_DIR}

# Install libraries
RUN \
    echo "*** install libraries ***" && \
    conda create --name ${CONDA_ENV} python=3 --file "/home/${CONTAINER_USER}/${REPO_DIR}/spec-file.txt"
    #pip3 install -r "/home/${CONTAINER_USER}/${REPO_DIR}/requirements.txt"

# Activate conda environment and install ipykernel
RUN \
    source /opt/conda/etc/profile.d/conda.sh \
    conda activate ${CONDA_ENV} \
    conda install ipykernel \
    python kernel install --${CONTAINER_USER} --name=${CONDA_ENV}}

# Start up the notebook
COPY --chown=${CONTAINER_USER}:users run_script /home/${CONTAINER_USER}
RUN \
    echo "*** start notebook ***" && \
    chmod +x ./run_script2
CMD ["./run_script"]