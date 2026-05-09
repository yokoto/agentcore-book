import boto3

client = boto3.client("bedrock-agent-runtime")
prompt = "質問文"

response = client.retrieve_and_generate(
    retrieveAndGenerateConfiguration={
        "knowledgeBaseConfiguration": {
            "knowledgeBaseId": "ナレッジベースID",
            "modelArn": "モデルARN",  # 回答生成に使用するLLM
            "retrievalConfiguration": {
                "vectorSearchConfiguration": {
                    "numberOfResults": 100,  # チャンク設定
                    "overrideSearchType": "SEMANTIC", # 検索タイプ
                    "filter": {},  # フィルター
                    "rerankingConfiguration": {}, # リランキング
                }
            },
            "generationConfiguration": {},  # ガードレール
            "orchestrationConfiguration": {
                "queryTransformationConfiguration": {} # クエリ分解
            },
        },
        "type": "KNOWLEDGE_BASE",
    },
    input={"text": prompt},
)
