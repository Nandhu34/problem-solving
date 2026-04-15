from     collections  import  defaultdict 
a="king of  heavenAAQ"

vowels =defaultdict(int)
for  char_  in  a:
    print(char_)
    if  char_  in   ['a','e','i','o', 'u', 'A','E','I','O','U']:
        print(char_)
        vowels[char_]+=1

print(vowels)
