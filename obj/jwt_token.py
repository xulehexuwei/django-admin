from datetime import datetime, timedelta
import jwt


class JwtToken(object):
    _salt = "@^4_00wedv**pi)+(!w1rwi=d3q4l=ie=g-u$s8jevmj*zgg2h"
    _expire_message = dict(code=1200, msg="token 已经失效")
    _unknown_error_message = dict(code=4200, msg="token 解析失败")

    @classmethod
    def generate_token(cls, payload: dict, expSeconds: int) -> str:
        """
        :param payload: 信息体
        :param expSeconds: 过期时间
        :return:
        """
        payload["exp"] = datetime.utcnow() + timedelta(seconds=expSeconds)
        headers = dict(typ="jwt", alg="HS256")
        resut = jwt.encode(payload=payload, key=cls._salt, algorithm="HS256", headers=headers)
        return resut

    @classmethod
    def parse_token(cls, token: str) -> tuple:
        verify_status = False
        try:
            payload_data = jwt.decode(token, cls._salt, algorithms=['HS256'])
            verify_status = True
        except jwt.ExpiredSignatureError:
            payload_data = cls._expire_message
        except Exception as _err:
            payload_data = cls._unknown_error_message
        return verify_status, payload_data


if __name__ == '__main__':
    # TEST_DATA = dict(name="mooor")
    # token = JwtToken.generate_token(TEST_DATA, 10)
    # print(token)
    # payload = JwtToken.parse_token(token)
    # print(payload)
    #
    # import time
    # time.sleep(11)
    token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6Imp3dCJ9.eyJuYW1lIjoieHV3ZWkiLCJleHAiOjE2NzgyODM2NzJ9.Dt97hD8khmGEWFaByhd_iCqauba6L2P_2CQ7tC8dqcA'
    payload = JwtToken.parse_token(token)
    print(payload)
