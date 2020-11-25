message = '我爱java,我爱python'
with open('D:\\inout9\\tosave', 'w') as example:
    example.write(message)

# mode 'a' 表示增量输入
addmessage = 'This is a single line to add.'
with open('D:\\inout9\\tosave', 'a', ) as example:
    example.write('\n'+addmessage)
    example.write('\t'+addmessage)

with open('D:\\inout9\\tosave', 'r') as example:
    # io.UnsupportedOperation: not writable
    # example.write(message)
    print(example.read())
