import random
print("START")

scam_events = [
    "하루 30% 확정 수익 코인",
    "VIP 리딩방 추천 종목",
    "AI 자동 수익 프로그램",
    "비공개 세력 투자 정보",
    "단 3일 만에 원금 5배",
    "100% 성공하는 주식 알고리즘",
    "손실 없는 안전 투자",
    "상위 1%만 아는 비밀 종목",
    "해외 부자들만 투자하는 코인",
    "지금 사면 무조건 오르는 주식",
    "원금 보장 해외 선물 투자",
    "자동 매매 프로그램 무료 체험",
    "한 달 안에 부자 되는 투자법",
    "유명 투자자가 추천한 비밀 종목"
]

normal_events = [
    "삼성전자 투자",
    "우량주 장기 투자",
    "클라우드 기업 투자",
    "반도체 ETF 투자", 
    "소비재 기업 장기 투자",
    "대형 플랫폼 기업 투자",
    "안정 성장형 펀드", 
    "글로벌 우량 기업 투자", 
    "금융 ETF 투자", 
    "장기 가치 투자 종목",  
    "배당 성장주 투자", 
    "친환경 자동차 기업 투자", 
    "국내 대기업 주식 투자", 
    "안정 자산 포트폴리오", 
    "인공지능 산업 투자"
]

def game_start():

    money = 100
    score = 0

    for round in range(1, 11):

        print(f"\n[{round}번째 게임]")

        event_type = random.choice(["normal", "scam"])

        if event_type == "normal":
            event = random.choice(normal_events)
        else:
            event = random.choice(scam_events)

        print(f"투자 : {event}")

        print("1. 투자\n2. 거절\n3. 신고")
        option = int(input("선택하세요: "))

        # 1. 투자
        if option == 1:

            if event_type == "normal":
                gain = random.randint(10, 30)
                money += gain
                score += 10
                print(f"투자 성공 +{gain}만원 +10점")

            else:
                loss = random.randint(20, 50)
                money -= loss
                score -= 20
                print(f"사기 투자 -{loss}만원 -20점")

        # 2. 거절
        elif option == 2:

            if event_type == "scam":
                score += 10
                print("사기 피함 +10점")
            else:
                print("기회 놓침")

        # 3. 신고
        elif option == 3:

            if event_type == "scam":
                score += 15
                print("신고 성공 +15점")
            else:
                score -= 5
                print("오신고 -5점")

        else:
            print("잘못 입력")

        print(f"현재 자산: {money}만원")
        print(f"현재 점수: {score}점")

        if money <= 0:
            print("파산!")
            break

    # 최종 결과
    print("\n===== 최종 결과 =====")
    print(f"최종 자산: {money}")
    print(f"최종 점수: {score}")

game_start()


        
123