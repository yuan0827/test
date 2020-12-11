# 分別輸入全票張數，全票價格，學生票張數，學生票價格，付的錢，總票數上限之數值
adult_ticket = int(input())
A_price = int(input())
student_ticket = int(input())
S_price = int(input())
pay = int(input())
lim = int(input())

total_ticket = adult_ticket + student_ticket  # 算出總票數
sum_1 = adult_ticket * A_price + student_ticket * S_price  # 算出花費總金額
make_change = pay - sum_1  # 算出找錢
buyable = lim - total_ticket  # 算出仍可購票數

# 先判斷總票數是否超出上限，再判斷是否付得起，分別決定是否印出可購票數以及找錢
if total_ticket <= lim:
    if pay >= sum_1:
        print(str(buyable) + ',' + '$' + str(make_change))
    else:
        print(str(buyable) + ',')
if total_ticket > lim:
    if pay >= sum_1:
        print('$' + str(make_change))
    else:
        print()

'''
if total_ticket <= lim and pay >= sum_1:  # 如果總張數控制在上限內且付的錢足夠，則印出仍可購票數及找錢
    print(str(buyable) + ',' + '$' + str(make_change))
if total_ticket <= lim and pay < sum_1:  # 如果總張數控制在上限內但付的錢不夠，則只印出仍可購票數
    print(str(buyable) + ',')
if total_ticket > lim and pay >= sum_1:  # 如果總張數超過上限但付的錢足夠，則只印出找錢
    print('$' + str(make_change))
if total_ticket > lim and pay < sum_1:   # 如果總張數超過上限且付的錢不夠，則什麼皆不印出
    print()
'''

