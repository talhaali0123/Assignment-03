Word=input('enter a word: ')
word=list(Word)
print(word)
a=0
e=0
I=0
o=0
u=0
for i in range(len(word)):
    if word[i]=='a':
        a=a+1
    elif word[i]=='e':
        e=e+1
    elif word[i]=='i':
        I=I+1
    elif word[i]=='o':
        o=o+1
    elif word[i]=='u':
        u=u+1
print(a+e+I+o+u ,"Number of times vowels appear")
print('a appeards',a,'times')
print('e appeards',e,'times')
print('i appeards',I,'times')
print('o appeards',o,'times')
print('u appeards',u,'times')
