import os
from strands import Agent
from strands_tools import retrieve

# 環境変数でナレッジベースIDとリージョンを指定
os.environ["KNOWLEDGE_BASE_ID"] = "ナレッジベースID"
os.environ["AWS_REGION"] = "us-east-1"

agent = Agent(
    tools=[retrieve],
    system_prompt="社内規定を参照して正確に回答してください。"
)

agent("出張時の宿泊費の上限を教えて")
