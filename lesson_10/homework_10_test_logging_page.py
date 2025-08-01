import pytest
import logging
from .homework_10 import log_event

class TestLoggingWebPage:

    @pytest.mark.parametrize('username, status',
                             [("Nosorog", "success"),
                              ("Begemot", "expired"),
                              ("Slon", "failed"),
                              ("Antilopa", "other")])

    def test_logging_page(self, username, status):
        log_event(username, status)
        with open("login_system.log", "r") as file:
            content = file.read()
            lines = content.splitlines()
        assert username in lines[-1]
        assert status in lines[-1]






    # def test_log_event_success_logged(self, caplog):
    #     username = "alice"
    #     status = "success"
    #     expected_result = f"Login event - Username: {username}, Status: {status}"
    #     with caplog.at_level("INFO", logger="login_logger"):
    #         log_event(username, status)
    #     actual_result = caplog.records[0].message
    #     assert expected_result == actual_result
