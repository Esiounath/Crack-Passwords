#!coding:utf8
#!/usr/lib/python3.9
import random
import requests
import string
import hashlib
import sys
from color import *
import time
from operator import length_hint
class Crack:
    debut = time.time()
    @staticmethod
    def time():
        print(color.BOLD+color.GREEN+'TIME '+str(time.time() - Crack.debut)+'s time elasped'+color.ENDC)

    @staticmethod
    def word(pattern,file,queue,order,_index=0):
        # Open the file in read mode
        MIN = string.ascii_lowercase
        NUMBER = string.digits
        ALPHANUM = string.hexdigits
        PUCTUATION = string.punctuation
        if _index < len(pattern):
            if pattern[_index] in MIN + PUCTUATION + NUMBER:
                Crack.word(pattern,file,queue,order,_index + 1)
                """NEXT STEP IS REQUESTS TO SERVER CRACK PASSWORDS WITH REQUESTS POST TO LOGIN ANY PASSWORDS !"""

            if "£" == pattern[_index]:
                found = True
                size = 0
                if order == Order.ASCEND :
                    ALPHANUM = ALPHANUM[::-1]
                else:
                    ALPHANUM = string.hexdigits
                for c in ALPHANUM:
                    size = size + 1
                    pattern = ''.join(pattern)
                    p = str(pattern.replace("£", c))
                    currhash = hashlib.sha256(p.encode("utf8")).hexdigest()
                    print(
                        color.BOLD + color.WARNING + "[*] TEST DE : " + p + " HASH : (" + currhash + ")" + str(
                            size + 1) + " WORDS " + color.ENDC)
                    """NEXT STEP IS REQUESTS TO SERVER CRACK PASSWORDS WITH REQUESTS POST TO LOGIN ANY PASSWORDS !"""
                    time.sleep(0.00000001)
                    Crack.word(p,file,queue,order, _index + 1)
                if not found:
                    queue.put("NON TROUVE")
                    sys.exit(0)

            if "+" == pattern[_index]:
                found = True
                size = 0
                if order == Order.ASCEND :
                    PUCTUATION = PUCTUATION[::-1]
                else:
                    PUCTUATION = string.punctuation
                for c in PUCTUATION:
                    size = size + 1
                    pattern = ''.join(pattern)
                    p = str(pattern.replace("+", c))
                    currhash = hashlib.sha256(p.encode("utf8")).hexdigest()
                    print(
                        color.BOLD + color.WARNING + "[*] TEST DE : " + p + " HASH : (" + currhash + ")" + str(
                            size + 1) + " WORDS " + color.ENDC)
                    time.sleep(0.00000001)
                    Crack.word(p,file,queue,order, _index + 1)
                     """NEXT STEP IS REQUESTS TO SERVER CRACK PASSWORDS WITH REQUESTS POST TO LOGIN ANY PASSWORDS !"""
                if not found:
                    queue.put("NON TROUVE")
                    sys.exit(0)
            try:
                if "$" == pattern[_index] and len(str(file)) > 0:
                    found = True
                    with open(file,"r") as f1:
                        if order == Order.ASCEND:
                            f1 = list(f1.readlines())
                            f1 = random.sample(f1,len(f1))
                            size = 0
                        else:
                            f1 = reversed(list(f1.readlines()))
                            size = 0
                        for f in f1:
                            f = f.strip()
                            size = size + 1
                            pattern = ''.join(pattern)
                            pattern.strip()
                            p = pattern.replace("$", f,1)
                            p.capitalize()
                            currhash = hashlib.sha256(p.encode("utf8")).hexdigest()
                            print(color.BOLD + "[*] TEST DE :" +
                                p.capitalize() + "(" + currhash + ")" + 'INDEX : ' + str(size))
                            Crack.word(p,file,queue,order, _index + 1)
                            """NEXT STEP IS REQUESTS TO SERVER CRACK PASSWORDS WITH REQUESTS POST TO LOGIN ANY PASSWORDS !"""
                            if size == length_hint(f1):
                                Crack.time()
                                queue.put("NON TROUVE")
                                sys.exit(0)
                        if not found:
                            queue.put("NON TROUVE")
                            sys.exit(0)
            except FileNotFoundError as file:
                        print(' FILE NOT FOUND !'+str(file))
                        queue.put("NON TROUVE")
                        sys.exit(0)
            except Exception:
                print(' ERROR FILE ! ')
                queue.put("NON TROUVE")
                sys.exit(0)

            if "*" == pattern[_index]:
                found = True
                size = 0
                for f in str(range(1000)):
                        size = size + 1
                        pattern = ''.join(pattern)
                        p = pattern.replace("*",f)
                        currhash = hashlib.sha256(p.encode("utf8")).hexdigest()
                        print(color.BOLD + "[*] TEST DE :" +
                            p + "(" + currhash + ")" + 'INDEX : ' + str(size))
                        Crack.word(p,file,queue,order, _index + 1)
                        """NEXT STEP IS REQUESTS TO SERVER CRACK PASSWORDS WITH REQUESTS POST TO LOGIN ANY PASSWORDS !"""
                        if f == 1000:
                            Crack.time()
                            queue.put("NON TROUVE")
                            sys.exit(0)
                if not found:
                        Crack.time()
                        queue.put("NON TROUVE")
                        sys.exit(0)

