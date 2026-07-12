import json
import math

import boto3

# Bedrock Runtimeを呼び出すクライアントを生成
client = boto3.client("bedrock-runtime")


# 円の面積を計算するツール（ツールとして実行する Python 関数）
def circle_area_tool(radius: float) -> str:
    area = math.pi * radius**2
    return f"{area:.10f}"


# ツール名とツール関数を辞書型で保持
tool_list = {"circle_area_tool": circle_area_tool}

# ツール定義
# モデルはこのJSON定義をもとに、実行すべきツール（関数）を判断し、呼び出しパラメータを生成する
# description に具体的な例示を含めることで、モデルが正しく判断しやすくなる
tool_spec = {
    "toolSpec": {
        "name": "circle_area_tool",
        "description": "円の面積を計算するツール",
        "inputSchema": {
            "json": {
                "type": "object",
                "properties": {
                    "radius": {
                        "type": "number",
                        "description": "円の半径（cm）",
                    }
                },
                "required": ["radius"],
            }
        },
    }
}

# メッセージを作成
messages = [
    {
        "role": "user",
        "content": [
            # 送信プロンプト
            {"text": "半径3センチと半径7センチの円の面積を教えて"},
        ],
    },
]

# Converse API呼び出し
response = client.converse(
    modelId="us.anthropic.claude-sonnet-4-6",
    messages=messages,
    toolConfig={"tools": [tool_spec]},  # ツール定義を指定
)

while True:
    tool_request = []
    # Converse APIのレスポンスを解析し、ツール呼び出し要求があれば保持する
    # print("response:", json.dumps(response, indent=2, ensure_ascii=False))
    # 
    # レスポンスの例：
    # response: {
    #   "ResponseMetadata": {
    #     "RequestId": "4f277db7-e9cb-459a-8e92-a8df3c91432a",
    #     "HTTPStatusCode": 200,
    #     "HTTPHeaders": {
    #       "date": "Sun, 12 Jul 2026 06:03:34 GMT",
    #       "content-type": "application/json",
    #       "content-length": "616",
    #       "connection": "keep-alive",
    #       "x-amzn-requestid": "4f277db7-e9cb-459a-8e92-a8df3c91432a"
    #     },
    #     "RetryAttempts": 0
    #   },
    #   "output": {
    #     "message": {
    #       "role": "assistant",
    #       "content": [
    #         {
    #           "text": "2つの円の面積を同時に計算しますね！"
    #         },
    #         {
    #           "toolUse": {
    #             "toolUseId": "tooluse_xahCh9zaTLJ43B4X8JiqY0",
    #             "name": "circle_area_tool",
    #             "input": {
    #               "radius": 3
    #             },
    #             "type": "tool_use"
    #           }
    #         },
    #         {
    #           "toolUse": {
    #             "toolUseId": "tooluse_WyPZKy3J8X8FPS2chOJYiq",
    #             "name": "circle_area_tool",
    #             "input": {
    #               "radius": 7
    #             },
    #             "type": "tool_use"
    #           }
    #         }
    #       ]
    #     }
    #   },
    #   "stopReason": "tool_use",
    #   "usage": {
    #     "inputTokens": 597,
    #     "outputTokens": 112,
    #     "totalTokens": 709,
    #     "cacheReadInputTokens": 0,
    #     "cacheWriteInputTokens": 0
    #   },
    #   "metrics": {
    #     "latencyMs": 1640
    #   }
    # }
    for content in response["output"]["message"]["content"]:
        if "text" in content:
            print(f"text: {content['text']}")
        # toolUse
        # モデルがプログラムに対して実行を依頼しているツール。
        # **モデルは自分でコードを実行できないため、プログラム側でツールを実行する必要がある**。
        if "toolUse" in content:
            tool_request.append(content)

    # ツール呼び出し要求がなければwhileを抜ける
    if len(tool_request) == 0:
        break

    # Bedrockのレスポンスをメッセージに追加
    messages.append(response["output"]["message"])

    # ツール実行結果を格納する変数
    tool_result = []

    for tool_use in tool_request:
        tool_use_id = tool_use["toolUse"]["toolUseId"]
        tool_name = tool_use["toolUse"]["name"]
        tool_input = tool_use["toolUse"]["input"]

        print(
            f"tool_id: {tool_use_id},  tool_name: {tool_name},"
            f" tool_input: {tool_input}"
        )

        # ツールリストから呼び出すツールを取得
        tool = tool_list[tool_name]

        # ツールを実行
        result = tool(**tool_input)

        print(f"tool_result: {result}")

        # ツール実行結果を保持
        tool_result.append(
            {
                "toolResult": {
                    "toolUseId": tool_use_id,
                    "content": [{"text": result}],
                }
            }
        )

    # ツール実行結果をメッセージに追加
    messages.append({"role": "user", "content": tool_result})

    # ツール実行結果を含めたメッセージを再度Bedrockに送信
    response = client.converse(
        modelId="us.anthropic.claude-sonnet-4-6",
        messages=messages,
        toolConfig={"tools": [tool_spec]},
    )
