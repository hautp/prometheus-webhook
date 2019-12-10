FROM python:3.8-alpine

RUN mkdir /app/prometheus-webhook/ -p

EXPOSE 5000 

COPY src/requirements.txt /app/
RUN  pip install --upgrade pip && \
	pip install -r /app/requirements.txt

COPY src/. /app/prometheus-webhook/

WORKDIR /app/prometheus-webhook/

RUN chmod +x docker_entrypoint.sh
ENTRYPOINT ["sh", "docker_entrypoint.sh"]
