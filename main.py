### REGULAR EXPRESSIONS || REGEX ###
# match - перевіряє початок рядка на співпадіння з паттерном    (після патерна може бути будь-що)
# fullmatch - перевіряє рядок на повне співпадіння з патерном   (повне спіпадіння з паттерном)
# search - просто шукає в рядку будь-де співпадіння
# [] - дужки для формули
# -  - діапазон     [a-z]
# +  - повтор елемента, або формули 1 або більше разів
# *  - повтор елемента, або формули 0 або більше разів
# .  - будь який елемент
# \  - показує що наступний елем
# |  - вибір із декількох (логічне або) (a|bb|c) - шукає a або bb або c
# {} - використовується для указування кількості повторів елементу або формули
# ?  - повтор елемента, або формули 0 або 1 раз
# $  - позначає кінець рядка

# import re
#
# patt = 'ab{2,3}'
# test_strings = ["a",'ab', "abb", "cabbb","abc", "b", ".", "abbb"]
# for test_string in test_strings:
#     if re.search(patt,  test_string):
#         print(f"{test_string} matches the pattern")
#     else:
#         print(f"{test_string} does not matches the pattern")


# import re
#
# test_strings = ["a_b", "ab", "abb", 'CAbbb_', "ac__", "Abc_", "b", ".", "A_"]
# patt = '[A-Z][a-z]+'
# for test_string in test_strings:
#     if re.search(patt,  test_string):
#         print(f"{test_string} matches the pattern")
#     else:
#         print(f"{test_string} does not matches the pattern")





import re

patt = '^[a-zA-Z]+ {0,1}'
test_strings = [" abc.", "abvbc", "1udxn", "acvb. ", 'bvb', "djf ","fhg jer"]
for test_string in test_strings:
    if re.search(patt,  test_string):
        print(f"{test_string} matches the pattern")
    else:
        print(f"{test_string} does not matches the pattern")



# import re
# test_strings = ["abc.", "abvbc", "udxn", "acvb.", 'bvb']
# patt = '[.!?,;]$'
# for test_string in test_strings:
#     if re.search(patt,  test_string):
#         print(f"{test_string} matches the pattern")
#     else:
#         print(f"{test_string} does not matches the pattern")


#test version 1.1
















