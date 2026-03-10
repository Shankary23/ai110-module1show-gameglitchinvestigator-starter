from logic_utils import check_guess, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


def test_hint_correct_on_win():
    outcome, hint = check_guess(50, 50)
    assert outcome == "Win"
    assert hint == "🎉 Correct!"

def test_hint_says_lower_when_too_high():
    outcome, hint = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in hint

def test_hint_says_higher_when_too_low():
    outcome, hint = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in hint


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
