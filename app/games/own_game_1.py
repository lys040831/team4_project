import random


class Quiz:
    def __init__(self, question, answer, explanation, score):
        self.question = question
        self.answer = answer
        self.explanation = explanation
        self.score = score


QUIZ_LIST = [
    Quiz("주식은 원금이 보장된다.", "X", "주식은 가격 변동 위험이 있습니다.", 1),
    Quiz("ETF는 여러 종목에 분산 투자할 수 있다.", "O", "ETF는 여러 자산에 나누어 투자할 수 있습니다.", 1),
    Quiz("복리는 이자에 이자가 붙는 구조이다.", "O", "복리는 시간이 지날수록 효과가 커질 수 있습니다.", 1),
    Quiz("분산투자는 위험 관리에 도움이 된다.", "O", "여러 자산에 나누면 위험을 줄일 수 있습니다.", 1),
    Quiz("채권 가격과 금리는 보통 반대로 움직인다.", "O", "금리가 오르면 기존 채권 가격은 하락할 수 있습니다.", 2),
    Quiz("모든 고배당주는 안전한 투자 상품이다.", "X", "배당이 높아도 기업 상황이 나쁠 수 있습니다.", 2),
    Quiz("장기 투자에서는 복리 효과가 중요하다.", "O", "기간이 길수록 복리 효과가 커질 수 있습니다.", 2),
    Quiz("한 종목에만 투자하면 분산투자 효과가 커진다.", "X", "한 종목 투자는 위험이 집중됩니다.", 2),
    Quiz("50% 손실 후 원금 회복에는 100% 수익이 필요하다.", "O", "절반이 된 자산은 두 배가 되어야 합니다.", 3),
    Quiz("연평균 수익률과 실제 누적 수익률은 다를 수 있다.", "O", "변동성과 복리 때문에 차이가 날 수 있습니다.", 3),
]


class OwnGame1:
    def ask_answer(self):
        while True:
            user_answer = input("O / X 입력: ").upper()
            if user_answer == "O" or user_answer == "X":
                return user_answer
            print("O 또는 X만 입력하세요.")

    def play(self):
        print()
        print("===== 투자 기초 상식 퀴즈 =====")
        score = 0
        random.shuffle(QUIZ_LIST)
        for quiz in QUIZ_LIST:
            print()
            print(quiz.question)
            user_answer = self.ask_answer()
            if user_answer == quiz.answer:
                score = score + quiz.score
                print("정답입니다. +" + str(quiz.score) + "점")
            else:
                print("틀렸습니다.")
            print("정답:", quiz.answer)
            print("해설:", quiz.explanation)
        if score >= 15:
            result_text = "투자 기초가 탄탄합니다."
        elif score >= 8:
            result_text = "기본 개념을 어느 정도 이해했습니다."
        else:
            result_text = "기초 개념을 더 복습하면 좋습니다."
        print()
        print("최종 점수:", str(score) + "점")
        print(result_text)
        return ["투자 기초 상식 퀴즈", score, result_text]
