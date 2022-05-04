"""
File: class_reviews.py
Name:
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""


def main():
    """
    TODO:
    """
    # 初始元素
    SC001_score = 0
    SC101_score = 0
    SC001_Times = 0
    SC101_Times = 0
    SC001_Max = 0
    SC101_Max = 0
    SC001_Min = 0
    SC101_Min = 0
    SC001_Avg = 0
    SC101_Avg = 0

    while True:
        print(f'Which class?')
        classname = input().upper() #將所有數入字符改為大寫

        if classname == "-1":
            break
        elif classname == "SC001":
            SC001_Times += 1 #計算數入次數
            print("Score:")
            New_Score = input()
            New_Score = int(New_Score)
            SC001_score += New_Score
            if New_Score > SC001_Max: #計算最大值
                SC001_Max = New_Score
            if SC001_Min == 0:
                SC001_Min = New_Score #當最小值為0顯示當前數值
            if SC001_Min > New_Score: #當計算最小值
                SC001_Min = New_Score
                SC001_Avg = SC001_score / SC001_Times #計算平均值

        elif classname == "SC101":
            SC101_Times += 1 #計算數入次數
            print("Score:")
            New_Score = input()
            New_Score = int(New_Score)
            SC101_score = SC101_score + New_Score
            if SC101_Max < New_Score: #計算最大值
                SC101_Max = New_Score
            if SC101_Min == 0:
                SC101_Min = New_Score #當最小值為0顯示當前數值
            if SC101_Min > New_Score: #當計算最小值
                SC101_Min = New_Score
                SC101_Avg = SC101_score / SC101_Times #計算平均值

    print(f'=============SC001=============')
    if SC001_Times > 0:
        print(f'Max (001): {SC001_Max} ')
        print(f'Min (001): {SC001_Min} ')
        print(f'Avg (001): {SC001_Avg} ')
    else:
        print(f'No score for SC001')
    print(f'=============SC101=============')
    if SC101_Times > 0:
        print(f'Max (101): {SC101_Max} ')
        print(f'Min (101): {SC101_Min} ')
        print(f'Avg (101): {SC101_Avg} ')
    else:
        print(f'No score for SC101')

    pass

# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()


