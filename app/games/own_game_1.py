import random

# Quiz
class Quiz:
    def __init__(self, question, answer, explanation, difficulty):
        self.question = question
        self.answer = answer
        self.explanation = explanation
        self.difficulty = difficulty

    def get_score(self):
        if self.difficulty == "초급":
            return 1
        elif self.difficulty == "중급":
            return 2
        elif self.difficulty == "고급":
            return 3


# 문제 리스트
quiz_list = [

    # 초급
    Quiz("주식은 원금이 보장된다.", "X",
          "주식은 가격 변동 위험이 있습니다.", "초급"),

    Quiz("ETF는 여러 종목에 분산 투자할 수 있다.", "O",
          "ETF는 다양한 자산에 투자하는 상품입니다.", "초급"),

    Quiz("복리는 이자에 이자가 붙는 구조이다.", "O",
          "복리는 시간이 지날수록 수익이 커질 수 있습니다.", "초급"),

    Quiz("손실률 50% 이후에는 50% 수익만 내면 원금 회복이다.", "X",
          "50% 손실 후에는 100% 수익이 필요합니다.", "초급"),

    Quiz("분산투자는 위험 관리에 도움이 된다.", "O",
          "여러 자산에 나누어 투자하면 위험을 줄일 수 있습니다.", "초급"),

    Quiz("채권 가격과 금리는 보통 반대로 움직인다.", "O",
          "금리가 오르면 기존 채권 가격은 하락하는 경우가 많습니다.", "초급"),

    Quiz("예금은 일반적으로 주식보다 위험성이 낮다.", "O",
          "예금은 상대적으로 안정적인 자산입니다.", "초급"),

    # 중급
    Quiz("수익률 10%와 손실률 10%를 반복하면 원금은 유지된다.", "X",
          "손실과 수익은 기준 금액이 달라 원금이 줄어듭니다.", "중급"),

    Quiz("금리가 상승하면 일반적으로 성장주에 부담이 될 수 있다.", "O",
          "미래 가치 할인 효과 때문에 성장주가 영향을 받을 수 있습니다.", "중급"),

    Quiz("모든 고배당주는 안전한 투자 상품이다.", "X",
          "배당이 높아도 기업 상황이 나쁠 수 있습니다.", "중급"),

    Quiz("현금도 하나의 자산군으로 볼 수 있다.", "O",
          "현금 역시 자산 배분의 한 종류입니다.", "중급"),

    Quiz("채권은 항상 수익이 보장된다.", "X",
          "채권도 발행 기관의 위험이 존재합니다.", "중급"),

    Quiz("장기 투자에서는 복리 효과가 중요하다.", "O",
          "투자 기간이 길수록 복리 효과가 커질 수 있습니다.", "중급"),

    Quiz("한 종목에만 투자하면 분산투자 효과가 극대화된다.", "X",
          "한 종목 투자는 위험 집중입니다.", "중급"),

    # 고급
    Quiz("100만원이 50% 하락 후 원금 회복하려면 100% 수익이 필요하다.", "O",
          "50만원이 된 자산은 두 배가 되어야 원금 회복입니다.", "고급"),

    Quiz("상관관계가 낮은 자산끼리 조합하면 포트폴리오 위험 감소에 도움이 된다.", "O",
          "다른 움직임을 가진 자산을 섞으면 변동성을 줄일 수 있습니다.", "고급"),

    Quiz("복리 수익률은 투자 기간이 길어질수록 선형적으로 증가한다.", "X",
          "복리는 기하급수적으로 증가하는 특징이 있습니다.", "고급"),

    Quiz("채권 금리가 상승하면 기존 채권의 매력도는 일반적으로 상승한다.", "X",
          "기존 낮은 금리 채권의 가격은 하락할 가능성이 큽니다.", "고급"),

    Quiz("자산군이 서로 다르면 항상 손실이 발생하지 않는다.", "X",
          "분산투자는 위험 감소에 도움을 주지만 손실 자체를 막지는 못합니다.", "고급"),

    Quiz("연평균 수익률과 실제 누적 수익률은 다를 수 있다.", "O",
          "변동성과 복리 효과 때문에 차이가 발생할 수 있습니다.", "고급")
]

# 문제 출제
def play_quiz(quiz, score):

    print("\n---------------------------") #구분하기 위해
    print(f"[{quiz.difficulty}] 문제")
    print(quiz.question)

    # ox만 받기
    while True:
        user_answer = input("O / X 입력 : ").upper()

        if user_answer in ["O", "X"]:
            break
        else:
            print(" O 또는 X 중에서만 입력하세요!")

    if user_answer == quiz.answer:
        gained_score = quiz.get_score()
        score += gained_score

        print("\n정답입니다!")
        print(f"{gained_score}점 획득!")
    else:
        print("\n틀렸습니다.")

    print(f"정답 : {quiz.answer}")
    print(f"해설 : {quiz.explanation}")

    print(f"\n현재 점수 : {score}")

    return score
#dd
#  첫번째 게임-ox퀴즈 함수
def game_1():

    # print("투자 전문가가 되고싶으신가요?")
    print("투자 상식 OX 퀴즈 게임")
    print("게임 시작!")

    score = 0

    random.shuffle(quiz_list)

    for quiz in quiz_list:
        score = play_quiz(quiz, score)

    print("\n===================================")
    print("게임 종료!")
    print(f"최종 점수 : {score}")

    if score >= 35:
        print("투자 고수입니다!!!!!")
    elif score >= 25:
        print("투자 중수입니다!!!")
    else:
        print("투자 초보입니다!")
        

# 프로그램 실행
game_1()