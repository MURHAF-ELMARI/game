def longWord(s):
    repet=[-1]*(128+32)
    temp=0
    best_w_len=0
    beg=0
    s+=s[0]
    s=list(s)
    for i in range(len(s)):
        if(repet[ord(s[i])]!=-1):
            s[len(s)-1]=s[repet[ord(s[i])]+1]
            if(temp>best_w_len):
                best_w_len=temp
                beg=i-best_w_len
            temp=i-repet[ord(s[i])]-1
            repet[ord(s[i])]=0


        temp+=1
        repet[ord(s[i])]=i
    best_w=''
    for i in range(best_w_len):
        best_w=best_w+s[beg]
        beg+=1
    return best_w



s = 'Microsoftopqrstuvwxyzabcd'
print(longWord(s))