from strands import Agent

agent = Agent(
    # 非ストリーミング方式
    callback_handler=None,
)
result = agent("こんにちは")

# エージェントの実行結果を受け取り、メッセージのテキストを非ストリーミング方式で出力する
print(result.message["content"][-1]["text"])
