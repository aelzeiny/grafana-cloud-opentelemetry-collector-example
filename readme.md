# Grafana Cloud + OpenTelemetry Collector

This repo is me banging my head against the wall to get OTel Collector working with Grafana cloud. I had no idea it was going to be _this_ hard to configure YAML.

See also [Connect OpenTelemetry Collector to Grafana Cloud databases](https://grafana.com/docs/opentelemetry/collector/send-otlp-to-grafana-cloud-databases/)

Run:

```
docker-compose up
```

The core config file is located at ./config/otel-collector/config-cloud.yaml.

### My Graphana Cloud Variables

- **TRACES_URL**: tempo-us-central1.grafana.net:443
- **TRACES_USER_ID**: 180575

- **LOGS_URL**:https://logs-prod3.grafana.net/loki/api/v1/push
- **LOGS_USER_ID**: 184062

- **METRICS_URL**:https://prometheus-prod-10-prod-us-central-0.grafana.net/api/prom/push
- **METRICS_USER_ID**: 370184

_Note_: All API Keys committed in this repo have been revoked.
