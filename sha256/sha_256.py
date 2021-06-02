class SHA2():
    bit64=0xFFFFFFFFFFFFFFFF
    bit32=0xFFFFFFFF
    def __init__(self,data):
        self.name="sha-256"
        self.byteorder='big'
        self.toBeHashed=data
        self.binH=bytearray()
        # hash values:
        # (first 32 bits of the fractional parts of the square roots of the first 8 primes 2..19):
        self.hashes=[
            0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
            0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19
        ]

        # array of round constants:
        # first 32 bits of the fractional parts of the cube roots of the first 64 primes (2 – 311).
        self.roundConstants = [
            0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
            0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
            0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
            0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
            0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
            0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
            0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
            0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
        ]
        self.pre()
        self.makeHash()
    
    def pre(self):
        for c in self.toBeHashed:
            self.binH.append(ord(c)&0xFF)
    
    def rightshift(self,num,shift):
        return ((num>>shift)&0xFFFFFFFF)

    ## not used, made just for completeness
    def leftshift(self,num,shift):
        return (num<<shift)&0xFFFFFFFF
    
    def rightrotate(self,num,shift):
        return (num>>shift)|((num<<(32-shift))&0xFFFFFFFF)

    ## not used, made just for completeness
    def leftrotate(self,num,shift):
        return ((num<<shift)&0xFFFFFFFF)|(num<<(32-shift))

    ## not of num in 32 bits    
    def nott(self,num):
        return (((1<<32)-1)-num)

    ## sha-256 algorithm
    def makeHash(self):
        nowdata=self.binH
        firstLen=(len(nowdata)*8)&(0xFFFFFFFFFFFFFFFF)
        #append 1
        nowdata.append(0x80)
        #append remaining 0's
        while len(nowdata)%64!=(64-8):
            nowdata.append(0x00)
        #append the initial size
        nowdata += firstLen.to_bytes(8, byteorder='big')

        for i in range(0,len(nowdata),64):
            w=[]
            for j in range (i,i+63,4):
                num=(nowdata[j]<<24)+(nowdata[j+1]<<16)+(nowdata[j+2]<<8)+(nowdata[j+3])    ##making 32 bit words
                w.append(num)
            
            for j in range (48):
                w.append(0)
            
            for j in range(16,64):
                s0=(self.rightrotate(w[j-15],7))^(self.rightrotate(w[j-15],18))^(self.rightshift(w[j-15],3))
                s1=(self.rightrotate(w[j-2],17))^(self.rightrotate(w[j-2],19))^(self.rightshift(w[j-2],10))
                w[j]=w[j-16]+s0+w[j-7]+s1
                w[j]=w[j]&self.bit32

            a,b,c,d,e,f,g,h=self.hashes
            for j in range(64):
                s1=(self.rightrotate(e,6))^(self.rightrotate(e,11))^(self.rightrotate(e,25))
                ch=(e&f)^((self.nott(e))&g)
                temp1=h+s1+ch+self.roundConstants[j]+w[j]
                temp1=temp1&self.bit32
                s0=(self.rightrotate(a,2))^(self.rightrotate(a,13))^(self.rightrotate(a,22))
                temp2=s0+((a&b)^(a&c)^(b&c))
                temp2=temp2&self.bit32
                h=g
                g=f
                f=e
                e=d+temp1
                e=e&self.bit32
                d=c
                c=b
                b=a
                a=temp1+temp2
                a=a&self.bit32
            
            self.hashes[0]=self.hashes[0]+a
            self.hashes[0]=self.hashes[0]&(self.bit32)
            self.hashes[1]=self.hashes[1]+b
            self.hashes[1]=self.hashes[1]&(self.bit32)
            self.hashes[2]=self.hashes[2]+c
            self.hashes[2]=self.hashes[2]&(self.bit32)
            self.hashes[3]=self.hashes[3]+d
            self.hashes[3]=self.hashes[3]&(self.bit32)
            self.hashes[4]=self.hashes[4]+e
            self.hashes[4]=self.hashes[4]&(self.bit32)
            self.hashes[5]=self.hashes[5]+f
            self.hashes[5]=self.hashes[5]&(self.bit32)
            self.hashes[6]=self.hashes[6]+g
            self.hashes[6]=self.hashes[6]&(self.bit32)
            self.hashes[7]=self.hashes[7]+h
            self.hashes[7]=self.hashes[7]&(self.bit32)
    
    def convertToString(self,h):
        now=hex(h)
        now=now[2:]
        while len(now)!=8:
            now='0'+now
        return now

    def finalhashcal(self):
        finalHash=""
        for x in self.hashes:
            finalHash=finalHash+self.convertToString(x)
        return finalHash



