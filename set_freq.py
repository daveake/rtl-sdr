#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# * UDP modifications: Original Code by Olgierd Pilarczyk
# * Extended by Frederik Granna <rtlsdr@granna.de>
#
import socket, sys

if len(sys.argv) < 2:
	sys.exit(3)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("localhost", 6020))

frequency = sys.argv[1]

buf = b'\x00'
data = int(frequency)

for i in range(4):
	buf = buf + bytes([data & 0xff])
	data = data >> 8


s.send(buf)
s.close()
