def printTable(data):
    width = []
    for x in data:
        max = 0
        for y in x:
            if max < len(y):
                max = len(y)
        width.append(max)
    
    
    for x in range(len(data[0])): 
        str = ''   
        for y in range(len(data)):
            str = str + ' ' + data[y][x]
        d = str.split()
        final = ''
        for x in range(len(width)):
            final = final + d[x].rjust(width[x]) + ' '
        print(final)
    
tableData = [['apples', 'oranges', 'cherries', 'banana'], ['Alice', 'Bob', 'Carol', 'David'],['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)
