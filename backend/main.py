from text_to_num import text2num
from word2number import w2n

text = input()
str_to_count = ''

operator_dict = {
    'плюс': '+',
    'минус': '-',
    'умножить': '*',
    'делить': '/'
}
operator_words = list(operator_dict.keys())
sort_text = [word for word in text.split() if word != 'на']
word_itog = ''
int_str = ''
for word in sort_text:
    print(word_itog)
    if word in operator_words:
        word_itog += str(text2num(int_str, "ru"))
        word_itog += operator_dict[word]
        int_str = ''
    else:
        int_str += ' ' + word
    print(int_str)
    
word_itog += str(text2num(int_str, "ru"))    
print(word_itog)
print(eval(word_itog))
