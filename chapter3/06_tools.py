from mcp.client.streamable_http import streamable_http_client
from strands import Agent, tool
from strands.tools.mcp import MCPClient
from strands_tools.tavily import tavily_search


# https://strandsagents.com/docs/user-guide/concepts/tools/custom-tools
# https://strandsagents.com/docs/api/python/strands.tools.decorator/#tool
# `@tool` デコレーターを付与することで、通常のPython関数をツールに変換できる。
@tool
def get_weather(location: str):
    """locationの天気を取得

    Args:
        location: 都市名
    """
    return f"{location}の天気は晴れで、気温は25℃です。"

# https://strandsagents.com/docs/user-guide/concepts/tools/custom-tools/#loading-function-based-tools
# tools: 関数ベースのツールを使用するには、それらをエージェントに渡す
agent = Agent(tools=[get_weather])
agent("東京の天気を教えて")

# https://www.tavily.com/
# tavily_search: 事前に環境変数 TAVILY_API_KEY に APIキーを設定しておく
agent = Agent(tools=[tavily_search])
agent("Strands Agentsの公式ドキュメントを検索して、MCPの概要を要約して")

# https://strandsagents.com/docs/user-guide/concepts/tools/mcp-tools/
# MCPClient: 追加ツールを提供するMCPサーバーとの通信を可能にする
#
# https://modelcontextprotocol.io/specification/2025-06-18/basic/transports#streamable-http
# MCP の標準トランスポート
#
# MCPクライアントとサーバーがメッセージをやり取りする通信手段の標準は次の2つだけ
#
# ① stdio — ローカル向け
# - MCPクライアントがサーバーをコマンドとして起動し、標準入出力でやり取りする
# - 例：uvx で起動するローカルの MCP サーバー
#
# ② Streamable HTTP — リモート向け
# - MCPクライアントはサーバーの単一のエンドポイントに HTTP POSTでメッセージを送信する。
# - レスポンスは JSON か、ストリーミング（SSE）
# - 例：06_tools.py で接続している AWS Knowledge MCP Server
mcp_client = MCPClient(
    # Streamable HTTP で、AWS Knowledge MCP Server（https://github.com/awslabs/mcp/tree/main/src/aws-knowledge-mcp-server） に接続する
    lambda: streamable_http_client("https://knowledge-mcp.global.api.aws")
)

agent = Agent(tools=[mcp_client])
agent(
    "AWSの最新ドキュメントを参照して、AgentCore EvaluationsとBedrock Evaluationsの違いを教えて"
)

# $ uv run 06_tools.py
# 東京の天気を取得します！
# Tool #1: get_weather
# 東京の現在の天気は以下の通りです：

# - **天気**: ☀️ 晴れ
# - **気温**: 25℃

# 気持ちの良い天気ですね！お出かけには最適な日和です。他に知りたいことがあればお気軽にどうぞ！Strands AgentsのMCPに関する公式ドキュメントを検索します。
# Tool #1: tavily_search

# Tool #2: tavily_search
# もう少し詳細なMCPツールのドキュメントを取得します。
# Tool #3: tavily_search
# 公式ドキュメントから十分な情報が集まりました。以下に要約します。

# ---

# # Strands Agents の MCP (Model Context Protocol) 概要

# > 📄 出典：[strandsagents.com 公式ドキュメント](https://strandsagents.com/docs/user-guide/concepts/tools/mcp-tools)

# ---

# ## 🔷 MCPとは？

# **Model Context Protocol (MCP)** は、アプリケーションが LLM（大規模言語モデル）にコンテキストを提供する方法を**標準化したオープンプロトコル**です。Strands Agents は MCP と統合することで、外部ツールやサービスを通じてエージェントの能力を拡張できます。

# ---

# ## 🔷 MCPの役割

# - エージェントと **MCPサーバー（外部ツール群）** の間の通信を仲介する
# - Strands Agents には **Python / TypeScript 両方**に対応した MCP サポートが組み込み済み
# - 既存の MCP サーバーを簡単にエージェントのツールとして利用可能

# ---

# ## 🔷 サポートされるトランスポート方式

# | トランスポート | 説明 |
# |---|---|
# | **stdio** | コマンドを起動してプロセス間通信 (`command` フィールドで指定) |
# | **SSE** (Server-Sent Events) | HTTP ベースのリモートサーバーと接続 (`url` フィールドで指定) |
# | **Streamable HTTP** | HTTP 経由のストリーミング通信（SSE の発展形） |

# > トランスポート種別は `command` か `url` の有無で**自動検出**されますが、`transport` フィールドで明示的に指定することも可能。

# ---

# ## 🔷 クイックスタート（Python）

