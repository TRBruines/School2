
def convert(c):
    f = c * 1.8 + 32
    print('{:3} {:4}'.format(int(f),c))

def table(z,x,c):
    print('  {:4} {:2}'.format('F', 'C'))
    for i in range(z,x,c):
        convert(int(i))

table(-30,41,10)