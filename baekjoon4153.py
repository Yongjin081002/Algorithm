while True:
    li = input().split()
    sorted(li)

    if  li[0] != '0' and li[1] != '0' and li[2] != '0':
        if int(li[0]) ** 2 + int(li[1]) **2  == int(li[2])**2:
            print('right')
        else:
            print('wrong')
    else:
        break
    
