monfichier = open("passwd", 'r')

for line in monfichier:
    print(line)
    
monfichier.close()