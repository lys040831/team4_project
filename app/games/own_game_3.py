GAME_TITLE = "회귀 투자자의 100년 포트폴리오 전쟁"
ASSET_NAMES = ["S&P500", "미국 10년물 국채", "달러 현금", "금"]
INITIAL_MONEY = 100.0
TOTAL_ALLOCATION = 10
LINE_LENGTH = 40
EVENTS = [
    ["대공황 붕괴", "1929~1932", "주식시장이 장기간 크게 하락하고 현금과 국채의 방어력이 부각된 구간입니다.", -64.77, 15.47, 11.53, 0.15, "극단적 주식 하락기에는 현금성과 국채가 손실 완화에 도움을 줄 수 있습니다."],
    ["뉴딜·리플레이션 반등", "1933~1936", "대공황 이후 정책 대응과 경기 회복 기대가 반영되며 위험자산이 크게 반등한 구간입니다.", 186.92, 20.65, 1.59, 68.54, "큰 위기 이후에는 정책 대응과 유동성 변화에 따라 위험자산이 강하게 반등할 수 있습니다."],
    ["오일쇼크·스태그플레이션", "1973~1974", "인플레이션과 경기침체가 동시에 나타났고, 금이 매우 강하게 상승한 구간입니다.", -36.50, 5.72, 15.44, 187.37, "인플레이션 충격 구간에서는 금과 현금성 자산이 상대적으로 유리할 수 있습니다."],
    ["볼커 고금리 전환", "1980~1982", "고금리 정책으로 물가를 잡는 과정에서 자산별 성과가 크게 갈린 구간입니다.", 51.19, 39.40, 41.12, -10.23, "높은 금리 환경에서는 현금성 자산 수익률이 높아질 수 있고, 금은 부진할 수 있습니다."],
    ["1994년 금리상승 충격", "1994", "금리 상승으로 채권 가격이 압박받았던 대표적인 구간입니다.", 1.33, -8.04, 4.37, -2.17, "채권은 방어자산이 될 수 있지만, 금리 상승기에는 기존 채권 가격이 하락할 수 있습니다."],
    ["닷컴버블 붕괴", "2000~2002", "기술주 중심의 과열이 꺼지며 주식시장이 여러 해 동안 하락한 구간입니다.", -37.43, 41.78, 11.49, 19.63, "주식 버블 붕괴 구간에서는 국채와 금이 포트폴리오 방어에 기여할 수 있습니다."],
    ["글로벌 금융위기", "2008", "금융 시스템 불안이 커졌고 주식은 크게 하락했으며 미국 국채가 강하게 상승한 구간입니다.", -36.55, 20.10, 1.40, 4.32, "시스템 위기에서는 유동성과 안전자산 선호가 강해질 수 있습니다."],
    ["코로나 유동성 장세", "2020", "코로나 충격 이후 대규모 유동성 공급이 이어지며 주식과 금이 모두 강세를 보인 구간입니다.", 18.02, 11.33, 0.36, 24.17, "유동성 공급 국면에서는 위험자산과 일부 실물자산이 동시에 강세를 보일 수 있습니다."],
    ["인플레이션·금리인상 쇼크", "2022", "금리 급등으로 주식과 채권이 동시에 하락한 대표적인 구간입니다.", -18.04, -17.83, 2.09, 0.55, "금리 급등기에는 주식과 채권이 동시에 하락할 수 있으며, 현금의 방어력이 커질 수 있습니다."],
    ["최신 완성연도 랠리", "2025", "주식이 상승했고 금이 매우 강한 성과를 보인 최신 완성연도 구간입니다.", 17.78, 7.80, 4.21, 66.22, "같은 상승장이라도 자산별 성과는 크게 달라질 수 있으며, 금이 주식보다 강할 때도 있습니다."],
]
def round_number(number):
    if number >= 0: return int(number + 0.5)
    return int(number - 0.5)
