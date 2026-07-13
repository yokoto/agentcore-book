import asyncio

from strands import Agent


# ストリーミング方式 – 非同期イテレータ方式
async def streaming():
    agent = Agent(
        # コールバックハンドラは指定しない
        callback_handler=None,
    )

    # stream_async()メソッドを使って、非同期イテレータでイベントを順次受け取る
    # https://strandsagents.com/docs/user-guide/concepts/streaming/async-iterators/#server-examples
    agent_stream = agent.stream_async("こんにちは")

    # event にどのキーが含まれるかを調べることで、イベントの種類を判定できます。主なイベントは次のとおりです。
    # https://strandsagents.com/docs/user-guide/concepts/streaming/#event-types
    # ┌────────────────────────────────────┬──────────────────┬────────────────────────────────────────────────────────────────┐
    # │           イベントのキー             │       種類        │                              説明                               │
    # ├────────────────────────────────────┼──────────────────┼────────────────────────────────────────────────────────────────┤
    # │ init_event_loop / start_event_loop │ ライフサイクル      │ イベントループの初期化・サイクル開始を通知する                         │
    # ├────────────────────────────────────┼──────────────────┼────────────────────────────────────────────────────────────────┤
    # │ data                               │ モデルストリーム    │ モデルが生成したテキストの断片（トークン単位のチャンク）                 │
    # ├────────────────────────────────────┼──────────────────┼────────────────────────────────────────────────────────────────┤
    # │ current_tool_use                   │ ツール            │ 実行中のツールの情報（ツールを使う場合のみ）                           │
    # ├────────────────────────────────────┼──────────────────┼────────────────────────────────────────────────────────────────┤
    # │ message                            │ ライフサイクル      │ メッセージが1件完成したタイミングで、その完全な内容を含む               │
    # ├────────────────────────────────────┼──────────────────┼────────────────────────────────────────────────────────────────┤
    # │ result                             │ ライフサイクル      │ ストリームの最後に1回だけ発生し、最終結果（AgentResult）を含む         │
    # └────────────────────────────────────┴──────────────────┴────────────────────────────────────────────────────────────────┘
    async for event in agent_stream:
        if "message" in event: 
            message = event["message"]  # メッセージ
            # print(f"message: {message}") # メッセージの内容をコンソール出力
            # $ uv run 03-3_invoke.py
            # message: {'role': 'assistant', 'content': [{'text': 'こんにちは！👋\n\nお元気ですか？何かお手伝いできることはありますか？😊'}], 'metadata': {'usage': {'inputTokens': 12, 'outputTokens': 35, 'totalTokens': 47}, 'metrics': {'latencyMs': 1462, 'timeToFirstByteMs': 1235}}}
        if "result" in event:
            result = event["result"]  # 最終回答
            print(f"result: {result}") # 最終回答をコンソール出力
            # $ uv run 03-3_invoke.py
            # result: こんにちは！👋
            # 
            # お元気ですか？何かお手伝いできることはありますか？😊
        if "data" in event:
            data = event["data"]  # トークン単位のテキスト
            # print(data, end="")  # トークン単位でコンソール出力
            # $ uv run 03-3_invoke.py
            # こんにちは！😊
            #
            # お元気ですか？何かお手伝いできることはありますか？%

# 非同期関数を実行する
asyncio.run(streaming())
