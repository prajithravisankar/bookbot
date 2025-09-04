def number_of_words_in_text(text: str) -> int:
    return len(text.split(sep=None))

def number_of_time_each_character_appears_in_text(text: str) -> dict[str, int]:
    char_dict = {}
    for ch in text:
        ch = ch.lower()
        if ch.isalpha():
            if ch in char_dict:
                char_dict[ch] += 1
            else:
                char_dict[ch] = 1
    return char_dict



