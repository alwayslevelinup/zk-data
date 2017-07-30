#!/usr/bin/env python
#from keybinder import *
import os
from BlueVar import *
from debug import *

def StockIt():
	for jedenLieferant in os.listdir("barcode/"):
		if os.path.exists(jedenLieferant + "-preis/"):
			print("Start Stock : " + jedenLieferant)
			for Artikel in os.listdir(jedenLieferant + "-preis/"):
				print("Artikel : " + Artikel)
				datei = jedenLieferant + "-preis/" + Artikel
				Name = BlueLoad("Name", datei)
				Anzahl = BlueLoad("Anzahl", datei)
				Anzahl = Anzahl.split(".")[0]
				PreisVKH = BlueLoad("PreisVKH", datei)
				PreisVK = BlueLoad("PreisVK", datei)
				PreisEK = BlueLoad("PreisEK", datei)
				BurkardtCode = BlueLoad("BurkardtCode", datei)
				Lieferant = BlueLoad("Lieferant", datei)
				Debug("BurkardtCode : " + str(BurkardtCode))
				if not BurkardtCode == "0": # IM STOCK
					print("Im Stock")
					BurkardtCodeChar = BurkardtCode[-3] + BurkardtCode[-2] + BurkardtCode[-1]
				else:# NICHT IM STOCK
					print("Nicht im Stock")
					while True:
						if os.path.exists("stock/AAA/" + str(BurkardtCode)):
							BurkardtCode = int(BurkardtCode) + 1
						else: break
					BurkardtCodeChar = "AAA"

				if not os.path.exists("stock/" + str(BurkardtCodeChar)): os.mkdir("stock/" + str(BurkardtCodeChar))
				stockdatei = "stock/" + str(BurkardtCodeChar) + "/" + str(BurkardtCode)
				#	Lieferant
				BlueSave("Lieferant", Lieferant, stockdatei)
				#	Name
				BlueSave("Name", Name, stockdatei)
				#	Preise
				BlueSave("PreisVKH", PreisVKH, stockdatei)
				BlueSave("PreisVK", PreisVK, stockdatei)
				BlueSave("PreisEK", PreisEK, stockdatei)
				#	Anzahl
				stockAnzahl = BlueLoad("Anzahl", stockdatei)
				if stockAnzahl == None: stockAnzahl = 0
				BlueSave("Anzahl", int(stockAnzahl) + int(Anzahl), stockdatei)	
				#	Artikel
				BlueSave("Artikel", str(Artikel), stockdatei)					
