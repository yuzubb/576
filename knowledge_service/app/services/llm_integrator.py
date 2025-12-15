def generate_contextual_answer(user_question: str, knowledge_graph_results: list[dict]) -> str:
    context_data = "\n".join([
        f"情報源: {res['Project.title']}, ライブラリ: {res['Library.name']}, 使用回数: {res['UsageCount']}"
        for res in knowledge_graph_results
    ])

    prompt = f"""
    あなたはユニバーサル・ナレッジ・コパイロットです。以下の知識グラフ検索結果に基づき、ユーザーの質問に正確に回答してください。
    ユーザーの質問: {user_question}
    知識グラフ検索結果:
    {context_data}
    """
    
    # response = LLM_API_CLIENT.generate(prompt, model='ukc-base-v1')
    return f"LLM処理結果: {prompt}"
