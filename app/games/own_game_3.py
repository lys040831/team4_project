from app.games import config
from app.games.portfolio_game import PortfolioGame


class OwnGame3:
    def play(self):
        game = PortfolioGame()
        score = game.play()
        result = {}
        result["game_name"] = config.GAME_TITLE
        result["score"] = score
        if game.is_quit:
            result["message"] = "중간 종료로 0점 처리되었습니다."
        else:
            result["message"] = game.get_grade()
        return result


def get_game_info():
    game_info = {}
    game_info["number"] = config.GAME_NUMBER
    game_info["title"] = config.GAME_TITLE
    game_info["file_name"] = config.GAME_FILE_NAME
    game_info["score_rule"] = config.GAME_SCORE_RULE
    game_info["score_text"] = config.GAME_SCORE_TEXT
    return game_info


def play():
    game = PortfolioGame()
    return game.play()