# ```python
# from mcp import stdio_client, StdioServerParameters
# from strands import Agent
# from strands.tools.mcp import MCPClient

# # stdio トランスポートで MCP クライアントを作成
# mcp_client = MCPClient(lambda: stdio_client(
#     StdioServerParameters(
#         command="uvx",
#         args=["awslabs.aws-documentation-mcp-server@latest"]
#     )
# ))

# # MCPClient を直接 Agent に渡す（ライフサイクルは自動管理）
# agent = Agent(tools=[mcp_client])
# agent("What is AWS Lambda?")
# ```

# ---

# ## 🔷 複数の MCP サーバーの併用

# 複数の MCP サーバーのツールを1つのエージェントで組み合わせることが可能。

# ```python
# # 管理アプローチ（ライフサイクルを自動管理）
# agent = Agent(tools=[sse_mcp_client, stdio_mcp_client])
# ```

# ---

# ## 🔷 Strands Agents MCP サーバー（開発支援用）

# Strands Agents 自身も **MCP サーバー（`strands-agents-mcp-server`）** を提供しており、AI コーディングアシスタントが Strands のドキュメントにアクセスできるようにします。

# | 機能 | 説明 |
# |---|---|
# | 🔍 インテリジェント検索 | TF-IDF ベースのランキングで関連ドキュメントを検索 |
# | 📂 セクション単位の参照 | トークン効率の高いドキュメント取得 |
# | 📥 オンデマンド取得 | 必要なドキュメントをリアルタイムに取得 |

# **対応クライアント：** Kiro / Claude Code / Cursor / VS Code / Cline など **40以上のアプリケーション**

# **セットアップ例（Claude Code）:**
# ```bash
# claude mcp add strands uvx strands-agents-mcp-server
# ```

# **開発支援でできること：**
# - カスタムツール・エージェントの開発（ガイド付きプロンプト）
# - Strands 実装のデバッグ・トラブルシューティング
# - Strands のコンセプトやパターンに関する質問への回答
# - Graph / Swarm パターンによるマルチエージェントシステムの設計

# ---

# ## 🔷 高度な機能

# | 機能 | 説明 |
# |---|---|
# | **Elicitation** | エージェントから追加情報を能動的に取得 |
# | **Progress Notifications** | 長時間処理の進捗通知 |
# | **Tool Filters** | 許可/拒否リストでロードするツールを制御 |
# | **Tool Prefix** | ツール名にプレフィックスを付与して区別 |

# ---

# ## 🔷 まとめ

# ```
# MCPの位置づけ（Strands Agentsにおけるツール種別）

# 1. カスタム関数ツール
# 2. Vended Tools（組み込みツール）
# 3. ✅ MCP Tools ← 外部サービスと標準規格で連携
# 4. Agents as Tools（エージェント自身をツールとして利用）
# ```

# MCP は「標準化されたツール共有の仕組み」として、複数エージェント・複数アプリケーションをまたいで再利用可能なツールコレクションを作成・共有する際に特に有効です。最新情報を調査するために、両サービスのドキュメントを同時に検索します。
# Tool #1: aws___search_documentation

# Tool #2: aws___search_documentation
# さらに詳細情報を取得します。
# Tool #3: aws___read_documentation

# Tool #4: aws___read_documentation

# Tool #5: aws___read_documentation
# 十分な情報が集まりました。日本語で詳しく整理して回答します。

# ---

# # AgentCore Evaluations と Bedrock Evaluations の違い

# 最新の AWS ドキュメントをもとに、両サービスの違いを詳しく解説します。

# ---

# ## 🔍 一言で言うと

# | | AgentCore Evaluations | Bedrock Evaluations |
# |---|---|---|
# | **目的** | **AIエージェント**のパフォーマンス評価 | **基盤モデル（FM）・RAGシステム**の性能評価 |
# | **位置づけ** | エージェントの品質保証・継続監視 | モデル選定・RAG精度測定 |

# ---

# ## 🎯 1. 評価対象

# ### AgentCore Evaluations
# - AIエージェント（AgentCore Runtime上のものに限らず、**外部ホストのエージェントも対象**）
# - Strands、LangGraph などの人気フレームワークで構築されたエージェント
# - エージェントが使用する**ツール**（ツール選択・パラメータ抽出の精度）

# ### Bedrock Evaluations
# - **基盤モデル（Foundation Models）** の比較・選定
# - **RAGシステム / Knowledge Base** の精度測定
# - Amazon Bedrock Marketplace モデル、カスタム FM、インポートされた FM なども対象

# ---

# ## 🧪 2. 評価の種類

# ### AgentCore Evaluations（3種類）

