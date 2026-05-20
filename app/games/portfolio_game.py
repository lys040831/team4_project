from app.games import config
from app.games import game_input
from app.games import game_screen


class PortfolioGame:
    def __init__(self):
        self.money = config.INITIAL_MONEY
        self.initial_money = config.INITIAL_MONEY
        self.peak_money = config.INITIAL_MONEY
        self.max_drawdown = 0.0
        self.round_count = 0
        self.is_quit = False

    def show_intro(self):
        game_screen.show_intro()

    def show_status(self):
        game_screen.show_status(self)

    def ask_allocation(self):
        return game_input.ask_allocation()

    def calculate_portfolio_return(self, allocation, returns):
        portfolio_return = 0.0
        for asset_name in config.ASSET_NAMES:
            weight = allocation[asset_name] / config.TOTAL_ALLOCATION
            portfolio_return = portfolio_return + (weight * returns[asset_name])
        return portfolio_return

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

    def show_round_result(self, event, allocation, portfolio_return, before_money):
        game_screen.show_round_result(event, allocation, portfolio_return, before_money, self.money)

    def get_grade(self):
        if self.money >= 250:
            return "S급 - 시대를 읽은 자본가"
        if self.money >= 180:
            return "A급 - 위기를 기회로 만든 투자자"
        if self.money >= 130:
            return "B급 - 생존형 운용자"
        if self.money >= 100:
            return "C급 - 원금 방어 성공"
        return "D급 - 다음 회귀 준비"

    def get_total_return(self):
        return ((self.money - self.initial_money) / self.initial_money) * 100

    def get_score(self):
        if self.is_quit:
            return 0
        return config.round_number(self.money)

    def show_final_result(self):
        game_screen.show_final_result(self)

    def show_round_start(self, event):
        game_screen.show_round_start(self.round_count, event)

    def play_one_round(self, event):
        self.round_count = self.round_count + 1
        self.show_round_start(event)
        self.show_status()
        allocation = self.ask_allocation()
        portfolio_return = self.calculate_portfolio_return(allocation, event["returns"])
        before_money = self.update_money(portfolio_return)
        self.show_round_result(event, allocation, portfolio_return, before_money)

    def ask_continue(self):
        return game_input.ask_continue()

    def wait_next_round(self):
        if self.round_count < len(config.EVENTS):
            return self.ask_continue()
        input("Enter를 누르면 최종 결과를 확인합니다...")
        return True

    def play(self):
        self.show_intro()
        for event in config.EVENTS:
            self.play_one_round(event)
            keep_playing = self.wait_next_round()
            if not keep_playing:
                self.is_quit = True
                game_screen.show_stop_message()
                break
        self.show_final_result()
        return self.get_score()


def play():
    game = PortfolioGame()
    return game.play()
