import pytest
import requests
import allure

class TestLogin:
    data = [
        {
            "qq": 879075962
        },
        {
            "qq": 35296459986
        },
        {
            "qq": 879075962
        }
    ]

    @pytest.mark.parametrize("account", data)
    def test_login(self, account):

        url = "https://api.oioweb.cn/api/qq/info"
        data = {
            "qq": account["qq"]
        }
        resp = requests.post(url=url, data=data)
        data = resp.json()
        assert data is not None
