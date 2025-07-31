def get_num_words(book_text):
    split_words = book_text.split()
    return len(split_words)

def get_num_chars(book_text):
    book_text_lower = book_text.lower()
    final_dic = {}
    for  b in book_text_lower:
        if b in final_dic:
            final_dic[b]+= 1
        else:
            final_dic[b] = 1
    return final_dic

def sort_on(dic):
    return dic["num"]

def sort_dic(char_dic):
    final_list = []
    for c in char_dic:
        if(c.isalpha()==True):
            final_list.append({"name":c, "num":char_dic[c]})
    final_list.sort(reverse=True, key = sort_on)
    return final_list
 

