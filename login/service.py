from obj.jwt_token import JwtToken
from django.http import HttpRequest
from obj.token_map import tokenMapRefreshToken
import common


class AccountPermission():

    def __init__(self):
        self.token = None
        self.refresh_token = None
        self.login_success = False

    def loginVerify(self, username, password: str):
        if username == "xuwei" and password == "xuwei":
            # TODO 账号密码验证
            payload = dict(name=username)
            # 这个每次请求会刷新，当token过期，而refresh_token未过期的时候，会重新颁发token，如果refresh_token也过期了，那就退出登录了
            token = JwtToken.generate_token(payload, common.JwtTokenExpired)
            refresh_token = JwtToken.generate_token(payload, common.JwtRefreshTokenExpired)
            tokenMapRefreshToken.set_refresh_token(token, refresh_token)  # 相当于缓存了token对应的refresh_token
            return token
        else:
            return None

    def tokenVerify(self, token):
        success, payload = JwtToken.parse_token(token)
        if success:
            # token 还有效，刷新 refresh_token
            refresh_token = JwtToken.generate_token(payload, common.JwtTokenExpired)
            tokenMapRefreshToken.set_refresh_token(token, refresh_token) # 更新缓存
            print(tokenMapRefreshToken)
            return success

        # token 过期， 查看 refresh_token 是否过期
        refresh_token = tokenMapRefreshToken.get_refresh_token(token)
        success, payload = JwtToken.parse_token(refresh_token)
        if not success: return success  # refresh_token 过期，即验证失败，返回False，退出登录

        # refresh_token 有效，换取新的 token，同时刷新 refresh_token，并删除缓存的老token
        new_token = JwtToken.generate_token(payload, common.JwtTokenExpired)
        refresh_token = JwtToken.generate_token(payload, common.JwtRefreshTokenExpired)
        tokenMapRefreshToken.set_refresh_token(new_token, refresh_token)
        tokenMapRefreshToken.del_token(token)
        print(tokenMapRefreshToken)
        self.token = new_token
        return True
