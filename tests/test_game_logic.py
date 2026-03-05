from logic_utils import check_guess, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


def test_parse_guess_rejects_below_range():
    ok, value, err = parse_guess("0")
    assert ok is False
    assert value is None
    assert err == "Guess must be between 1 and 100."


def test_parse_guess_rejects_above_range():
    ok, value, err = parse_guess("101")
    assert ok is False
    assert value is None
    assert err == "Guess must be between 1 and 100."


def test_parse_guess_accepts_boundary_values():
    ok_low, val_low, _ = parse_guess("1")
    assert ok_low is True and val_low == 1

    ok_high, val_high, _ = parse_guess("100")
    assert ok_high is True and val_high == 100
