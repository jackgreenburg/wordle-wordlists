from typing import Tuple, List
import regex as re

def format_list(list_as_string: str) -> List[str]:
    word_regex = r"\"(\D{5})\""
    return set(re.findall(word_regex, list_as_string))


def get_wordlist(filename: str, answers_var_name: str, word_list_var_name: str) -> Tuple[List[str], List[str]]:
    with open(filename, "r", encoding="cp437") as f:
        text = f.read()
    answers_regex = fr"{answers_var_name}=\[(.*?)\]"
    answers = re.search(answers_regex, text).group()

    word_list_regex = fr"{word_list_var_name}=\[(.*?)\]"
    word_list = re.search(word_list_regex, text).group()
    return format_list(answers), format_list(word_list)

def get_wordlists(filename: str) -> Tuple[List[str], List[str]]:
    with open(filename, "r", encoding="cp437") as f:
        text = f.read()
    # lists_regex = r"\[[\"(\D{5})\"]*?\]"

    lists_regex = r"(\[(\"[a-z]{5}\",?)+\])"
    answers = re.findall(lists_regex, text)
    print(answers[0][0])
    return format_list(answers[0][0]), format_list(answers[1][0])

def save_wordlist(filename: str, wordlist: List[str]):
    with open(filename, 'w') as f:
        for word in wordlist:
            f.write(f"{word}\n")

def main():
    answers_old, guessable_old = get_wordlist("jan_01_wordle_snapshot.js", "Aa", "La")
    # answers_new, w = get_wordlist("apr_18_wordle_snapshot.js", "mo", "fo")
    # answers_new, w = get_wordlist("may_09_wordle_snapshot.js", "ko", "wo")
    answers_new, guessable_new = get_wordlist("aug_03_wordle_snapshot.js", "he", "be")

    print("old wordlist # answers:", len(answers_old))
    print("new wordlist # answers:", len(answers_new))
    # save_wordlist("answers_old.txt", answers_old)
    # save_wordlist("answers_new.txt", answers_new)

    added = [answer for answer in answers_new if answer not in answers_old]
    print("answers added:", added)
    removed = [answer for answer in answers_old if answer not in answers_new]
    print("answers removed:", removed)

    print("old wordlist # guesses:", len(guessable_old))
    print("new wordlist # guesses:", len(guessable_new))
    # save_wordlist("guessable_old.txt", guessable_old)
    # save_wordlist("guessable_new.txt", guessable_new)

    added = [answer for answer in guessable_new if answer not in guessable_old]
    print("guesses added:", added)
    removed = [answer for answer in guessable_old if answer not in guessable_new]
    print("guesses removed:", removed)

if __name__ == "__main__":
    main()
