__author__ = 'xuqiang'
# -*- coding: UTF-8 -*-
import os
import subprocess

#从这个文件夹中找到所有的extname的文件，遍历
def findfiles(rootdir,extname):
    filenamelist = []
    for parent,dirnames,filenames in os.walk(rootdir):
        for filename in filenames:
            lists = filename.split('.') #分割出文件与文件扩展名
            file_ext = lists[-1] #取出后缀名(列表切片操作)
            if(file_ext==extname):
                print "parent is :" + parent
                print "filename is:"+ filename
                parentandnanme = [filename,parent]
                filenamelist.append(parentandnanme)
                print "the full name of the file is:" + os.path.join(parent,filename) + '\n' #输出文件路径信息
    return filenamelist

#破解
def rewritefiles(filenamelist):
    for parentandnanme in filenamelist:
        rewritefile(parentandnanme)

#破解单个文件
#原理：针对每个文件，读出文件内容写入到一个txt文件中，然后删除原文件，将txt文件重命名为原来的扩展名
def rewritefile(parentandnanme):
    filename = parentandnanme[0]
    lists = filename.split('.') #分割出文件与文件扩展名
    file_ext = lists[-1] #取出后缀名(列表切片操作)
    namenoext = lists[0]
    parent = parentandnanme[1]
    wholename = os.path.join(parent,filename)

    f = open(wholename, "r")
    newfile = open(parent + '/'+ namenoext + '.txt','w')  #一个新文件
    lines = f.readlines()
    newfile.writelines(lines)
    newfile.close()
    f.close()
    os.remove(os.path.join(parent,filename))
    #os.rename( parent + '/' + namenoext + '.txt',  parent + '/' + namenoext + '.java') #osrename无法解密
    shellrename = 'mv ' + namenoext + '.txt ' + namenoext + '.java'
    subprocess.Popen(shellrename,shell=True,cwd=parent).communicate()



def crackfiles(rootdir,ext):
    rewritefiles(findfiles(rootdir,ext))

#使用方法如下：
#rootdir = "/home/xuqiang/learning"
#extname = 'java'
#crackfiles(rootdir,extname)