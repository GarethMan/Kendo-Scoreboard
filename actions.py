def updateIpponColumn(symbol,colour,fn,colourIndex,window,whiteIppon,redIppon,totalPoints,whiteWins,redWins,results,actionLog):
    print(colourIndex)
    print(totalPoints)
    if results[fn][0] == 2:
        return
    if results[fn][1] == 2:
        return
    if eval(colour + 'Ippon[fn][0]') == '':
        exec(colour + 'Ippon[fn][0] = "' + symbol + '"')
        window[colour + 'Ippon[' + str(fn) + '][0]'].Update(symbol)
        actionLog.append(colour + 'Ippon[' + str(fn) + '][0]')
        actionLog.append(colour)
        actionLog.append('ippon')
    elif eval(colour + 'Ippon[fn][1]') == '':
        exec(colour + 'Ippon[fn][1] = "' + symbol + '"')
        window[colour + 'Ippon[' + str(fn) + '][1]'].Update(symbol)
        actionLog.append(colour + 'Ippon[' + str(fn) + '][1]')
        actionLog.append(colour)
        actionLog.append('ippon')
    totalPoints[colourIndex]+=1
    results[fn][colourIndex]+=1
    window[colour + 'Sum'].Update('Wins: ' + str(eval(colour + 'Wins')) + '  Points: ' + str(totalPoints[colourIndex]))
    

def addHansoku(colour1,colour2,fn,colourIndex,window,whiteIppon,redIppon,totalPoints,whiteWins,redWins,results,actionLog,whiteHansoku,redHansoku):
    print(totalPoints)
    if eval(colour1 + 'Hansoku[fn]') == '':
        exec(colour1 + 'Hansoku[fn] = "▲"')
        window[colour1 + 'Hansoku[' + str(fn) + ']'].Update('▲')
        actionLog.append(colour1 + 'Hansoku[' + str(fn) + ']')
        actionLog.append(colour1)
        actionLog.append('hansoku')
        #points = eval(colour2 + 'Points')
    elif eval(colour1 + 'Hansoku[fn]') == '▲':
        exec(colour1 + 'Hansoku[fn] = ""')
        window[colour1 + 'Hansoku[' + str(fn) + ']'].Update('')
        updateIpponColumn('H',colour2,fn,colourIndex,window,whiteIppon,redIppon,totalPoints,whiteWins,redWins,results,actionLog)
    #return points

def undoAction(actionLog,window,whiteIppon,redIppon,totalPoints,whiteWins,redWins,results):
    #global actionLog
    print('undo')
    print(actionLog)
    try:
        actionType = actionLog.pop()
        print('actionType: ' + actionType)
    except:
        actionType = 'Error'
        print('actionType: ' + actionType)
    try:
        colour = actionLog.pop()
        print(colour)
    except:
        colour = 'Error'
        print(colour)
    try:
        lastAction = actionLog.pop()
        print(lastAction)
    except:
        lastAction = 'Error'
        print(lastAction)
    if colour == 'white':
        cIndex = 0
    elif colour == 'red':
        cIndex = 1
    else:
        cIndex = 99
    print(cIndex)
    
    window[lastAction].Update('')
    return lastAction, colour, actionType, cIndex
