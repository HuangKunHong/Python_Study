import py_message

py_message.send_message.send("Hello")
txt = py_message.receive_message.receive()
print(txt)