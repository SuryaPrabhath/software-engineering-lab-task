# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 22:38:23 2022

@author: hp
"""
#comments are added          

import socket
c=socket.socket()
c.connect(('localhost',9999))
print(c.recv(1024).decode())
