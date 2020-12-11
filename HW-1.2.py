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

if total_ticket <= lim and pay >= sum_1:
    print(str(buyable) + ',' + '$' + str(make_change))
if total_ticket <= lim and pay < sum_1:
    print(str(buyable) + ',' + '-2')
if total_ticket > lim and pay >= sum_1:
    print('-1' + ',' + '$' + str(make_change))
if total_ticket > lim and pay < sum_1:
    print('-1' + ',' + '-2')
