from strands import Agent

# https://strandsagents.com/docs/user-guide/concepts/agents/prompts/#system-prompts
# system_prompt: モデルの役割・能力・制約についての高レベルの指示. 会話全体を通じてモデルの振る舞いを方向付けるもの.
agent = Agent(
    system_prompt="あなたはリサーチエージェントです。ツールを活用して情報を収集し回答します。回答はMarkdown形式で出力します。",
)

# https://strandsagents.com/docs/user-guide/concepts/agents/prompts/#text-prompt
# テキストプロンプト: モデルに対して行う指示・質問.
result = agent("Bedrockについて情報収集をしてください。")

with open("image.jpg", mode="rb") as f:
    image_bytes = f.read()

# https://strandsagents.com/docs/user-guide/concepts/agents/prompts/#multi-modal-prompting
# マルチモーダルプロンプト: 画像や音声などの非テキストデータを含むプロンプト.
result = agent(
    [
        {
            "image": {"format": "jpeg", "source": {"bytes": image_bytes}},
        },
        {"text": "画像に写っている動物を特定してください"},
    ]
)

# $ uv run 05_prompt.py
# # Amazon Bedrock 情報収集

# 情報収集を開始します。

# ---

# ## 🔍 Amazon Bedrock とは

# ### 概要

# **Amazon Bedrock** は、AWS（Amazon Web Services）が提供する**フルマネージド型の生成AIサービス**です。様々な基盤モデル（Foundation Models / FM）をAPIを通じて利用できるプラットフォームです。

# ---

# ## 🏗️ 主な特徴

# ### 1. マルチモデル対応
# 複数のAIプロバイダーの基盤モデルを単一のAPIで利用可能：

# | プロバイダー | モデル例 |
# |---|---|
# | **Anthropic** | Claude 3.5 Sonnet, Claude 3 Opus, Claude 3 Haiku |
# | **Amazon** | Amazon Titan Text, Titan Embeddings, Nova シリーズ |
# | **Meta** | Llama 3.1, Llama 3.2 |
# | **Mistral AI** | Mistral Large, Mistral Small |
# | **Cohere** | Command R+, Embed |
# | **Stability AI** | Stable Diffusion |
# | **AI21 Labs** | Jamba |

# ---

# ### 2. 主要機能

# #### 📌 テキスト生成・対話
# - チャットボット、コンテンツ生成、要約、翻訳

# #### 📌 RAG（Retrieval-Augmented Generation）
# - **Knowledge Bases for Amazon Bedrock**
# - 企業の独自データと基盤モデルを組み合わせた回答生成

# #### 📌 Agents for Amazon Bedrock
# - タスクの自動化・複数ステップのワークフロー実行
# - 外部APIやデータベースとの連携

# #### 📌 Fine-tuning（カスタマイズ）
# - 独自データでモデルをファインチューニング
# - **Continued Pre-training** によるドメイン特化

# #### 📌 画像生成
# - Stable Diffusion, Amazon Titan Image Generator

# #### 📌 Embeddings
# - テキストのベクトル化（検索・類似度計算に活用）

# ---

# ## 🔒 セキュリティ・プライバシー

# | 項目 | 内容 |
# |---|---|
# | **データ分離** | ユーザーデータはモデルトレーニングに使用されない |
# | **暗号化** | 通信・保存時ともに暗号化対応 |
# | **VPCサポート** | プライベートネットワーク経由でのアクセス可能 |
# | **IAM連携** | AWS IAMによるきめ細かいアクセス制御 |
# | **コンプライアンス** | HIPAA, SOC, ISO 等の各種認証対応 |

# ---

# ## 💰 料金体系

# ### 主な課金モデル

# 1. **オンデマンド**（従量課金）
#    - 入力トークン数 / 出力トークン数で課金
#    - 例：Claude 3.5 Sonnet → 入力 $3/1M tokens、出力 $15/1M tokens

# 2. **プロビジョンドスループット**
#    - 一定のスループットを予約購入
#    - 大量利用時にコスト最適化

# 3. **バッチ推論**
#    - 大量データをまとめて処理（割引あり）

# ---

# ## 🚀 最新動向（2024〜2025年）

# ### Amazon Nova シリーズ（2024年11月発表）
# AWSが独自開発した新世代モデル：

