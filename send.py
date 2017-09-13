#!/usr/bin/env python
import sys
import socket
from debug import *


SERVER_IP = ("raspberrypi", 10000)

def StockGetArtInfo(IDToChange, Var):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect(SERVER_IP)
	data = "StockGetArtInfo(zKz)" + str(IDToChange) + "(zkz)" + str(Var)

	Debug("Send " + str(data))
	data = data.encode()
	sock.sendto(data, SERVER_IP)
	data = sock.recv(2048)
	Debug("Get " + str(data.decode()))
	sock.close()
	return data.decode()

def StockSetArtInfo(IDToChange, VarName, Var):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect(SERVER_IP)
	data = "StockSetArtInfo(zKz)" + str(IDToChange) + "(zkz)" + str(VarName) + "(zkz)" + str(Var)

	Debug("Send " + str(data))
	data = data.encode()
	sock.sendto(data, SERVER_IP)
	data = sock.recv(2048)
	Debug("Get " + str(data.decode()))
	sock.close()
	return data.decode()

def GetStockZahl():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect(SERVER_IP)
	data = "GetStockZahl"

	Debug("Send " + str(data))
	data = data.encode()
	sock.sendto(data, SERVER_IP)
	data = sock.recv(2048)
	Debug("Get " + str(data.decode()))
	sock.close()
	return data.decode()

	

def SendeChangeAnzahl(bcode, anzahl):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect(SERVER_IP)
	Debug("Bcode " + str(bcode))
	Debug("Anzahl " + str(anzahl))
	
	data = "ChangeStock(zKz)" + str(bcode) + "(zkz)" + str(anzahl)

	Debug("Send " + str(data))
	data = data.encode()
	sock.sendto(data, SERVER_IP)
	data = sock.recv(2048)
	Debug("Get " + str(data.decode()))
	sock.close()
	return data.decode()
	

def SendeSucheStock(bcode, barcode, artikel, ort):
	#bcode = int(bcode); barcode = str(barcode); artikel = str(artikel);
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect(SERVER_IP)
	Debug("Bcode " + str(bcode))
	Debug("Barcode " + str(barcode))
	Debug("Artikel " + str(artikel))
	Debug("Ort " + str(ort))
	
	data = "SearchStock(zKz)" + str(bcode) + "(zkz)" + str(barcode) + "(zkz)" + str(artikel) + "(zkz)" + str(ort)

	Debug("Send " + str(data))
	data = data.encode()
	sock.sendto(data, SERVER_IP)
	data = sock.recv(2048)
	Debug("Get " + str(data.decode()))
	sock.close()
	return data.decode()
	
	

