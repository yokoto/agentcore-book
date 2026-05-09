import boto3
import json

# Boto3クライアントのendpoint_urlにゲートウェイのURLを指定
client = boto3.client(
    service_name="bedrock-agentcore",
    endpoint_url="https://<ゲートウェイID>.gateway.bedrock-agentcore.us-east-1.amazonaws.com/<ターゲット名>"
)

# HTTPターゲット経由でAgentCoreランタイムを呼び出す
response = client.invoke_agent_runtime(
   agentRuntimeArn="arn:aws:bedrock-agentcore:us-east-1:xxxxxxxxxxxx:runtime/handson_MyAgent-XXXXXXXXXX", # あなたのランタイムARNを記載
   runtimeSessionId="this-is-runtime-session-id-000001",
   payload=json.dumps({"prompt": "こんにちは"})
)

# レスポンスからテキスト内容を取り出して表示
content = response["response"].read().decode('utf-8')
print(json.loads(content))
