def longWord(s):
    repet=[-1]*(128+32)
    temp=0
    best_w_len=0
    beg=0
    s+=s[0]
    s=list(s)
    i=0
    while(i<len(s)):
        print('9 line', s[i],repet[ord(s[i])])
        if(repet[ord(s[i])]!=-1):
            x=repet[ord(s[i])]
            if(temp>best_w_len):
                print('temp',temp)
                best_w_len=temp
                beg=i-best_w_len

            repet=[-1]*(128+32)
            s[len(s)-1]=s[i]
            print('i ',i)
            print(s)
            print('24 line',s[i],end=' ')
            print( repet[ord(s[i])])
            print('line 25 ' , temp)
            temp=0

            i=x+1
            continue
        temp+=1
        repet[ord(s[i])]=i
        i+=1

    best_w=''

    for i in range(best_w_len):
        best_w=best_w+s[beg]
        beg+=1
    return best_w





s = 'Al-Khwarizmi'

s = 'Solution'

s = 'Microsoft'

s = 'abcd'

s = 'abbcde'

s = 'Microssdoftxyz'

s = 'abcdefghabcdefghijklmnopqrstuvwx'

s = 'Microsoftopqrstuvwxyzabcd'
print(longWord(s))




