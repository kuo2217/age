driving = input('請問你有沒有開過車?')
if driving != '有' and driving != '沒有':
    print('我是問你有沒有!!!')
    raise SystemExit
    
age = input('請問你的年齡?')
age = int(age)
if driving == '有':
    if age >= 18:
        print('你通過測驗了!')
    else:
        print('你不能無照駕駛!!!')
elif driving == '沒有':
    if age >= 18:
        print('你可以考駕照了!')
    else:
        print('再過幾年就可以考駕照了!')

