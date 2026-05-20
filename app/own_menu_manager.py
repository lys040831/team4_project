class OwnMenuManager:
    def show_main_menu(self):
        print()
        print("===== 메인 메뉴 =====")
        print("1. 투자 기초 상식 퀴즈")
        print("2. 투자 사기 탐지 시뮬레이션")
        print("3. 회귀 투자자의 100년 포트폴리오 전쟁")
        print("4. 투자 기록 / 점수 확인")
        print("5. 프로그램 종료")
        print()

    def input_menu(self):
        menu = input("메뉴를 선택하세요: ")
        return menu
