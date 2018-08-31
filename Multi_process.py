import threading
import queue
import subprocess
import os
def pxj():
    #切换到切词程序的目录下面
    os.chdir("C:\\Users\\41951\\PycharmProjects\\test\\venv")
    #执行python程序
    child = subprocess.Popen("python stringcutwithline.py",shell=True)
    #等待程序执行完
    child.wait()
    #返回程序执行状态，仅供调试使用。
    temp = child.poll()
    print(temp)
while True:
    #判断文件夹中是否存在result.txt
    if os.path.exists('C:\\Users\\41951\\Desktop\\result.txt'):
        #创建子线程，处理result文件
        linux_shell = threading.Thread(target=pxj(), name="helloword")
        #子线程开启
        linux_shell.start()
        #保证子线程执行完
        linux_shell.join()
        #切换到固定的result.txt文件目录下面
        os.chdir("C:\\Users\\41951\\Desktop")
        #删除result.txt文件
        os.remove("result.txt")
    else:
        #供调试使用
        print("Waiting for the result.txt")


