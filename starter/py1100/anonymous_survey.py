class AnonymousSurvey:
    """アンケート収集用クラス"""

    def __init__(self, question: str) -> None:
        """初期化"""

        self.question = question
        self.responses = []

    def show_question(self) -> None:
        """アンケートの質問を表示する"""

        print(self.question)

    def store_response(self, new_response: str) -> None:
        """アンケートの答えを保存する"""

        self.responses.append(new_response)

    def show_results(self) -> None:
        """すべての調査結果を表示する"""

        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")