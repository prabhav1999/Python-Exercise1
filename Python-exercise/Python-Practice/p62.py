fp=open('file.txt','r')
fp.seek(10,0)
content=fp.read(10)
print(content)