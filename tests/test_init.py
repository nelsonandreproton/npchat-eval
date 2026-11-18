from npchat_eval import hello


def test_hello_returns_expected_text() -> None:
    result = hello()

    assert result == "Hello from npchat-eval!"
