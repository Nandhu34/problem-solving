a=  "qoloi"

# # by  for  loop  
# reversed_word =  ""
# for char_  in  range(len(a)-1,  -1, -1  ):
#     reversed_word+= a[char_]

# print(reversed_word)

# # by  python  prebuild  method 
# reverse_a =   reversed(a)

# str_a =   ''.join(reverse_a)
# print(str_a)


def   reverse_word(word ):
    reversed_str =   ""
    if   len(word)==1:
        return   word 
    return  word [-1]+ reverse_word(word[:-1])

rev_a =   reverse_word("hello")

print(rev_a)