def load_lines(data):
    lines = data.strip().split("\n")
    lines = [line.strip() for line in lines]
    return lines


def parse_one_line(line):
    letter, number_str = line.split(" ")
    return letter, int(number_str)


def get_score(letter_and_score):
    letter, score = letter_and_score
    return score


def find_best_letter(data):
    lines = load_lines(data)
    letter_and_score_list = []
    for line in lines:
        letter_and_score = parse_one_line(line)
        letter_and_score_list.append(letter_and_score)
    sorted_letter_scores = sorted(letter_and_score_list, key=get_score)
    return sorted_letter_scores[-1]