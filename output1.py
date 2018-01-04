def writeintofile():
    output = open('sample.txt', 'w')
    output.write('My first output file!')
    output.close()

"""add a verify for read the written file content"""
def readfromfile():
    outfile = open('sample.txt', 'r')
    content = outfile.read()
    retvalue = outfile.close()
    print(retvalue)
    print(content)

def main():
    writeintofile()
    readfromfile()

main()

"""verify end"""
