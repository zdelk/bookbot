
def word_count(text):
    return len(text.split())

def char_count(text):
    text_lower = text.lower()
    char_dict = {}
    
    for char in text_lower:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
        
    return char_dict

def sort_on(dic):
    return dic["num"]

def sort_dict(char_dict):
    dict_list = []
    for key, val in char_dict.items():
        if key.isalpha():
            dict_list.append({"name":key, "num": val})
        
    dict_list.sort(reverse=True, key=sort_on)
    
    return dict_list