# 需求
#
# 在控制台连续输出五行 *，每一行星号的数量依次递增
# *
# **
# ***
# ****
# *****
# 开发步骤
#
# 1> 完成 5 行内容的简单输出
# 2> 分析每行内部的 * 应该如何处理？

row = 1

while row <= 5:

    # 每一行要打印的星星就是和当前的行数是一致的
    # 增加一个小的循环，专门负责当前行中，每一 ‘列’ 的星星显示
    # 1. 定义一个计数器变量
    col = 1

    # 2. 开始循环
    """
    1
    2
    3
    4
    5
    """
    while col <= row:
        print("*", end="")

        col += 1

    # print("第 %d 行" % row)
    print("")

    row += 1