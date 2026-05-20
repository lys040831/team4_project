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

    def get_menu_choice(self):
        choice = input("메뉴 번호를 입력하세요: ")
        return choice

    def show_project_info(self):
        print()
        print("[프로젝트 설명]")
        print("이 프로그램은 디지털 금융 학습을 위한 콘솔 기반 미니게임입니다.")
        print("사용자는 투자 상식, 사기 회피, 투자 판단 과정을 게임 형식으로 경험합니다.")
        print()
        print("게임 1: 투자 관련 기초 개념을 퀴즈로 학습")
        print("게임 2: 의심스러운 투자 상황에서 사기 위험을 판단")
        print("게임 3: 실제 투자자가 되어 자산 배분과 투자 선택을 체험")
