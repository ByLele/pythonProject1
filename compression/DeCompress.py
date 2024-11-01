#coding utf8
# -*- coding: utf-8 -*-
import os

import time
import logging
import py7zr
import zipfile
import pyzipper
logger = logging.getLogger(__file__)

def get_dirs(dir_path:str) -> list:
    dirs = []
    if not os.path.exists(dir_path):
        logger.error(f"dir path not found:{dir_path}")
    
    for item in os.listdir(dir_path):
        abs_dir_path= os.path.join(dir_path,item)
        if not os.path.isdir(abs_dir_path):
            logger.error(f"abs path not found:{abs_dir_path}")
            continue
        dirs.append(abs_dir_path)
    return dirs

def get_file(dirs:str,prefix_start:str,prefix_end:str) -> list :
    file_res = []
    if not dirs:
        logger.error("file not found")
    for dir in dirs:
        for parent,dirname,files in os.walk(dir):    
            for file in  files:
                abs_file = os.path.join(dir,file)
                if not os.path.exists(abs_file) or not abs_file.endswith(prefix_end):
                    logger.error(f"file not found:{abs_file}")
                else:
                    print(f"****{abs_file}")
                    file_res.append(abs_file)
                
    return file_res
    
def com_file_7z(files:str,com_files:str) ->None:
    with py7zr.SevenZipFile(files, 'r',password="老王爱学习") as archive:  
        archive.write(com_files)

    
def com_file_zip(files:str,com_files:str) ->None:
    # zip_file = zipfile.ZipFile(files)#文件的路径与文件名
    # zip_list = zip_file.namelist() # 得到压缩包里所有文件

    # for f in zip_list:
    #     com_files = os.path.join(com_files,f)
    #     zip_file.extract(f, com_files,pwd=bytes("老王爱学习",'utf-8')) # 循环解压文件到指定目录
    password= '老王爱学习'
    # zip_file.close() # 关闭文件，必须有，释放内存
    
    for file in files:
        g = os.path.basename(file)
        g = g.split(".zip")[0]
        com_file = os.path.join(com_files,g)
        try:
            os.mkdir(com_file)
            with pyzipper.AESZipFile(file, 'r', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as extracted_zip:
                extracted_zip.pwd= "老王爱学习".encode("gb2312")
                extracted_zip.extractall(com_file)
                extracted_zip.close()
                extracted_zip.printdir()
                print(com_file)
        except Exception  as e:
                print(e)
        
        

def com_file_zip2(files:str,com_files:str) -> None:
    with zipfile.ZipFile(files, 'r') as zip_ref:
        # 设置密码
        zip_ref.setpassword(bytes('老王爱学习', 'gbk'))
        # 解压所有文件到指定目录
        zip_ref.extractall(com_files)
        print('解压成功！')
        
    
if __name__ == "__main__":
    #print(get_dirs(dir_path="G:\Downloads\网红留学生刘玥P站付费视频125部大合集超清141G"))
    #print(get_file(dirs=["G://Downloads//网红留学生刘玥P站付费视频125部大合集超清141G"],prefix_start=None,prefix_end="zip"))
    res_files = get_file(dirs=["G://Downloads//网红留学生刘玥P站付费视频125部大合集超清141G"],prefix_start=None,prefix_end="zip")
    com_file_zip(files=res_files,com_files="G://Downloads//JuneLiu//")
    # com_file_zip(files="G://Downloads//网红留学生刘玥P站付费视频125部大合集超清141G//刘玥 汪珍珍 康爱福.zip",com_files="G://Downloads//JuneLiu//")
    # f = "G://Downloads//网红留学生刘玥P站付费视频125部大合集超清141G//刘玥 汪珍珍 康爱福.zip"
    # g = os.path.basename(f)
    # g = g.split(".zip")[0]
    # h = os.path.splitext(f)[0]
    # i = os.path.splitdrive(h)

    #print(os.path.splitext(f)[0])
    
    
    
