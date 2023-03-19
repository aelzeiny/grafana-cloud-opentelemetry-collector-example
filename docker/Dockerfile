
FROM python:slim-buster

WORKDIR app
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .

EXPOSE 5000
# CMD ["/usr/local/bin/opentelemetry-instrument", "--traces_exporter", "console", "--metrics_exporter", "console", "flask", "run", "--host", "0.0.0.0"]
CMD ["/usr/local/bin/opentelemetry-instrument", "--service_name", "gambler", "--exporter_otlp_endpoint", "http://collector:4317", "flask", "run", "--host", "0.0.0.0"]
