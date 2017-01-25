from __future__ import print_function
import struct

def redemption(a):

    j = []
    j.append('')
    c = 0
    for i in a:
        j[c] += i

        if i == 'x':
            j.append('')
            c = c+1

    j.remove(j[0])
    for i in xrange(len(j)):
        j[i] = j[i].replace('0x', '')
        #print j[i]
        #print i[0:1]

    word = []
    word.append('')
    k = 0
    for i in j:
        #print i
        for x in range(0,len(i)):
            if x%2 == 0 and x != len(i)-1:
                word[k] += chr(int(i[x:x+2], 16))
        k = k+1
        word.append('')

    for item in word:
        item = item[::-1]
        print (item, end = '')
