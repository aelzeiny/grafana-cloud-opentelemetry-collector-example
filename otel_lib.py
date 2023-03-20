from opentelemetry.trace.span import SpanContext, TraceFlags
# import zlib


def serialize_ctx(ctx: SpanContext) -> str:
    """Serialize a SpanContext to a hexified string. Used for sending over the wire."""
    bytearr = bytearray()
    bytearr.extend(ctx.trace_id.to_bytes(128, 'little'))
    bytearr.extend(ctx.span_id.to_bytes(64, 'little'))
    bytearr.extend(ctx.trace_flags.to_bytes(ctx.trace_flags.bit_length(), 'little'))
    # return zlib.compress(bytearr, level=1).hex()
    return bytearr.hex()


def deserialize_ctx(val: str, is_remote: bool = True) -> SpanContext:
    """Deserialize a hexified string to a SpanContext."""
    # ctx_bytes = zlib.decompress(bytearray.fromhex(val))
    ctx_bytes = bytearray.fromhex(val)
    trace_bytes = ctx_bytes[:128]
    span_bytes = ctx_bytes[128:128+64]
    flag_bytes = ctx_bytes[128+64:]
    return SpanContext(
        int.from_bytes(trace_bytes, 'little'),
        int.from_bytes(span_bytes, 'little'),
        is_remote,
        trace_flags=TraceFlags(int.from_bytes(flag_bytes, 'little'))
    )
    