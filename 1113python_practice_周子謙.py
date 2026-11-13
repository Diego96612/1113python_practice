# 班級成績計算器（模板）

# 在輸入分數的迴圈裡，把每個分數存進串列。 算完平均後，再用一個 for 找出低於平均的同學，印出座號和分數。 
# 最後印出低於平均的人數。 如果沒有人低於平均（例如全班同分），就印出「沒有人低於平均」。

# 完成檢查清單 用範例資料 85、42、60、73、59，輸出和上面完全一樣 輸入 1 位、分數 100，最高分和最低分都是 100 輸入 3 位、分數都是 0，最低分是 0，
# 及格人數是 0 輸入 3 位、分數都是 80，顯示「沒有人低於平均」 輸入一位剛好 60 分的同學，有算進及格人數 功能一沒有用到 max()、min()

n = int(input("請輸入學生人數："))

total = 0
# TODO 功能一：在這裡準備需要的變數
score_list = []
less_than_average = []
average_score = 0
for i in range(1, n + 1):
    score = int(input("請輸入第 " + str(i) + " 位的分數："))
    score_list.append(score)

# 平均
average_score = sum(score_list) / len(score_list)

for a in range(len(score_list)):
    if score_list[a] <= (average_score -1):  
        less_than_average.append(score_list[a])
        print(less_than_average)

average = total / n
print(less_than_average)
print(f"平均{score_list}")

print("====== 結果 ======")
print("總分：", total)
print(average_score)
print(f"低於平均{less_than_average}")
