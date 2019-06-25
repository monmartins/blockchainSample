# -*- coding: utf-8 -*-
from hashlib import sha256
from time import time
class Block:
    def __init__(self):
        self.data = {"joao":0, "jose":0, "maria":0}
        self.prev = ""
        self.time = time()
        self.value_hash = self.generateHash()
    def getDataRaw(self):
        return {"data":self.data,"prev":self.prev,"time":self.time,"value_hash":self.value_hash}
    def generateHash(self):
        txt = ""
        for value in self.data.values():
            txt = txt + ""+ str(value)
        txt = txt + ""+  str( self.time)
        txt = txt + ""+  str( self.prev)
        
        return sha256(txt).hexdigest()
    def setPrev(self,prev):
        self.prev=prev
        self.update()

    def getPrev(self):
        return self.prev
    def getValueHash(self):
        return self.value_hash
    def update(self):
        self.value_hash = self.generateHash()
    def getData(self):
        txt = ""
        for key, value in self.data.items():
            txt = txt +""+str(key) + ":"+ str(value)+ ","
        txt = txt[:-1]
        txt = txt + " -- time: "+  str( self.time)
        txt = txt + " -- previous: "+  str( self.prev)
        return txt

    def setData(self,key,value):
        self.data[key] = value
        self.update()

