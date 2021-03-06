#!/usr/bin/env python3
import sys
import socket
#from libs.BlueFunc import *
#from libs.debug import *

def IDToBarcode(ID):
	print("ID To Barcode")
	Barcode = "123456" + str(ID)
	if len(str(ID)) == 6:
		print("Barcode " + str(Barcode))
		Sum = 0
		for x in range(1, 13):
			if int(x/2) == x/2:
				print("a = 3")
				a=3
			else:
				print("a = 1")
				a=1
			Sum = Sum + int(Barcode[-13+x])*a
		print("Sum = " + str(Sum) + " + " + str(Barcode[-13+x]) + " * " + str(x))
		print("Sum " + str(Sum))
		End = str(10 - int(str(Sum)[-1]))[-1]
		Barcode = str(Barcode) + str(End)
		print("Barcode " + str(Barcode) )
	return str(Barcode)
	
IDToBarcode("654321")

def PrintBarcode(IP, ID, Barcode, Name, Price):
	print("Barcode")
	TCP_IP = "10.0.0.22"#ZBR5581684 ##### ZBR7681522
	TCP_PORT = 9100

	ID = str(ID)
	Barcode = str(Barcode)
	Name = str(Name)
	Price = str(Price) + " Euro"

	BarcodePos = "^FO140,5^BY2"
	BarcodeType = "^BEI,30,N,N"
	BarcodeString = "^FD" + Barcode + "^FS"
	Barcode = BarcodePos + BarcodeType + BarcodeString

	IDPos = "^FO120,30^BY2"
	IDText = "^ACB^FD" + ID + "^FS" # ^AOB^FD
	ID = IDPos + IDText

	MaxStringLen = 15
	if len(Name) < MaxStringLen:
		NamePos = "^FO150,70^BY1"
		NameText = "^ACN^FD" + Name + "^FS"
		Name = NamePos + NameText
	else:
		Name1 = Name[0:MaxStringLen]
		Name2 = Name[MaxStringLen:len(Name)]
		NamePos1 = "^FO150,70^BY1"
		NameText1 = "^ACN^FD" + Name1 + "^FS"
		NamePos2 = "^FO150,100^BY1"
		NameText2 = "^ACN^FD" + Name2 + "^FS"
		Name = NamePos1 + NameText1 + NamePos2 + NameText2
	

	PricePos = "^FO160,40^BY1"
	PriceText = "^ACN^FD" + Price + "^FS"
	Price = PricePos + PriceText

	zpl="^XA" + Barcode + ID + Name + Price + "^XZ"
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((TCP_IP, TCP_PORT))
	s.send(bytes(zpl, "utf-8"))
	s.close()


def PrintLocation(Location):
	TCP_IP = "10.0.0.22"#ZBR5581684 ##### ZBR7681522
	TCP_PORT = 9100

	Location = str(Location)

	BarcodePos = "^FO150,10^BY1"
	BarcodeType = "^B3,Y,40,N,N"
	BarcodeString = "^FD" + Location + "^FS"
	Barcode = BarcodePos + BarcodeType + BarcodeString

	StringPos = "^FO150,70^BY3"
	StringText = "^AFD^FD" + Location + "^FS"
	String = StringPos + StringText

	zpl="^XA" + Barcode + String + "^XZ"
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((TCP_IP, TCP_PORT))
	s.send(bytes(zpl, "utf-8"))
	s.close()


