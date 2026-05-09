# 第5章 AgentCoreの概要とメイン機能「ランタイム」

この章のハンズオンが実施しやすいように、書籍に掲載されているコマンドをコピペしやすい形で掲載しています。

## 5.2.3 作成したエージェントを呼び出す

マネジメントコンソールで作成したハーネスのARNを `00_invoke_harness.py` 内の `<ハーネスARN>` に置き換えてから実行してください。

```bash
uv run 00_invoke_harness.py
```

## 5.3.2 AgentCore CLIでプロジェクトを作成する

```bash
npm install -g @aws/agentcore@1.0.0-preview.8
```

```bash
agentcore create
```

```bash
cd handson
```

## 5.3.4 AgentCoreランタイムへのデプロイ

```bash
agentcore deploy
```

## 5.3.5 デプロイしたエージェントの呼び出し

```bash
uv init --python 3.14
uv add "boto3[crt]==1.42.96"
```

```bash
touch invoke.py
```

```bash
uv run invoke.py
```
