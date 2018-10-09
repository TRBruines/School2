def nested2(n):
    for j in range(n,11):
        for i in range(n,11):
            c = i * j
            print(i,'x' ,j ,'=',c )
        print()
    else:
        print('Klaar!')
n = 1
nested2(n)