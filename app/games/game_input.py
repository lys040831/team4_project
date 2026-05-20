from app.games import config


def ask_one_asset(asset_name):
    user_input = input(asset_name + " 배분: ")
    user_input = user_input.strip()
    if user_input.startswith("-") and user_input[1:].isdigit():
        return -int(user_input[1:])
    if not user_input.isdigit():
        return None
    return int(user_input)


def check_allocation_number(asset_count):
    if asset_count < config.MIN_ALLOCATION:
        print("음수는 입력할 수 없습니다. 처음부터 다시 입력합니다.")
        return False
    if asset_count > config.MAX_ALLOCATION:
        print("각 자산은 10칸을 넘을 수 없습니다. 처음부터 다시 입력합니다.")
        return False
    return True


def get_allocation_total(allocation):
    total = 0
    for asset_name in config.ASSET_NAMES:
        total = total + allocation[asset_name]
    return total


def is_total_allocation(total):
    return total == config.TOTAL_ALLOCATION


def ask_allocation():
    while True:
        print()
        print("네 자산에 총 " + str(config.TOTAL_ALLOCATION) + "칸을 배분하세요.")
        print("각 자산은 0~10 사이 정수로 입력합니다. 올인도 가능합니다.")
        allocation = {}
        is_wrong = False
        for asset_name in config.ASSET_NAMES:
            asset_count = ask_one_asset(asset_name)
            if asset_count is None:
                print("숫자만 입력해 주세요. 처음부터 다시 입력합니다.")
                is_wrong = True
                break
            if not check_allocation_number(asset_count):
                is_wrong = True
                break
            allocation[asset_name] = asset_count
        if is_wrong:
            continue
        total = get_allocation_total(allocation)
        if not is_total_allocation(total):
            print("배분 합계는 반드시 " + str(config.TOTAL_ALLOCATION) + "이어야 합니다.")
            print("현재 합계:", total)
            print("처음부터 다시 입력합니다.")
            continue
        return allocation


def ask_continue():
    while True:
        user_input = input("다음 라운드는 Enter, 중간 종료는 q를 입력하세요: ")
        user_input = user_input.strip().lower()
        if user_input == "":
            return True
        if user_input == "q":
            return False
        print("Enter 또는 q만 입력해 주세요.")
