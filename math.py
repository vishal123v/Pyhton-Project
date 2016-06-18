
sum1 = 3

while True:
    x = int(raw_input())
    y = int(raw_input())
    try:
        sum1 = x/y
    except Exception as er:
        print 'Error:', er
    else:
        print sum1
