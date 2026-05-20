from app.games import config


def find_best_asset(returns):
    best_asset = config.ASSET_NAMES[0]
    best_return = returns[best_asset]
    for asset_name in config.ASSET_NAMES:
        if returns[asset_name] > best_return:
            best_asset = asset_name
            best_return = returns[asset_name]
    return best_asset


def find_worst_asset(returns):
    worst_asset = config.ASSET_NAMES[0]
    worst_return = returns[worst_asset]
    for asset_name in config.ASSET_NAMES:
        if returns[asset_name] < worst_return:
            worst_asset = asset_name
            worst_return = returns[asset_name]
    return worst_asset


def make_choice_message(best_count, worst_count):
    if best_count >= 4 and worst_count <= 2:
        return "좋은 자산에 비교적 많이 배분한 편입니다."
    if worst_count >= 4:
        return "부진했던 자산 비중이 커서 손실 위험이 컸습니다."
    if best_count > worst_count:
        return "좋은 자산 쪽으로 조금 더 기울어져 있었습니다."
    if best_count == worst_count:
        return "좋은 자산과 부진한 자산 비중이 비슷했습니다."
    return "좋은 자산보다 부진한 자산 비중이 더 컸습니다."


def analyze_choice(allocation, returns):
    best_asset = find_best_asset(returns)
    worst_asset = find_worst_asset(returns)
    best_count = allocation[best_asset]
    worst_count = allocation[worst_asset]
    analysis = {}
    analysis["best_asset"] = best_asset
    analysis["best_return"] = returns[best_asset]
    analysis["best_count"] = best_count
    analysis["worst_asset"] = worst_asset
    analysis["worst_return"] = returns[worst_asset]
    analysis["worst_count"] = worst_count
    analysis["message"] = make_choice_message(best_count, worst_count)
    return analysis
