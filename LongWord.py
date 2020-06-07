def longWord(s):
    s = s + '0'
    s = list(s)
    a = [""] * 128
    repet = [False] * 128 # to check the reptation
    temp = ''
    long = 0  #length of longest word
    x = 0  # index of longest word

    for i in s:
        if (repet[ord(i)]):
            repet = [False] * 128
            if (len(temp) > len(a[ord(temp[0])])):
                a[ord(temp[0])] = temp
                if (long < len(temp)):
                    x = ord(temp[0])

                    long = len(temp)
                    s[len(s) - 1] = i
                temp = ''

        temp += i
        repet[ord(i)] = True
    return a[x]


s = 'Microsoftopqrstuvwxyzabcd'
word = longWord(s)
print(word)
