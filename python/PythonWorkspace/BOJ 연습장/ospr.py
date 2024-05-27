import os

directory = []
file = []
name = os.getcwd()

def classify_file(path):

    if os.path.isdir(path):
        message = '디렉터리입니다.'
        directory.append(name)
        return message
    elif os.path.is_file(path):
        message = '파일입니다.'
        file.append(name)
        return message



print(classify_file(name))
print(directory)
print(file)