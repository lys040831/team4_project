# 3번 게임의 설정과 데이터만 모아 둔 파일입니다.
# 다른 파일에는 주석을 두지 않고, 설명이 필요한 내용은 이 파일에서만 관리합니다.
# 자산 수익률 데이터는 애스워스 다모다란 교수의 뉴욕대학교 스턴 자료를 참고했습니다.
# 게임은 가격 데이터가 아니라 연간 수익률 데이터를 사용합니다.
# 여러 해로 된 구간은 연간 수익률을 복리로 누적한 값입니다.
# 이 게임은 투자 추천이 아니라 교육용 역사 시뮬레이션입니다.

GAME_TITLE = "회귀 투자자의 100년 포트폴리오 전쟁"
GAME_NUMBER = 3
GAME_FILE_NAME = "own_game_3"
GAME_SCORE_RULE = "final_money_round"
GAME_SCORE_TEXT = "최종 자본을 반올림한 정수를 점수로 사용합니다."

INITIAL_MONEY = 100.0
TOTAL_ALLOCATION = 10
MIN_ALLOCATION = 0
MAX_ALLOCATION = 10
LINE_LENGTH = 40

DATA_SOURCE_NAME = "Aswath Damodaran, NYU Stern - Historical Returns on Stocks, Bonds and Bills"
DATA_SOURCE_URL = "https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/histretSP.html"
DATA_SOURCE_DATE = "January 2026"
DATA_YEAR_RANGE = "1928~2025"

ASSET_NAMES = ["S&P500", "미국 10년물 국채", "달러 현금", "금"]
ASSET_SOURCE_COLUMNS = {
    "S&P500": "S&P 500 (includes dividends)",
    "미국 10년물 국채": "US T. Bond (10-year)",
    "달러 현금": "3-month T.Bill",
    "금": "Gold",
}

# 사건 데이터 순서: 제목, 기간, 설명, 주식, 국채, 현금, 금, 해설
EVENT_ROWS = [
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
    if number >= 0:
        return int(number + 0.5)
    return int(number - 0.5)


def make_returns_from_row(row):
    returns = {}
    returns[ASSET_NAMES[0]] = row[3]
    returns[ASSET_NAMES[1]] = row[4]
    returns[ASSET_NAMES[2]] = row[5]
    returns[ASSET_NAMES[3]] = row[6]
    return returns


def make_event_from_row(row):
    event = {}
    event["title"] = row[0]
    event["period"] = row[1]
    event["description"] = row[2]
    event["returns"] = make_returns_from_row(row)
    event["lesson"] = row[7]
    return event


def make_events():
    events = []
    for row in EVENT_ROWS:
        events.append(make_event_from_row(row))
    return events


EVENTS = make_events()