class OwnGame3:
    def __init__(self):
        self.money = INITIAL_MONEY
        self.initial_money = INITIAL_MONEY
        self.peak_money = INITIAL_MONEY
        self.max_drawdown = 0.0
        self.round_count = 0
        self.is_quit = False
    def ask_number(self, asset_name):
        user_input = input(asset_name + " 배분: ").strip()
        if user_input.startswith("-") and user_input[1:].isdigit():
            return -int(user_input[1:])
        if not user_input.isdigit():
            return None
        return int(user_input)
    def ask_allocation(self):
        while True:
            allocation = []
            total = 0
            print()
            print("총 10칸을 네 자산에 배분하세요. 올인도 가능합니다.")
            for asset_name in ASSET_NAMES:
                asset_count = self.ask_number(asset_name)
                if asset_count is None:
                    print("숫자만 입력해 주세요.")
                    allocation = []
                    break
                if asset_count < 0 or asset_count > 10:
                    print("0부터 10 사이 정수만 입력해 주세요.")
                    allocation = []
                    break
                allocation.append(asset_count)
                total = total + asset_count
            if len(allocation) != 4:
                continue
            if total != TOTAL_ALLOCATION:
                print("배분 합계는 10이어야 합니다. 현재 합계:", total)
                continue
            return allocation
    def get_portfolio_return(self, allocation, returns):
        result = 0.0
        for i in range(len(ASSET_NAMES)):
            result = result + (allocation[i] / TOTAL_ALLOCATION * returns[i])
        return result
    def update_money(self, portfolio_return):
        before_money = self.money
        self.money = self.money * (1 + portfolio_return / 100)
        if self.money > self.peak_money:
            self.peak_money = self.money
        if self.money < self.peak_money:
            drawdown = self.peak_money - self.money
            if drawdown > self.max_drawdown:
                self.max_drawdown = drawdown
        return before_money
    def get_best_and_worst(self, returns):
        best_index = 0
        worst_index = 0
        for i in range(len(returns)):
            if returns[i] > returns[best_index]:
                best_index = i
            if returns[i] < returns[worst_index]:
                worst_index = i
        return [best_index, worst_index]
    def show_round_result(self, event, allocation, returns, portfolio_return, before_money):
        best_and_worst = self.get_best_and_worst(returns)
        print()
        print("-" * LINE_LENGTH)
        print("[라운드 결과]", event[0])
        print("-" * LINE_LENGTH)
        for i in range(len(ASSET_NAMES)):
            print(ASSET_NAMES[i] + ":", str(allocation[i]) + "칸,", str(round_number(returns[i])) + "%")
        print("포트폴리오 수익률:", str(round_number(portfolio_return)) + "%")
        print("라운드 전 자본:", str(round_number(before_money)) + "억")
        print("라운드 후 자본:", str(round_number(self.money)) + "억")
        print("좋았던 자산:", ASSET_NAMES[best_and_worst[0]])
        print("주의할 자산:", ASSET_NAMES[best_and_worst[1]])
        print("[해설]")
        print(event[7])
    def get_grade(self):
        if self.money >= 250: return "S급 - 시대를 읽은 자본가"
        if self.money >= 180: return "A급 - 위기를 기회로 만든 투자자"
        if self.money >= 130: return "B급 - 생존형 운용자"
        if self.money >= 100: return "C급 - 원금 방어 성공"
        return "D급 - 다음 회귀 준비"
    def get_score(self):
        if self.is_quit: return 0
        return round_number(self.money)
    def get_total_return(self):
        return round_number((self.money - self.initial_money) / self.initial_money * 100)
    def show_final_result(self):
        print()
        print("=" * LINE_LENGTH)
        print("최종 결과")
        print("=" * LINE_LENGTH)
        print("최종 자본:", str(round_number(self.money)) + "억")
        print("총 수익률:", str(self.get_total_return()) + "%")
        print("최고 자본:", str(round_number(self.peak_money)) + "억")
        print("최대 낙폭:", str(round_number(self.max_drawdown)) + "억")
        print("등급:", self.get_grade())
        print("반환 점수:", str(self.get_score()) + "점")
    def play(self):
        print()
        print("=" * LINE_LENGTH)
        print(GAME_TITLE)
        print("=" * LINE_LENGTH)
        print("이 게임은 교육용 역사 수익률 기반 시뮬레이션입니다.")
        input("Enter를 누르면 시작합니다...")
        for event in EVENTS:
            self.round_count = self.round_count + 1
            print()
            print("=" * LINE_LENGTH)
            print("[" + str(self.round_count) + "라운드] " + event[0] + " (" + event[1] + ")")
            print("=" * LINE_LENGTH)
            print(event[2])
            print("현재 자본:", str(round_number(self.money)) + "억")
            allocation = self.ask_allocation()
            returns = [event[3], event[4], event[5], event[6]]
            portfolio_return = self.get_portfolio_return(allocation, returns)
            before_money = self.update_money(portfolio_return)
            self.show_round_result(event, allocation, returns, portfolio_return, before_money)
            if self.round_count < len(EVENTS):
                if input("다음 라운드는 Enter, 중간 종료는 q: ").strip().lower() == "q":
                    self.is_quit = True
                    print("중간 종료를 선택했습니다.")
                    break
        self.show_final_result()
        return [GAME_TITLE, self.get_score(), self.get_total_return()]

def play():
    return OwnGame3().play()[1]
