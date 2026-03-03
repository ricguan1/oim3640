# def check_vowel(s):
#     for c in s:
#         result = (c in 'aeiou')
#     return result
# print(check_vowel('orange'))   # ?
# print(check_vowel('lemon'))    # ?
# print(check_vowel('kiwi'))     # ?

# def any_vowel(s):
#     flag = False
#     for c in s:
#         flag = flag or (c in 'aeiou')
#     return flag
# print(any_vowel('rhythm'))   # ?
# print(any_vowel('cafe'))     # ?
# print(any_vowel('sky'))      # ?

def has_space(s):
    for c in s:
        if c == ' ':
            break
            return True
    return False
print(has_space('ice cream'))   # ?
print(has_space(' hello'))      # ?
print(has_space('pizza'))       # ? why does this only show false when there are no spaces?




