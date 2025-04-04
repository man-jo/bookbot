def get_num_words(text):
    return len(text.split())

def character_distrib(text):
    char_dict = dict()
    for char in text.lower():
        if not char in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def sort_on(dict,key="n"):
    return dict[key]

def sort_char_dict(char_dict):
    sorted_char = []
    for c in char_dict:
        sorted_char.append({"char":c, "n":char_dict[c]})
    sorted_char.sort(reverse=True, key=sort_on)
    return sorted_char
