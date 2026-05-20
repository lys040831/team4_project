from app.games import choice_check
from app.games import config


def show_data_source():
    print("[데이터 출처]")
    print("뉴욕대학교 스턴 경영대학 애스워스 다모다란 교수 자료를 참고했습니다.")
    print("사용 범위:", config.DATA_YEAR_RANGE, "연간 수익률")


def show_intro():
    print()
    print("=" * config.LINE_LENGTH)
    print(config.GAME_TITLE)
    print("=" * config.LINE_LENGTH)
    print("당신은 투자 기초와 사기 투자 피하기를 배운 뒤,")
    print("갑자기 과거 금융시장으로 회귀한 투자자입니다.")
    print("지난 100년의 대표 금융 국면 10개를 지나며")
    print("네 가지 자산에 자본을 배분해 복리로 운용합니다.")
    print()
    print("이 게임은 교육용 역사 수익률 기반 시뮬레이션입니다.")
    print("실제 투자 추천이 아니며, 정밀한 금융 모델도 아닙니다.")
    print("화면에 보이는 자본과 수익률은 정수로 표시합니다.")
    print()
    show_data_source()
    print()
    input("Enter를 누르면 회귀 투자를 시작합니다...")


def show_status(game):
    print()
    print("[현재 상태]")
    print("현재 자본:", str(config.round_number(game.money)) + "억")
    print("최고 자본:", str(config.round_number(game.peak_money)) + "억")
    print("최대 낙폭:", str(config.round_number(game.max_drawdown)) + "억")


def show_round_start(round_count, event):
    print()
    print("=" * config.LINE_LENGTH)
    print("[" + str(round_count) + "라운드] " + event["title"] + " (" + event["period"] + ")")
    print("=" * config.LINE_LENGTH)
    print(event["description"])


def show_allocation(allocation):
    print("[나의 배분]")
    for asset_name in config.ASSET_NAMES:
        print(asset_name + ":", str(allocation[asset_name]) + "칸")


def show_asset_returns(returns):
    print("[각 자산의 역사 수익률]")
    for asset_name in config.ASSET_NAMES:
        print(asset_name + ":", str(config.round_number(returns[asset_name])) + "%")


def show_choice_analysis(allocation, returns):
    analysis = choice_check.analyze_choice(allocation, returns)
    print("[선택 분석]")
    print("좋았던 자산:", analysis["best_asset"], str(config.round_number(analysis["best_return"])) + "%")
    print("내 배분:", str(analysis["best_count"]) + "칸")
    print("주의할 자산:", analysis["worst_asset"], str(config.round_number(analysis["worst_return"])) + "%")
    print("내 배분:", str(analysis["worst_count"]) + "칸")
    print(analysis["message"])


def show_round_result(event, allocation, portfolio_return, before_money, after_money):
    print()
    print("-" * config.LINE_LENGTH)
    print("[라운드 결과]", event["title"])
    print("-" * config.LINE_LENGTH)
    show_allocation(allocation)
    print()
    show_asset_returns(event["returns"])
    print()
    if portfolio_return > 0:
        result_message = "자본 증가"
    elif portfolio_return < 0:
        result_message = "자본 감소"
    else:
        result_message = "자본 유지"
    print("포트폴리오 수익률:", str(config.round_number(portfolio_return)) + "%", "-", result_message)
    print("라운드 전 자본:", str(config.round_number(before_money)) + "억")
    print("라운드 후 자본:", str(config.round_number(after_money)) + "억")
    print()
    show_choice_analysis(allocation, event["returns"])
    print()
    print("[해설]")
    print(event["lesson"])


def show_final_result(game):
    total_return = game.get_total_return()
    final_score = game.get_score()
    print()
    print("=" * config.LINE_LENGTH)
    print("최종 결과")
    print("=" * config.LINE_LENGTH)
    print("최종 자본:", str(config.round_number(game.money)) + "억")
    print("총 수익률:", str(config.round_number(total_return)) + "%")
    print("최고 자본:", str(config.round_number(game.peak_money)) + "억")
    print("최대 낙폭:", str(config.round_number(game.max_drawdown)) + "억")
    print("등급:", game.get_grade())
    if game.is_quit:
        print("중간 종료:", "랭킹 점수는 0점으로 처리됩니다.")
    print("반환 점수:", str(final_score) + "점")
    print("=" * config.LINE_LENGTH)


def show_stop_message():
    print()
    print("중간 종료를 선택했습니다. 현재까지의 결과를 보여드립니다.")
