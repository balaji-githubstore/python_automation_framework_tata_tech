import pytest


class TestDemo():

    @pytest.mark.parametrize("username,password",
                             [
                                 ("john", "john123"),
                                 ("peter", "peter123")
                             ])
    def test_login(self, username, password):
        print("demo" + username + password)
