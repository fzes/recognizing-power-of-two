a = int(input('?'))
while True :
    if a//2 == a/2 :
        a = a/2
        if a/2 == 1 :
            print('this number is a power of two.')
            break    
    else :
        print('this number is not a power of two.')
        break        