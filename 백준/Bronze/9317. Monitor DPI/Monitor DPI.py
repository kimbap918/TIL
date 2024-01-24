while 1:
    d, rh, rv = map(float, input().split())
    if d == rh == rv == 0:
        break
    w = 16 * d / 337**0.5 
    h = w * 9/16
    print('Horizontal DPI: %.2f'%(rh/w))
    print('Vertical DPI: %.2f'%(rv/h))