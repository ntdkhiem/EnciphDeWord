import bcolors as b
a = ''''''
with open('banner_key.txt','r') as f:
    a = f.read()
    f.close()
print a
print a.format(BBLUE=b.BLUE,BEND=b.END)

