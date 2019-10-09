#------------------------------------Code for generating the table and printing it----------------------------------
    
def tablemaker(names,expenses):
    line1 = '\t'
    line1 += '\t'.join(names)
    print('------------------------------------')
    print
    print(line1)
    for i in range(0,len(names)):
        temp_line = names[i]
        temp_line += '\t'
        temp_line += '\t'.join(list(map(str,expenses[i])))
        print(temp_line)
    print('------------------------------------')
    print()