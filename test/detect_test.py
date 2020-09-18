from src.main import detect_keywords


def test_detect_keyword():
    text = "She really got you"
    assert detect_keywords(text, "really got you")
    assert not detect_keywords(text, "ally")