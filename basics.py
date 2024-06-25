# python Basics

# Identifiers

# variables
# comment if
#
#
# hello = 45
# print("Hello ---> ", hello)
# accpets alphabets
# hello155 = 777
# print(hello155)
# hello8webjkhsjdkhfkjsdhjfkhsjksfhjksdhfjksdhfkjhsdkjfhsdkjhf = 777
# print(hello8webjkhsjdkhfkjsdhjfkhsjksfhjksdhfjksdhfkjhsdkjfhsdkjhf)
# __ ==> Private
# _ ==> Protected
# public
# hello =777
# print("Hello ---> ", hello)
# print("id of hello ---> ", id(hello))
# HELlO =8888
# print("Hello ---> ", HELlO)
# print("id of HELlO ---> ", id(HELlO))
# hello = 9999
# print("Hello2 ---> ", hello)
# print("id of hello2 ---> ", id(hello))


import keyword

print("Keyword List ---> ", keyword.kwlist)
# ['False', 'None', 'True',
# 'and', 'as', 'assert', 'async', 'await', 'break',
#  'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for',
#  'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or',
#  'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# Rules for identifiers
# 1. Can not start with number
# 2. Can not start with special characters
# 3. Can not use keyword

# Examples
# 1. hello = 45  ==> True
# 2. hello155 = 777 ==> True
# 3. hello8webjkhsjdkhfkjsdhjfkhsjksfhjksdhfjksdhfkjhsdkjfhsdkjhf = 777 ==> True
# 4. __hello = 999 ==> True
# 5. _hello = 999 ==> True
# 6. #hello ="jjhjkk" ===> False
# 7. hui@oo = "342" ==> False
# 8. __ijji__ ="3424" ==> True
# 9. import = 78687 ==> False
#10. True =3242
