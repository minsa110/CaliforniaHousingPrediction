FROM jupyter/minimal-notebook

# Set arguments
ARG CONTAINER_USER=jovyan
ARG GIT_URI=https://github.com/minsa110/CaliforniaHousingPrediction.git
ARG REPO_DIR=repo

# Clone repo
USER ${CONTAINER_USER}
RUN \
    echo "*** cloning repo ${GIT_URI} ***" && \
    git clone --single-branch ${GIT_URI} /home/${CONTAINER_USER}/${REPO_DIR}

COPY --chown=${CONTAINER_USER}:users environment.yml /home/${CONTAINER_USER}/${REPO_DIR}
RUN \
    echo "*** start notebook ***" && \
    chmod +x /home/${CONTAINER_USER}/${REPO_DIR}/environment.yml
RUN conda env update --file /home/${CONTAINER_USER}/${REPO_DIR}/environment.yml

# Start up the notebook
COPY --chown=${CONTAINER_USER}:users run_script /home/${CONTAINER_USER}
RUN \
    echo "*** start notebook ***" && \
    chmod +x ./run_script
CMD ["./run_script"]
