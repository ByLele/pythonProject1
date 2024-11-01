import os
# import codecs7z
import time
import py7zr
from os import walk

import py7zr
srcpath = "D:\\Download\\迅雷下载\\7z"
srcpathdudu = "D:\\Download\\迅雷下载\\嘻哈范大神DuDu收官之战\\"



save_dir = srcpath
ignore_folder = []
ignore_files = ['']



# 排除的指定文件夹
ignore_folder = ['.vscode', 'node_modules']
# 排除的任意指定文件
ignore_files = ['*.log', '*.md', '*.tmp']
# 排除指定路径下的文件(会保留相应路径下的文件夹)
ignore_path_files = ['app/*', 'log/*', 'runtime/session/*', 'runtime/config/*']

ignore_str = ''
for i in ignore_files:
    ignore_str = ignore_str + '-x!' + i + ' '

for i in ignore_folder:
    ignore_str = ignore_str + '-xr!*' + i + ' '

for i in ignore_path_files:
    ignore_str = ignore_str + '-x!' + i + ' '



def file_list(srcpath):
    # for x in os.listdir(srcpath):
    #     print(x)
    arr = [os.path.join(srcpath,x) for x in os.listdir(srcpath)]
    return arr



def compression(savedir,source_dir):
    #  ============================= 将文件压缩 ===============
    save_dir = savedir

    # 获取备份的文件夹名称
    dname = os.path.dirname(source_dir).split(os.sep)[-1]
    # 拼接文件名
    fname = dname + "@" + "DUDU" + '.7z'
    # 拼接保存文件路径
    target = save_dir + os.sep + fname
    # 拼接命令（按需要自行修改）
    ziz = "C:\\Program Files\\7-Zip\\7z.exe"
    cmd = f" \"{ziz}\" a -t7z \"{target}\" \"{source_dir}\" -mx=5 -m0=LZMA2"
    print(cmd)
    # 执行压缩
    os.system(cmd)
    time.sleep(3)
    print(source_dir, '=====>', target)

def com2():
    i = 143
    for item in file_arr:

        filename = f"D:/gez/EDC-{i}.7z"
        with py7zr.SevenZipFile(filename, 'w',password="LIFE") as archive:
            print(item)
            archive.write(item)

        print("is over")
        i = i+1
srcpath = "D:/Download/迅雷下载/推特大神EDC/v/"


if __name__ == "__main__":
    # filelist = file_list(srcpathdudu)
    # for x in filelist:
    #
    #     compression(srcpath,x)
    #com2()
    #file_arr=file_list(srcpath)
    # com2()
    # pass
    dir(py7zr)