# | モデル | 用途 |
# |---|---|
# | **Nova Micro** | テキスト特化・超高速・低コスト |
# | **Nova Lite** | マルチモーダル・低コスト |
# | **Nova Pro** | 高性能マルチモーダル |
# | **Nova Canvas** | 画像生成 |
# | **Nova Reel** | 動画生成 |

# ### Bedrock Marketplace（2024年）
# - サードパーティモデルの追加対応
# - より多様なモデル選択肢

# ### Amazon Bedrock Flows
# - ノーコード/ローコードでAIワークフローを構築

# ### Guardrails for Amazon Bedrock
# - コンテンツフィルタリング
# - 有害コンテンツ・プロンプトインジェクション対策

# ---

# ## 🛠️ 主なユースケース

# ```
# 📊 エンタープライズ向け
# ├── カスタマーサポートの自動化
# ├── 社内ドキュメント検索・QAシステム
# ├── コード生成・レビュー支援
# ├── レポート・文書の自動生成
# └── データ分析・インサイト抽出

# 🎨 クリエイティブ向け
# ├── 画像・動画生成
# ├── マーケティングコンテンツ作成
# └── 多言語コンテンツ翻訳

# 🏥 業界特化
# ├── 医療：診療記録の要約
# ├── 金融：リスク分析・レポート生成
# └── 製造：異常検知・マニュアル生成
# ```

# ---

# ## 📡 他サービスとの連携

# ```
# Amazon Bedrock
# ├── Amazon S3          → データストレージ
# ├── AWS Lambda         → サーバーレス処理
# ├── Amazon OpenSearch  → ベクトル検索
# ├── Amazon RDS/Aurora  → データベース連携
# ├── AWS Step Functions → ワークフロー管理
# ├── Amazon SageMaker   → MLパイプライン
# └── AWS CloudWatch     → モニタリング・ログ
# ```

# ---

# ## 📍 利用可能リージョン（主要）

# - 🇺🇸 米国東部（バージニア北部）
# - 🇺🇸 米国西部（オレゴン）
# - 🇪🇺 欧州（アイルランド、フランクフルト）
# - 🇯🇵 **アジアパシフィック（東京）** ✅
# - 🇸🇬 アジアパシフィック（シンガポール）
# - など

# ---

# ## ✅ まとめ

# | 項目 | 内容 |
# |---|---|
# | **サービス分類** | フルマネージド生成AI基盤プラットフォーム |
# | **提供開始** | 2023年9月（GA） |
# | **特徴** | マルチモデル・セキュア・AWS統合 |
# | **対象** | 企業向け（エンタープライズグレード） |
# | **東京リージョン** | 対応済み ✅ |

# ---

# > 📌 **公式情報**: https://aws.amazon.com/jp/bedrock/
# >
# > Amazon Bedrockは急速に進化しているサービスのため、最新情報はAWS公式ドキュメントを参照することをお勧めします。# 画像の動物特定

# ## 🐦 特定結果：**キンバト（スポテッドダブ）/ Spotted Dove**
# **学名：*Spilopelia chinensis***

# ---

# ## 📋 特徴の一致点

# | 特徴 | 画像の観察内容 |
# |---|---|
# | **体色** | 灰褐色〜ピンクがかった羽毛 ✅ |
# | **首の模様** | 黒と白の斑点模様（チェッカー柄） ✅ |
# | **体サイズ** | 中型のハト（約30cm程度） ✅ |
# | **足の色** | ピンク〜赤みがかった足 ✅ |
# | **尾羽** | 黒と白のコントラストのある尾羽 ✅ |

# ---

# ## 🌏 生息地・生態

# - **分布**：東南アジア・南アジア原産
#   - インド、中国南部、東南アジア全域
#   - **バリ島（インドネシア）** などの熱帯地域に多い
# - **生息環境**：人間の生活圏に近い場所（庭園、リゾート、公園など）
# - **習性**：人慣れしており、飲食店やリゾートホテルに近づくことが多い

# ---

# ## 📍 撮影場所の推察

# 背景のトロピカルな植生・池・バリ風の東屋（パビリオン）から、**バリ島（インドネシア）のリゾートホテルやレストラン**での撮影と思われます。

# ---

# > 🔍 **結論**：この鳥は **シマキジバト（スポテッドダブ）** で、東南アジアのリゾート地でよく見られる人慣れした野鳥です。%
