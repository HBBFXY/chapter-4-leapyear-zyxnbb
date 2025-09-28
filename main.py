def is_leap_year(year):
    # 年份为0是闰年，负数不是闰年
    if year == 0:
        return True
    if year < 0:
        return False
    # 闰年判断规则
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def main():
    user_input = input("请输入年份：")
    try:
        # 判断输入是否为整数
        year = int(user_input)
        # 小数检测
        if "." in user_input or user_input.strip() != str(year):
            print("输入错误")
            return
    except ValueError:
        print("输入错误")
        return

    if is_leap_year(year):
        print("是闰年")
    else:
        print("不是闰年")

if __name__ == "__main__":
    main()
