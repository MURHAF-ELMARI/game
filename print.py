
def longWord(s):
    #repet = [False] * 128 # to check the reptation
    w_len=0     #longest word length
    last=''       #longest word start point
    w_e=0        #longest word end
    a=[0]*128
    temp=1
    for i in range(1,len(s)):
        if(a[ord(s[i])]!=0):
                w_e=ord(s[i-1])
                print(s[i-1])
                w_len=temp
                temp=1


        else:
            a[ord(s[i])]=ord(s[i-1])
            temp+=1
    word=chr(w_e)
    for i in range(w_len-1):
        word=chr(a[w_e])+word
        w_e=a[w_e]
    return word



s = 'Microsoftxyz'
word = longWord(s)
print(word)
