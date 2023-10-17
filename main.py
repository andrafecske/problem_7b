a = int(input())
b = int(input())

def longest_seq(a, b, l):
    lnew = []
    lmax = []
    leng = 0
    lengmx = 0
    for i in range(len(l)):
        if l[i] > a and l[i] < b:
            lnew.append (l[i])
            leng+=1
        else:
            if leng > lengmx:
                lengmx = leng
                lmax = lnew[:]
            lnew.clear()
            leng = 0
    if leng > lengmx:
        lengmx = leng
        lmax = lnew[:]
    print (lmax)

list = [ 2, 1, 4, 6 , 8, 11, 5, 7, 9, 6 ]
longest_seq (a, b, list)




