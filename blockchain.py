# -*- coding: utf-8 -*-
class Blockchain:

    def __init__(self):
        self.chain = {}
        self.lastHash = ""
        
    def status(self):
        for key, value in self.chain.items():
            print("Hash --  {}: Data --- {}".format(key, value.getData()))
        print("Last HASH --- "+ self.lastHash)
    def addBlock(self, block):
        if not self.lastHash:
            block.setPrev("")
        else:
            block.setPrev(self.lastHash)
        self.lastHash=block.getValueHash()
        self.chain[block.getValueHash()] = block
    def getBlock(self,key):
        return self.chain[key]
    def setData(self,key,value):
        self.data[key] = value
    def getLastHash(self):
        return self.lastHash
    def getBlockChain(self):
        return self.chain