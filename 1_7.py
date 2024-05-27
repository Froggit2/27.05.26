text_name = 'File.txt'
text = open(text_name, mode='r')
print(text.read())
text.close()