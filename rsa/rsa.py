#asymmetric key incryption of rsa
# image encryption and text encryption

import random
import math
from .random_prime_generator import retPrime,mypow
from .rsa_math import modinv
import cv2

class rsa():
    def __init__(self,length):
        self.length=int(length)      ##length is binary
        self.isset=True
        self.findPrimes()
        self.isIncryptedString=False
        self.isIncryptedImage=False
        self.n=self.p*self.q
        self.phin=(self.p-1)*(self.q-1)
        self.e=10
        while math.gcd(self.e,self.n)!=1 or math.gcd(self.e,self.phin)!=1:
            self.e=random.randint(2,(self.phin-1))
        self.d=modinv(self.e,self.phin)
        self.publicKey={
            "n":self.n,
            "e":self.e
        }
        self.__privateKey={
            "n":self.n,
            "d":self.d
        }

    def findPrimes(self):
        self.p=retPrime(self.length,self.isset)
        assert(self.length > 3)
        self.q=self.p
        while self.q==self.p:
            self.q=retPrime(self.length,self.isset)

    def showimg(self):
        if not self.isIncryptedImage:
            print("Image not inputted")
            return
        cv2.imshow('image',self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


    def encryptimage(self,path):
        self.img=cv2.imread(path)
        self.isIncryptedImage=True
        row,col=self.img.shape[0],self.img.shape[1]
        self.store=[[0 for x in range(col+10)]for y in range (row+10)]
        for i in range(row):
            for j in range(col):
                r,g,b=self.img[i,j]
                c1,c2,c3=int(r),int(g),int(b)
                c1=mypow(c1,self.e,self.n)
                c2=mypow(c2,self.e,self.n)
                c3=mypow(c3,self.e,self.n)
                self.store[i][j]=[c1,c2,c3]
                c1%=256
                c2%=256
                c3%=256
                self.img[i,j]=[c1,c2,c3]
        cv2.imwrite("encryptphoto.jpg",self.img)

    def decryptimage(self):
        if not self.isIncryptedImage:
            print("not encrypted yet")
            return
        row,col=self.img.shape[0],self.img.shape[1]
        for i in range(row):
            for j in range(col):
                r,g,b=self.store[i][j]
                r=mypow(r,self.d,self.n)
                g=mypow(g,self.d,self.n)
                b=mypow(b,self.d,self.n)
                r%=256
                g%=256
                b%=256
                self.img[i,j]=[r,g,b]
        cv2.imwrite("decryptphoto.jpg",self.img)
                

    def convstringtoint(self,data):
        res=0
        hash=[]
        for x in data:
            res=res*100
            if x==" ":
                res+=99
                hash.append(3)
                continue
            if(x.isnumeric()):
                res+=int(x)
                hash.append(2)
                continue
            res+=(ord(x.lower())-97+1)
            if x.lower()!=x:
                hash.append(1)
            else:
                hash.append(0)
        return res,hash

    def encryptstring(self,data):
        self.isIncrypted=True
        self.lenghtBits=(self.length*math.log(2,10))//2
        self.lenghtBits=math.floor(self.lenghtBits)
        self.lenghtBits=int(self.lenghtBits)
        self.hash=[]
        self.ind=[]
        for i in range(0,len(data),self.lenghtBits):
            lb=i
            ub=min(len(data),i+self.lenghtBits)
            ndata=data[lb:ub]
            tintd,tis=self.convstringtoint(ndata)
            self.hash.append(tis)
            self.ind.append(tintd)
        self.incrypted=[]
        for x in self.ind:
            self.incrypted.append(mypow(x,self.e,self.n))
        self.outstrincrypt=""
        lst=0
        for x in self.incrypted:
            y=str(x)
            for i in y:
                if lst==43:
                    lst=0
                    self.outstrincrypt+="\n"
                self.outstrincrypt+=i
                lst+=1
    
    def revOp(self,hashn,indn):
        now=""
        while indn>0:
            yy=int(indn%100)
            indn=indn//100
            lst=hashn.pop()
            if yy==99:
                now+=" "
                continue
            if lst==0:
                now+=chr(yy+97-1)
            elif lst==1:
                now+=chr(yy+97-1).upper()
            else:
                now+=str(yy)
        return now

    def decryptstring(self):
        if not self.isIncrypted:
            print("Not yet incrypted")
            return
        self.findata=""
        for i in range(0,len(self.incrypted)):
            decrypted=mypow(self.incrypted[i],self.d,self.n)
            self.findata+=self.revOp(self.hash[i],decrypted)[::-1]

        
