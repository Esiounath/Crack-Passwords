#!coding:utf8
#!/usr/lib/python3.9
from crack import *
from color import *
import argparse
import random
import sys
import multiprocessing



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='CRACK PASSWORD')
    parser.add_argument('-f','--f',help='ENTER PATH FILE',type=str,dest='file',required=False)
    parser.add_argument('-a', '--active', help='TRUE OR FALSE  ?', type=bool, dest='words', required=False)
    args = parser.parse_args()
    index = 0
    size = 0
    cracke = Crack()
    process = []
    if args.words or args.file:
        print(color.UNDERLINE+color.BLUE+'NOTICE ENTER ($)--> Execute a ANY FILES TEXT (+)--> Loop Punctuation Characters (£)--> Loop Alphanumeric values between a and Z (*)--> Loop number range between 0 and 1000'+color.ENDC)
        print(color.UNDERLINE+color.HEADER+' IF YOU USING ANY FILES TO ATTACK IT BETTER WRITING FIRST \'$\' AND AFTER OTHER CHARACTERS'+color.ENDC)
        pattern = list(map(str, input(color.BOLD + color.FAIL + "ENTER MUTIPLES WORDS TO SELECT ATTACK : " + color.ENDC).split()))
        queue = multiprocessing.Queue()
        if args.file:
            if pattern.count('$') > 0 and args.file:
                place = pattern.index('$')
                pattern[0],pattern[place] = pattern[place],pattern[0]
                queue = multiprocessing.Queue()
                if args.file and pattern.count("$") > 0 and str(args.file) != "":
                    processe1 = multiprocessing.Process(target=cracke.word,args=(pattern,args.file,queue,Order.ASCEND,index))
                    process.append(processe1)
                    processe1.start()
                    processe2 = multiprocessing.Process(target=cracke.word, args=(pattern,args.file,queue,Order.DESCEND,index))
                    process.append(processe2)
                    processe2.start()
                    data = queue.get()
                    nofound = 0
                    if processe1.is_alive() and processe2.is_alive():
                        if data == "TROUVE" or data == "NON TROUVE":
                            print(color.BOLD+color.HEADER+"PASSWORD NOT FOUND !"+color.ENDC)
                            processe1.kill()
                            processe2.kill()
                            processe1.join()
                            processe2.join()
                            processe1.close()
                            processe2.close()
                            sys.exit(0)
            else:
                if args.file and pattern.count("$") > 0 and str(args.file) != "":
                    processe1 = multiprocessing.Process(target=cracke.word,args=(pattern,args.file,queue,Order.ASCEND,index))
                    process.append(processe1)
                    processe1.start()
                    processe2 = multiprocessing.Process(target=cracke.word, args=(pattern,args.file,queue,Order.DESCEND,index))
                    process.append(processe2)
                    processe2.start()
                    data = queue.get()
                    nofound = 0
                    if processe1.is_alive() and processe2.is_alive():
                        if data == "TROUVE" or data == "NON TROUVE":
                            Crack.time()
                            print(color.BOLD+color.HEADER+"PASSWORD NOT FOUND !"+color.ENDC)
                            processe1.kill()
                            processe2.kill()
                            processe1.join()
                            processe2.join()
                            processe1.close()
                            processe2.close()
                            sys.exit(0)

                else:
                  for i in range(len(pattern)):
                    size = size + 1
                    shuffled = random.sample(pattern, len(pattern))
                    shuffled = ''.join(shuffled)
                    print(color.BOLD+color.CYAN+'[*] ELEMENT : '+shuffled.capitalize()+' INDEX :'+str(size)+color.ENDC)
                    time.sleep(0.000001)
                    Crack.word(shuffled,args.file,queue,Order.ASCEND,index + 1)
                    """NEXT STEP IS REQUESTS TO SERVER CRACK PASSWORDS WITH REQUESTS POST TO LOGIN ANY PASSWORDS !"""
                    if size == len(pattern):
                        Crack.time()
                        sys.exit(0)
        else:
            for i in range(len(pattern)):
                size = size + 1
                shuffled = random.sample(pattern, len(pattern))
                shuffled = ''.join(shuffled)
                print(color.BOLD + color.CYAN + '[*] ELEMENT : ' + shuffled.capitalize() + ' INDEX :' + str(
                    size) + color.ENDC)
                time.sleep(0.000001)
                Crack.word(shuffled, args.file, queue, Order.ASCEND, index + 1)
                """NEXT STEP IS REQUESTS TO SERVER CRACK PASSWORDS WITH REQUESTS POST TO LOGIN ANY PASSWORDS !"""
                if size == len(pattern):
                    Crack.time()
                    sys.exit(0)
    else:
            print(color.BOLD+color.FAIL+'YOU DO ENTER 2 NAME FILE --F FOR FILE AND -w FOR ANY WORD !! '+color.ENDC)
            sys.exit(0)