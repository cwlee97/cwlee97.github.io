import os
import datetime
import re

d = datetime.datetime.now()
day = d.strftime("{}-{}-{}-".format(d.strftime("%y"), d.strftime("%m"), d.strftime("%d")))

# Rename README.md
before_md_name = ''
md_path = 'C:/Users/Administrator/Desktop/github/Programmers-main/'
file_names = os.listdir(md_path)
for name in file_names:
    if name[-3:] == '.md':
        before_md_name = name
        print(before_md_name)
        break
src = os.path.join(md_path, before_md_name)
dst = os.path.join(md_path, day + "README.md")
os.rename(src, dst)

# File Rename & Edit README.md
dir_list = ['lv1', 'lv2', 'lv3',  'unrated']
file_path = md_path + '프로그래머스/'
md_path = md_path + day + "README.md"
head_py = "---\nlayout: single\ntitle: Programmers_py\ncategories: Programmers_py\n---\n"
head_cpp = "---\nlayout: single\ntitle: Programmers_cpp\ncategories: Programmers_cpp\n---\n"
main = "\nPython 관련 코딩테스트 문제풀이 기록소입니다.\n"
with open(md_path, 'w', encoding = "UTF-8") as f:
    f.write(head_py)
    f.write(main)
    f.close()
        
for dir in dir_list:
    file_path_in = file_path + dir + '/'
    file_names_in = os.listdir(file_path_in)
    # File Rename
    for name in file_names_in:
        if '.' in name:
            state = name.find('.')
            rename = name[state + 2:]
            src = os.path.join(file_path_in, name)
            dst = os.path.join(file_path_in, rename)
            os.rename(src, dst)
for dir in dir_list:
    file_path_in = file_path + dir + '/'
    file_names_in = os.listdir(file_path_in)
    # Edit README.md
    with open(md_path, 'a', encoding = "UTF-8") as f:
        f.write("\n## {}\n".format(dir))
        f.close()
    for i in range(len(file_names_in)):
        name = file_names_in[i]
        n_name = re.sub('\s', '-', name)
        print(n_name)
        with open(md_path, 'a', encoding = "UTF-8") as f:
            f.write('* [{}](https://1stapplepie.github.io/programmers_py/{}/)\n'.format(name, n_name))
            f.close()

## Edit Solution
for dir in dir_list:
    file_path_in = file_path + dir + '/'
    file_names_in = os.listdir(file_path_in)
    for name in file_names_in:
        Solution = os.listdir(file_path_in + name + '/')
        contain_py, contain_cpp = "", ""
        head_py = "---\nlayout: single\ntitle: {}\ncategories: Programmers_py\n---\n".format(name)
        head_cpp = "---\nlayout: single\ntitle: {}\ncategories: Programmers_cpp\n---\n".format(name)
        for sol in Solution:
            if sol[-3:] == ".py":
                with open(file_path_in + "/" + name + "/" + sol, 'r', encoding = "UTF-8") as f:
                    contain_py = f.read()
                    f.close()
            elif sol[-4:] == ".cpp":
                with open(file_path_in + "/" + name + "/" + sol, 'r', encoding = "UTF-8") as f:
                    contain_cpp = f.read()
                    f.close()
        for sol in Solution:
            if sol[-3:] == ".md" and contain_py != "":
                with open(file_path_in + "/" + name + "/" + sol, 'r', encoding = "UTF-8") as f:
                    temp = f.read()
                with open(file_path_in + "/" + name + "/" + sol, 'w', encoding = "UTF-8") as f:
                    f.write(head_py)
                    f.write(temp)
                    f.write("\n\n```py\n")
                    f.write(contain_py)
                    f.write("\n\n```\n")
                    f.close()   
            elif sol[-3:] == ".md" and contain_cpp != "":
                with open(file_path_in + "/" + name + "/" + sol, 'r', encoding = "UTF-8") as f:
                    temp = f.read()
                with open(file_path_in + "/" + name + "/" + sol, 'w', encoding = "UTF-8") as f:
                    f.write(head_cpp)
                    f.write(temp)
                    f.write("\n\n```cpp\n")
                    f.write(contain_cpp)
                    f.write("\n\n```\n")
                    f.close()
                 
# Solution README file Rename
    for name in file_names_in:
        src = os.path.join(file_path_in + name + "/" , "README.md")
        dst = os.path.join(file_path_in + name + "/" , day + "{}.md".format(name))
        os.rename(src, dst)
