from app.own_menu_manager import OwnMenuManager
from app.own_record_manager import OwnRecordManager
from app.games.own_game_1 import OwnGame1
from app.games.own_game_2 import OwnGame2
from app.games.own_game_3 import OwnGame3


class OwnApp:
    def __init__(self):
        self.menu_manager = OwnMenuManager()
        self.record_manager = OwnRecordManager()
        self.player_name = ""

    def start(self):
        print("===== 디지털 투자 안전 훈련소 =====")
        self.player_name = input("닉네임을 입력하세요: ")
        if self.player_name == "":
            self.player_name = "사용자"
        print(self.player_name + "님, 환영합니다.")

    def run(self):
        self.start()
        while True:
            self.menu_manager.show_main_menu()
            menu = self.menu_manager.input_menu()
            if menu == "1":
                game = OwnGame1()
                result = game.play()
                self.record_manager.add_record(self.player_name, result)
            elif menu == "2":
                game = OwnGame2()
                result = game.play()
                self.record_manager.add_record(self.player_name, result)
            elif menu == "3":
                game = OwnGame3()
                result = game.play()
                self.record_manager.add_record(self.player_name, result)
            elif menu == "4":
                self.record_manager.show_records()
            elif menu == "5":
                print("프로그램을 종료합니다.")
                break
            else:
                print("잘못된 입력입니다. 다시 선택해주세요.")
