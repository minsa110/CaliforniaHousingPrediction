FROM ubuntu:18.04

# Set arguments
ARG CONTAINER_USER=minsa110
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
# RUN source /opt/conda/etc/profile.d/conda.sh
# RUN conda activate ${CONDA_ENV}
# RUN conda install ipykernel
# RUN python kernel install --${CONTAINER_USER} --name=${CONDA_ENV}}

# Start up the notebook
COPY --chown=${CONTAINER_USER}:users run_script /home/${CONTAINER_USER}
RUN \
    echo "*** start notebook ***" && \
    chmod +x ./run_script
CMD ["./run_script"]