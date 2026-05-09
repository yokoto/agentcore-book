import boto3
import uuid

# AgentCore用のAPIクライアントを作成
client = boto3.client("bedrock-agentcore")

# ハーネスのエージェントを呼び出す
response = client.invoke_harness(
    harnessArn="<ハーネスARN>",
    runtimeSessionId=str(uuid.uuid4()),
    messages=[{"role": "user", "content": [{"text": "元気？"}]}]
)

# レスポンスをストリーミング表示
for event in response["stream"]:
    if "contentBlockDelta" in event:
        delta = event["contentBlockDelta"].get("delta", {})
        if "text" in delta:
            print(delta["text"], end="")
