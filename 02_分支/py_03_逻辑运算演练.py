# 练习1: 定义一个整数变量 age，编写代码判断年龄是否正确
age = 1202

# 要求人的年龄在 0-120 之间
"""
age >= 0 or age <= 120  ×
age >= 0 and age <= 120  √
"""
if age >= 0 and age <= 120:
    print("年龄正确")
else:
    print("年龄不正确")
# 练习2: 定义两个整数变量 python_score、c_score，编写代码判断成绩
python_score = 20
c_score = 25

# 要求只要有一门成绩 > 60 分就算合格
if python_score > 60 or c_score > 60:
    print("考试通过")
else:
    print ("考试失败，继续努力")


# 练习3: 定义一个布尔型变量 is_employee，编写代码判断是否是本公司员工
is_employee = False
# 如果不是提示不允许入内
# 在开发中，通常希望某个条件不满足时，执行一些代码，可以使用not
# 另外，如果需要拼接复杂的逻辑计算条件，同样也有可能使用到 not
if not is_employee:
    print("非本公司人员，请勿入内")
else:
    print("欢迎入内")
