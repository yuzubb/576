576/
├── .github/
│   └── workflows/
│       └── main.yml        # GitHub ActionsによるCI/CD定義（テストとデプロイの自動化）
├── docker-compose.yml      # 全てのサービス（DB, Kafka, Zookeeper）をローカル開発用に定義
├── render.yaml             # Render上でのサービス、データベース、環境変数などのIaC定義
├── frontend/               # フロントエンドサービス (Next.js/Reactを想定)
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   └── pages/
│   ├── package.json
│   └── ...
│
├── knowledge_service/      # 知識グラフ検索とLLM統合サービス (Python/FastAPI)
│   ├── app/
│   │   ├── db/
│   │   │   └── neo4j_queries.py  # (I-A) 知識グラフ検索クエリ
│   │   ├── services/
│   │   │   ├── kg_processor.py   # (I-B) クエリ実行ロジック
│   │   │   └── llm_integrator.py # (I-C) LLMへのプロンプト統合
│   │   └── main.py             # FastAPIのメインルーティング
│   ├── Dockerfile              # サービス専用のDockerイメージ定義
│   └── requirements.txt        # Python依存関係
│
├── task_router/            # API Gatewayとタスクルーティングサービス (Python/FastAPI)
│   ├── app/
│   │   └── main.py             # APIエンドポイントと意図解析/ルーティングロジック
│   ├── event_producer.py       # (II) Kafkaへのイベント投入ロジック
│   └── requirements.txt
│
└── task_agent_flight/      # 並行処理を行うタスク実行エージェント (Go)
    ├── cmd/
    │   └── main.go             # Goアプリケーションのエントリーポイント
    ├── pkg/
    │   └── agent/
    │       └── executor.go     # (III) 並行フライト検索ロジック
    ├── go.mod
    └── Dockerfile
