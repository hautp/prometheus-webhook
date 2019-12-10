# Prometheus webhook
## Introduction
> Note: This project is using python v3.6.9
v1. Prometheus webhook only support for send messages notify to Microsoft Teams channel.

##Installation 
### Run app with WSGI
1. Clone repository
```bash
git clone https://github.com/hautp/prometheus-webhook.git
```

2. Install package dependencies
```bash
cd prometheus-webhook/src/
pip install -r requirements.txt
```

3. Start application
```bash
gunicorn -c app_config.py webhook:app
```

### Run app with Docker
1. Clone repository
```bash
git clone https://github.com/hautp/prometheus-webhook.git
```

2. Build image
```bash
cd prometheus-webhook
docker build -t "prometheus-webhook" .
```

3. Run image
```bash
docker run -it -d --name "prome-webhook" -p 5000:5000 prometheus-webhook
```
