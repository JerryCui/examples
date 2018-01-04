outFile = open('sample3.txt', 'w')
outFile.write('A revised output file!\n')
outFile.write('Write some more.\n')
outFile.close()

"""read from file and print"""
readfile = open("sample3.txt", "r")
content = readfile.read()
readfile.close()
print(content)
