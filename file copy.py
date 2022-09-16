import shutil
import os

shutil.copyfile('test.txt', 'copy.txt')


#move

src = 'test.txt'
dest = 'D:\\Downloads\\text.txt'

try:
    if os.path.exists(dest):
        print('there is already a file')
    else:
        os.replace(src,dest)
        print("file was moved")

except FileNotFoundError:
    print(src+' was not found')


#delete


try:
    os.remove('test1.txt')

except FileNotFoundError:
    print('no file')

#for folder
#os.rmdir(folder)  empty folder
#  shutil.rmtree(path)   filled folder