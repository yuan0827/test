# 分別輸入全票張數，全票價格，學生票張數，學生票價格，付的錢之數值
adult_ticket = int(input())
A_price = int(input())
student_ticket = int(input())
S_price = int(input())
pay = int(input())

sum1 = adult_ticket * A_price + student_ticket * S_price  # 算出花費總金額
make_change = pay - sum1  # 算出找錢

if pay >= sum1:  # 如果付的錢夠，則印出＄找錢
    print('$' + str(make_change))  # 將找錢之數值轉換成字串和＄一同印出
else:
    print('-1')
