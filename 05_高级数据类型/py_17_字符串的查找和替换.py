hello_str = "hello world"

# 1. 判断是否以指定字符串开始
print(hello_str.startswith("Hello"))

# 2. 判断是否以指定字符串结束
print(hello_str.endswith("world"))

# 3. 查找指定字符串
# index同样可以查找指定的字符串在大字符串中的索引
print(hello_str.find("llo"))
# index如果指定的字符串不存在，会报错
# find如果指定的字符串不存在，会返回-1
# print(hello_str.index("abc"))
print(hello_str.find("abc"))

# 4. 替换字符串
print(hello_str.replace("world", "Python"))

print(hello_str)