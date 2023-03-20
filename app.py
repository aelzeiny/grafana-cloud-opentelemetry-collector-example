# These are the necessary import declarations
from opentelemetry import trace, context
from opentelemetry import metrics
import otel_lib
from opentelemetry.trace import NonRecordingSpan

from random import randint
from flask import Flask, request

tracer = trace.get_tracer(__name__)
# Acquire a meter.
meter = metrics.get_meter(__name__)

# Now create a counter instrument to make measurements with
roll_counter = meter.create_counter(
    "roll_counter",
    description="The number of rolls by roll value",
)

app = Flask(__name__)


def set_opentelemetry_context(*_, **__):
    serialized_ctx = request.headers.get('_OTEL_', None)
    if serialized_ctx:
        span_ctx = otel_lib.deserialize_ctx(serialized_ctx)
        ctx = trace.set_span_in_context(NonRecordingSpan(span_ctx))
        context.attach(ctx)


app.before_request_funcs.setdefault(None, []).insert(0, set_opentelemetry_context)


@app.route("/rolldice")
def roll_dice():
    return str(do_roll())


def do_roll():
    with tracer.start_as_current_span("do_roll") as rollspan:
        res = randint(1, 6)
        rollspan.set_attribute("roll.value", res)
        # This adds 1 to the counter for the given roll value
        roll_counter.add(1, {"roll.value": res})
        return res
