while True:
    X, Y = map(int,input().split())
    if X==0 or Y==0:
        break
    elif X>0 and Y>0:
        print(f'primeiro')
    elif X>0 and Y<0:
        print(f'quarto')
    elif X<0 and Y<0:
        print(f'terceiro')
    else:
        print(f'segundo')