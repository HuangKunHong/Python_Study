# 1. 判断空白字符串
space_str = "   \t\n\r"

print(space_str.isspace())

# 2. 判断字符串中是否只包含数字
# num_str = "1.1"
# 2> unicode 字符串
# num_str = "⑴"
# num_str = "\u00b2"
# 3> 中文数字
num_str = "一千零一"



print(num_str)
print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())