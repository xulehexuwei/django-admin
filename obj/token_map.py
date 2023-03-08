class TokenMapRefreshToken():
    def __init__(self):
        self.__token_map_refreshToken = dict()

    def get_refresh_token(self, token: str):
        return self.__token_map_refreshToken.get(token)

    def set_refresh_token(self, token, refresh_token: str):
        self.__token_map_refreshToken[token] = refresh_token

    def del_token(self, token: str):
        try:
            del self.__token_map_refreshToken[token]
        except:
            pass


tokenMapRefreshToken = TokenMapRefreshToken()
