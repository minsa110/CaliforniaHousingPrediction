FROM mambaorg/micromamba:0.22.0

USER root
RUN apt-get update && DEBIAN_FRONTEND=“noninteractive” apt-get install -y --no-install-recommends \
       nginx \
       ca-certificates \
       apache2-utils \
       certbot \
       python3-certbot-nginx \
       sudo \
       cifs-utils \
       && \
    rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get -y install cron

RUN mkdir /opt/demo_azure
RUN chmod -R 777 /opt/demo_azure
WORKDIR /opt/demo_azure

COPY --chown=$MAMBA_USER:$MAMBA_USER environment.yml environment.yml
RUN micromamba install -y -n base -f environment.yml && \
   micromamba clean --all --yes

COPY model.pkl model.pkl
COPY app.py app.py
COPY run.sh run.sh
COPY nginx.conf /etc/nginx/nginx.conf

USER root
RUN chmod a+x run.sh
CMD ["./run.sh"]