grondgetallen=[ 4, 5, 3, -81 ]
def kwadraten_som(grondgetallen):
    sum = 0
    for c in grondgetallen:
        if c > 0:
            sum += c**2
    print(sum)
kwadraten_som(grondgetallen)
