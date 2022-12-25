from distutils.core import setup

setup(name="py_message",  # 包名
      version="1.0",  # 版本
      description="py's 发送和接收消息模块",  # 描述信息
      long_description="完整的发送和接收消息模块",  # 完整描述信息
      author="py",  # 作者
      author_email="py@python.com",  # 作者邮箱
      url="www.py.com",  # 主页
      py_modules=["py_message.send_message",
                  "py_message.receive_message"])