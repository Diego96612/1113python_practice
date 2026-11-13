# 班級成績計算器（模板）
n = int(input("請輸入學生人數："))

total = 0
# TODO 功能一：在這裡準備需要的變數

for i in range(1, n + 1):
    score = int(input("請輸入第 " + str(i) + " 位的分數："))
    total = total + score
    # TODO 功能一：在這裡更新最高分、最低分、及格人數

average = total / n

print("====== 結果 ======")
print("總分：", total)
print("平均：", round(average, 1))
# TODO 功能一：印出最高分、最低分、及格人數
# TODO 功能二：列出低於平均的同學