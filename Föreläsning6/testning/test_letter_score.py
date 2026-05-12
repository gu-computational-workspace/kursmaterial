import letter_score


def test_load_lines():
    test_data = """
    K 2
    M 4
    N 1
    """
    expected_result = ["K 2", "M 4", "N 1"]

    assert letter_score.load_lines(test_data) == expected_result


def test_parse_one_line():
    test_data = "K 2"
    expected_result = ("K", 2)
    assert letter_score.parse_one_line(test_data) == expected_result


def test_get_score():
    test_data = ("K", 2)
    expected_result = 2
    assert letter_score.get_score(test_data) == expected_result


def test_find_best_letter():
    test_data = """
        K 2
        M 4
        N 1
        """
    expected_result = ("M", 4)
    assert letter_score.find_best_letter(test_data) == expected_result