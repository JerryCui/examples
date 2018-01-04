'One way to input lines from the user: say how many.'

lines = list() 

outfile = open('sample_readlines0.txt', 'w')
n = int(input('How many lines do you want to enter? ')) 
for i in range(n): 
    line = input('Next line: ') 
    lines.append(line) 

outfile.writelines(lines)
outfile.close()

print('Your lines were:')  # check now 
for line in lines: 
    print(line) 

readfile = open('sample_readlines0.txt', 'r')
content = readfile.read()
print(content)
