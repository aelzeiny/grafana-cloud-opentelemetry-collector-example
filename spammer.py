import requests
import time
import otel_lib

from opentelemetry import trace


tracer = trace.get_tracer(__name__)


def spam():
    while True:
        with tracer.start_as_current_span("spam"):
            with tracer.start_as_current_span("spam-request") as spam_req_span:
                span_ctx = spam_req_span.get_span_context()
                requests.get('http://app:5000/rolldice', headers=dict(_OTEL_=otel_lib.serialize_ctx(span_ctx)))
        with tracer.start_as_current_span("spam-sleep"):
            time.sleep(5)


if __name__ == '__main__':
    time.sleep(5)
    spam()