# | 評価タイプ | 説明 |
# |---|---|
# | **オンライン評価** | 本番トラフィックをリアルタイムで継続的に監視。一部セッションのサンプリングやフィルタリングが可能 |
# | **オンデマンド評価** | 特定のスパン・トレースIDを指定してピンポイントで分析。開発初期のビルドタイム検証にも活用 |
# | **バッチ評価** | 複数セッションをまとめて非同期ジョブで評価。ベースライン測定・回帰テスト・定期監査に最適 |

# ### Bedrock Evaluations（3種類）

# | 評価タイプ | 説明 |
# |---|---|
# | **自動評価（Programmatic）** | 事前定義メトリクス（正確性・堅牢性・毒性）で自動評価。ビルトインデータセットも利用可 |
# | **人間評価（Human Workers）** | 社内の従業員や専門家チームが主観的メトリクス（フレンドリーさ・ブランドボイスなど）を評価 |
# | **LLM-as-a-Judge 評価** | 別のLLMがジャッジモデルとして応答を採点。9つの品質メトリクスと3つのResponsible AIメトリクスに対応 |

# ---

# ## 📊 3. 評価メトリクスの粒度

# ### AgentCore Evaluations：**3階層構造**で評価

# ```
# セッション (Session)
#   └─ トレース (Trace)
#        └─ スパン (Span)
# ```

# | 階層 | 評価内容 |
# |---|---|
# | **セッション** | Goal Success Rate（会話全体でユーザー目標を達成できたか） |
# | **トレース** | Helpfulness, Correctness, Coherence, Conciseness, Faithfulness, Harmfulness, Instruction Following, Response Relevance, Refusal, Stereotyping（11種） |
# | **ツール/スパン** | Tool Selection Accuracy（ツール選択の正確さ）, Tool Parameter Accuracy（パラメータ抽出精度） |

# **ビルトイン評価器：合計13種**

# ### Bedrock Evaluations：**モデル・RAG単位**で評価

# | 対象 | 主なメトリクス |
# |---|---|
# | **モデル評価** | 正確性(Accuracy)・堅牢性(Robustness)・毒性(Toxicity)、または Helpfulness / Faithfulness / Completeness など最大9種 |
# | **RAG評価** | 情報検索精度・応答の正確性（グラウンドトゥルースとの比較） |

# ---

# ## ⚙️ 4. 技術的な特徴

# | 項目 | AgentCore Evaluations | Bedrock Evaluations |
# |---|---|---|
# | **トレース収集** | OpenTelemetry / OpenInference 対応 | 不要（直接モデルを呼び出して評価） |
# | **カスタム評価器** | LLM-as-a-Judge ＋ **Lambda関数（コードベース）** の2種類 | カスタムメトリクス（LLM-as-a-Judge、judge prompts定義） |
# | **人間評価** | ❌ なし | ✅ あり（社内ワーカー / AWS管理チーム） |
# | **結果の確認場所** | **CloudWatch Observability ダッシュボード** | **S3 + Bedrockコンソール** |
# | **リアルタイム監視** | ✅ オンライン評価で継続監視 | ❌ バッチジョブ形式 |
# | **管理ツール** | AgentCore CLI / Python SDK / AWS SDK / コンソール | AWS SDK / コンソール |

# ---

# ## 🏗️ 5. ユースケースの違い

# | シナリオ | 使うべきサービス |
# |---|---|
# | 複数のFMを比較してベストモデルを選びたい | ✅ **Bedrock Evaluations** |
# | RAG（Knowledge Base）の精度を測りたい | ✅ **Bedrock Evaluations** |
# | 本番稼働中のエージェントを継続的に品質監視したい | ✅ **AgentCore Evaluations（オンライン評価）** |
# | 特定のエージェントセッションで問題を調査したい | ✅ **AgentCore Evaluations（オンデマンド評価）** |
# | エージェントのツール呼び出し精度を測りたい | ✅ **AgentCore Evaluations** |
# | LangGraph / Strands製エージェントを評価したい | ✅ **AgentCore Evaluations** |
# | ブランドボイスや主観的品質を人間に評価させたい | ✅ **Bedrock Evaluations** |

# ---

# ## 📝 まとめ

# - **Bedrock Evaluations** は「**どのモデルやRAGが優れているか**」を選定・測定するためのサービス。モデル選定フェーズや Knowledge Base の精度チューニングに特化。
# - **AgentCore Evaluations** は「**エージェントが本番で正しく動作しているか**」を保証するためのサービス。ツール選択・目標達成率など **エージェント固有の評価指標** を持ち、**本番リアルタイム監視** まで対応している点が最大の差別化ポイントです。
