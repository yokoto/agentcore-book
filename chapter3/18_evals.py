from strands import Agent
from strands_evals import Case, Experiment
from strands_evals.evaluators import OutputEvaluator

# 各テストケースの入力をエージェントに渡して回答を取得する関数
def get_response(case: Case) -> str:
    agent = Agent(callback_handler=None)
    return str(agent(case.input))

# テストケースを定義
test_cases = [
    Case[str, str](
        name="knowledge-test",
        input="フランスの首都はどこですか？",
        expected_output="パリ",
    ),
]

# 評価基準を指定
evaluator = OutputEvaluator(
    rubric="正確性と完全性を評価してください。",
)

# テストケースと評価器を組み合わせて実行
experiment = Experiment[str, str](
    cases=test_cases, evaluators=[evaluator]
)
reports = experiment.run_evaluations(get_response)
print(reports[0].to_dict())
