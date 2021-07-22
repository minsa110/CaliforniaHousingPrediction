FROM jupyter/minimal-notebook

# Set arguments
ARG CONTAINER_USER=minsa110
ARG GIT_URI=https://github.com/minsa110/CaliforniaHousingPrediction.git
ARG REPO_DIR=repo

# Configure sudo
USER root
RUN \
    echo "*** configure sudo ***" && \
    adduser ${CONTAINER_USER} && \
    adduser ${CONTAINER_USER} sudo && \
    echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

# Clone repo
USER ${CONTAINER_USER}
RUN \
    echo "*** clone ${GIT_URI} ***" && \
    git clone --single-branch ${GIT_URI} /home/${CONTAINER_USER}/${REPO_DIR}

# Install libraries
RUN \
    echo "*** install libraries ***" && \
    pip install -r requirements.txt

# Copy all files
COPY . /

# Start up the notebook
USER ${CONTAINER_USER}
COPY --chown=${CONTAINER_USER} run_script /home/${CONTAINER_USER}
RUN \
    echo "*** start notebook ***" && \
    chmod +x ./run_script
CMD ["./run_script"]