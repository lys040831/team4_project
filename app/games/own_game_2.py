import random


SCAM_EVENTS = [
    "하루 30% 확정 수익 코인",
    "VIP 리딩방 추천 종목",
    "AI 자동 수익 프로그램",
    "비공개 세력 투자 정보",
    "단 3일 만에 원금 5배",
    "100% 성공하는 주식 알고리즘",
    "손실 없는 안전 투자",
    "지금 사면 무조건 오르는 주식",
    "원금 보장 해외 선물 투자",
    "한 달 안에 부자 되는 투자법",
]

NORMAL_EVENTS = [
    "삼성전자 투자",
    "우량주 장기 투자",
    "클라우드 기업 투자",
    "반도체 ETF 투자",
    "소비재 기업 장기 투자",
    "대형 플랫폼 기업 투자",
    "안정 성장형 펀드",
    "글로벌 우량 기업 투자",
    "배당 성장주 투자",
    "안정 자산 포트폴리오",
]


class OwnGame2:
    def ask_option(self):
        while True:
            print("1. 투자")
            print("2. 거절")
            print("3. 신고")
            option = input("선택하세요: ")
            if option == "1" or option == "2" or option == "3":
                return option
            print("1, 2, 3 중에서 입력하세요.")

    def get_result_text(self, money, score):
        if money <= 0:
            return "파산했습니다. 위험한 투자를 조심해야 합니다."
        if score >= 80:
            return "사기 투자를 잘 피했습니다."
        if score >= 40:
            return "위험 신호를 어느 정도 구분했습니다."
        return "사기 투자 문구를 더 조심해야 합니다."

    def play(self):
        print()
        print("===== 투자 사기 탐지 시뮬레이션 =====")
        money = 100
        score = 0
        for round_count in range(1, 11):
            print()
            print("[" + str(round_count) + "번째 게임]")
            event_type = random.choice(["normal", "scam"])
            if event_type == "normal":
                event = random.choice(NORMAL_EVENTS)
            else:
                event = random.choice(SCAM_EVENTS)
            print("투자:", event)
            option = self.ask_option()
            if option == "1" and event_type == "normal":
                gain = random.randint(10, 30)
                money = money + gain
                score = score + 10
                print("투자 성공 +" + str(gain) + "만원 +10점")
            elif option == "1" and event_type == "scam":
                loss = random.randint(20, 50)
                money = money - loss
                score = score - 20
                print("사기 투자 -" + str(loss) + "만원 -20점")
            elif option == "2" and event_type == "scam":
                score = score + 10
                print("사기 피함 +10점")
            elif option == "2":
                print("기회 놓침")
            elif option == "3" and event_type == "scam":
                score = score + 15
                print("신고 성공 +15점")
            else:
                score = score - 5
                print("오신고 -5점")
            print("현재 자산:", str(money) + "만원")
            print("현재 점수:", str(score) + "점")
            if money <= 0:
                print("파산!")
                break
        result_text = self.get_result_text(money, score)
        print()
        print("===== 최종 결과 =====")
        print("최종 자산:", str(money) + "만원")
        print("최종 점수:", str(score) + "점")
        print(result_text)
        return ["투자 사기 탐지 시뮬레이션", score, result_text]
