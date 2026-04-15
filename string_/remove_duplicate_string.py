a="programming"

seen_list =  set()

result  =[]


for  char_  in    a:
    if   char_  not  in    seen_list:
        seen_list.add(char_) 
        result.append(char_)
print(''.join(result)) 




# print(dict.fromkeys(a))