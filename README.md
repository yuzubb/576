576/<br>
├── .github/<br>
│   └── workflows/<br>
│       └── main.yml        # GitHub ActionsによるCI/CD定義（テストとデプロイの自動化）<br>
├── docker-compose.yml      # 全てのサービス（DB, Kafka, Zookeeper）をローカル開発用に定義<br>
├── render.yaml             # Render上でのサービス、データベース、環境変数などのIaC定義<br>
├── frontend/               # フロントエンドサービス (Next.js/Reactを想定)<br>
│   ├── public/<br>
│   ├── src/<br>
│   │   ├── components/<br>
│   │   └── pages/<br>
│   ├── package.json<br>
│   └── ...<br>
│<br>
├── knowledge_service/      # 知識グラフ検索とLLM統合サービス (Python/FastAPI)<br>
│   ├── app/<br>
│   │   ├── db/<br>
│   │   │   └── neo4j_queries.py  # (I-A) 知識グラフ検索クエリ<br>
│   │   ├── services/<br>
│   │   │   ├── kg_processor.py   # (I-B) クエリ実行ロジック<br>
│   │   │   └── llm_integrator.py # (I-C) LLMへのプロンプト統合<br>
│   │   └── main.py             # FastAPIのメインルーティング<br>
│   ├── Dockerfile              # サービス専用のDockerイメージ定義<br>
│   └── requirements.txt        # Python依存関係<br>
│<br>
├── task_router/            # API Gatewayとタスクルーティングサービス (Python/FastAPI)<br>
│   ├── app/<br>
│   │   └── main.py             # APIエンドポイントと意図解析/ルーティングロジック<br>
│   ├── event_producer.py       # (II) Kafkaへのイベント投入ロジック<br>
│   └── requirements.txt<br>
│<br>
└── task_agent_flight/      # 並行処理を行うタスク実行エージェント (Go)<br>
    ├── cmd/<br>
    │   └── main.go             # Goアプリケーションのエントリーポイント<br>
    ├── pkg/<br>
    │   └── agent/<br>
    │       └── executor.go     # (III) 並行フライト検索ロジック<br>
    ├── go.mod<br>
    └── Dockerfile<br>
<br>
