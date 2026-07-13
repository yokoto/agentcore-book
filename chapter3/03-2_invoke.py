from strands import Agent


# ストリーミング処理を行う関数
def print_callback_handler(**kwargs):
    print(kwargs)


agent = Agent(
    # ストリーミング方式 – ストリーミング処理を行う関数を指定
    callback_handler=print_callback_handler
)

# エージェントの実行結果がコンソールにストリーミングで出力される
agent("こんにちは")

# $ uv run 03-2_invoke.py
# {'init_event_loop': True}
# {'start': True}
# {'start_event_loop': True}
# {'event': {'messageStart': {'role': 'assistant'}}}
# {'event': {'contentBlockDelta': {'delta': {'text': 'こ'}, 'contentBlockIndex': 0}}}
# {'data': 'こ', 'delta': {'text': 'こ'}, 'agent': <strands.agent.agent.Agent object at 0x103fa5010>, 'event_loop_cycle_id': UUID('8009acac-1a0e-4613-9217-d0e5e2c46394'), 'request_state': {}, 'event_loop_cycle_trace': <strands.telemetry.metrics.Trace object at 0x1047d6cf0>, 'event_loop_cycle_span': NonRecordingSpan(SpanContext(trace_id=0x00000000000000000000000000000000, span_id=0x0000000000000000, trace_flags=0x00, trace_state=[], is_remote=False))}
# {'event': {'contentBlockDelta': {'delta': {'text': 'んにちは！'}, 'contentBlockIndex': 0}}}
# {'data': 'んにちは！', 'delta': {'text': 'んにちは！'}, 'agent': <strands.agent.agent.Agent object at 0x103fa5010>, 'event_loop_cycle_id': UUID('8009acac-1a0e-4613-9217-d0e5e2c46394'), 'request_state': {}, 'event_loop_cycle_trace': <strands.telemetry.metrics.Trace object at 0x1047d6cf0>, 'event_loop_cycle_span': NonRecordingSpan(SpanContext(trace_id=0x00000000000000000000000000000000, span_id=0x0000000000000000, trace_flags=0x00, trace_state=[], is_remote=False))}
# {'event': {'contentBlockDelta': {'delta': {'text': '👋\n\nお'}, 'contentBlockIndex': 0}}}
# {'data': '👋\n\nお', 'delta': {'text': '👋\n\nお'}, 'agent': <strands.agent.agent.Agent object at 0x103fa5010>, 'event_loop_cycle_id': UUID('8009acac-1a0e-4613-9217-d0e5e2c46394'), 'request_state': {}, 'event_loop_cycle_trace': <strands.telemetry.metrics.Trace object at 0x1047d6cf0>, 'event_loop_cycle_span': NonRecordingSpan(SpanContext(trace_id=0x00000000000000000000000000000000, span_id=0x0000000000000000, trace_flags=0x00, trace_state=[], is_remote=False))}
# {'event': {'contentBlockDelta': {'delta': {'text': '元'}, 'contentBlockIndex': 0}}}
# {'data': '元', 'delta': {'text': '元'}, 'agent': <strands.agent.agent.Agent object at 0x103fa5010>, 'event_loop_cycle_id': UUID('8009acac-1a0e-4613-9217-d0e5e2c46394'), 'request_state': {}, 'event_loop_cycle_trace': <strands.telemetry.metrics.Trace object at 0x1047d6cf0>, 'event_loop_cycle_span': NonRecordingSpan(SpanContext(trace_id=0x00000000000000000000000000000000, span_id=0x0000000000000000, trace_flags=0x00, trace_state=[], is_remote=False))}
# {'event': {'contentBlockDelta': {'delta': {'text': '気ですか？何'}, 'contentBlockIndex': 0}}}
# {'data': '気ですか？何', 'delta': {'text': '気ですか？何'}, 'agent': <strands.agent.agent.Agent object at 0x103fa5010>, 'event_loop_cycle_id': UUID('8009acac-1a0e-4613-9217-d0e5e2c46394'), 'request_state': {}, 'event_loop_cycle_trace': <strands.telemetry.metrics.Trace object at 0x1047d6cf0>, 'event_loop_cycle_span': NonRecordingSpan(SpanContext(trace_id=0x00000000000000000000000000000000, span_id=0x0000000000000000, trace_flags=0x00, trace_state=[], is_remote=False))}
# {'event': {'contentBlockDelta': {'delta': {'text': 'かお手伝いできること'}, 'contentBlockIndex': 0}}}
# {'data': 'かお手伝いできること', 'delta': {'text': 'かお手伝いできること'}, 'agent': <strands.agent.agent.Agent object at 0x103fa5010>, 'event_loop_cycle_id': UUID('8009acac-1a0e-4613-9217-d0e5e2c46394'), 'request_state': {}, 'event_loop_cycle_trace': <strands.telemetry.metrics.Trace object at 0x1047d6cf0>, 'event_loop_cycle_span': NonRecordingSpan(SpanContext(trace_id=0x00000000000000000000000000000000, span_id=0x0000000000000000, trace_flags=0x00, trace_state=[], is_remote=False))}
# {'event': {'contentBlockDelta': {'delta': {'text': 'は'}, 'contentBlockIndex': 0}}}
# {'data': 'は', 'delta': {'text': 'は'}, 'agent': <strands.agent.agent.Agent object at 0x103fa5010>, 'event_loop_cycle_id': UUID('8009acac-1a0e-4613-9217-d0e5e2c46394'), 'request_state': {}, 'event_loop_cycle_trace': <strands.telemetry.metrics.Trace object at 0x1047d6cf0>, 'event_loop_cycle_span': NonRecordingSpan(SpanContext(trace_id=0x00000000000000000000000000000000, span_id=0x0000000000000000, trace_flags=0x00, trace_state=[], is_remote=False))}
# {'event': {'contentBlockDelta': {'delta': {'text': 'ありますか？'}, 'contentBlockIndex': 0}}}
# {'data': 'ありますか？', 'delta': {'text': 'ありますか？'}, 'agent': <strands.agent.agent.Agent object at 0x103fa5010>, 'event_loop_cycle_id': UUID('8009acac-1a0e-4613-9217-d0e5e2c46394'), 'request_state': {}, 'event_loop_cycle_trace': <strands.telemetry.metrics.Trace object at 0x1047d6cf0>, 'event_loop_cycle_span': NonRecordingSpan(SpanContext(trace_id=0x00000000000000000000000000000000, span_id=0x0000000000000000, trace_flags=0x00, trace_state=[], is_remote=False))}
# {'event': {'contentBlockDelta': {'delta': {'text': '😊'}, 'contentBlockIndex': 0}}}
# {'data': '😊', 'delta': {'text': '😊'}, 'agent': <strands.agent.agent.Agent object at 0x103fa5010>, 'event_loop_cycle_id': UUID('8009acac-1a0e-4613-9217-d0e5e2c46394'), 'request_state': {}, 'event_loop_cycle_trace': <strands.telemetry.metrics.Trace object at 0x1047d6cf0>, 'event_loop_cycle_span': NonRecordingSpan(SpanContext(trace_id=0x00000000000000000000000000000000, span_id=0x0000000000000000, trace_flags=0x00, trace_state=[], is_remote=False))}
# {'event': {'contentBlockStop': {'contentBlockIndex': 0}}}
# {'event': {'messageStop': {'stopReason': 'end_turn'}}}
# {'event': {'metadata': {'usage': {'inputTokens': 12, 'outputTokens': 35, 'totalTokens': 47}, 'metrics': {'latencyMs': 1293}}}}
# {'message': {'role': 'assistant', 'content': [{'text': 'こんにちは！👋\n\nお元気ですか？何かお手伝いできることはありますか？😊'}], 'metadata': {'usage': {'inputTokens': 12, 'outputTokens': 35, 'totalTokens': 47}, 'metrics': {'latencyMs': 1293, 'timeToFirstByteMs': 1074}}}}
# {'result': AgentResult(stop_reason='end_turn', message={'role': 'assistant', 'content': [{'text': 'こんにちは！👋\n\nお元気ですか？何かお手伝いできることはありますか？😊'}], 'metadata': {'usage': {'inputTokens': 12, 'outputTokens': 35, 'totalTokens': 47}, 'metrics': {'latencyMs': 1293, 'timeToFirstByteMs': 1074}}}, metrics=EventLoopMetrics(cycle_count=1, tool_metrics={}, cycle_durations=[2.779223918914795], agent_invocations=[AgentInvocation(cycles=[EventLoopCycleMetric(event_loop_cycle_id='8009acac-1a0e-4613-9217-d0e5e2c46394', usage={'inputTokens': 12, 'outputTokens': 35, 'totalTokens': 47})], usage={'inputTokens': 12, 'outputTokens': 35, 'totalTokens': 47})], traces=[<strands.telemetry.metrics.Trace object at 0x1047d6cf0>], accumulated_usage={'inputTokens': 12, 'outputTokens': 35, 'totalTokens': 47}, accumulated_metrics={'latencyMs': 1293}), state={}, interrupts=None, structured_output=None)}
