#!/usr/bin/env python
import os

def GetBurkardtCode(lieferant, artikel):
	Pfad = open("barcode", "r").readlines()[0].rstrip() + lieferant + "/" + str(len(artikel)) + "/"
	if os.path.exists(Pfad + str(artikel)):
		return open(Pfad + str(artikel), "r").readlines()[0].rstrip()
	else:
		return "0"
