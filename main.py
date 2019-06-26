# -*- coding: utf-8 -*-
from hashlib import sha256
from blockchain import Blockchain
from block import Block
from random import randint

blockchain = Blockchain()
DEBUG = False

def debug(str_print):
    if(DEBUG):
        print(str_print)

def hash(data):
    txt = ""
    for value in data["data"].values():
        txt = txt + ""+ str(value)
    txt = txt + ""+  str( data["time"])
    txt = txt + ""+  str( data["prev"])
    return sha256(txt).hexdigest()

def validate():
    lastHash = blockchain.getLastHash()
    booCheck = True
    for i in range(0,len(blockchain.getBlockChain().items())):
        block = blockchain.getBlock(lastHash)
        lastHash = block.getPrev()
        blockHash = block.getValueHash()
        dataRaw = block.getDataRaw()
        if(hash(dataRaw) in blockHash and blockHash in hash(dataRaw)):
            prevBlock = Block()
            if(block.getPrev() == ""):
                debug("Genesys Block")
                break
            else:
                prevBlock = blockchain.getBlock(block.getPrev())
            prevBlockHash = prevBlock.getValueHash()
            prevDataRaw = prevBlock.getDataRaw()
            if(hash(prevDataRaw) in prevBlockHash and prevBlockHash in hash(prevDataRaw)):
                debug("Block - "+blockHash + "Ok\n Previous: "+lastHash+"\n")
            else:
                booCheck=False
                break
        else:
            booCheck=False
            break
    if(booCheck):
        print("\nTudo ok\n")
    else:
        print("Falha blockchain comprometida\n")

        

for i in range(0,100):
    data = {1:"maria",2:"jose",3:"joao"}
    block = Block()
    block.setData(data[randint(1, 3)],randint(1, 9))
    block.setData(data[randint(1, 3)],randint(1, 9))
    block.setData(data[randint(1, 3)],randint(1, 9))
    blockchain.addBlock(block)


while 1:
    print("A blockchain foi gerada, escolha se quer validar:")
    print("1 para validar")
    print("2 para sair")
    a = int(input("Escolha: " ))
    
    if(a==1):
        validate()
    elif(a==2):
        break
    else:
        print("\nEscolha incorreta\n")