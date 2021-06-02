# implementation of time based otp (totp) using sha-256
# pseudo - random

from .sha_256 import *
import time

def otpgen(len):
    currtime=time.time()
    y=str(currtime)
    o1=SHA2(y)
    z=o1.finalhashcal()
    offset=int(z[-1],16)
    taken=z[0:64-offset]
    otp=int(taken,16)%(10**len)
    return otp
