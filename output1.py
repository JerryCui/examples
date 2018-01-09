"""file read and write ops"""
def writeintofile():
    """"write sth into a file"""
    output = open('sample.txt', 'w')
    output.write('My first output file!')
    output.close()

def readfromfile():
    """add a verify for read the written file content"""
    outfile = open('sample.txt', 'r')
    content = outfile.read()
    retvalue = outfile.close()
    print(retvalue)
    print(content)

def main():
    """invoke write and read """
    writeintofile()
    readfromfile()

main()

"""verify end"""
