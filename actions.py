import PySimpleGUI as sg

def updateIpponColumn(symbol,colour,fn,colourIndex,window,whiteIppon,redIppon,totalPoints,wins,results,actionLog):
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
    window[colour + 'Sum'].Update('Wins: ' + str(wins[colourIndex]) + '  Points: ' + str(totalPoints[colourIndex]))
    if results[fn][0] == 2:
        print('Next Fight')
        window['b5'].click()
    if results[fn][1] == 2:
        print('Next Fight')
        window['b5'].click()
    

def addHansoku(colour1,colour2,fn,colourIndex,window,whiteIppon,redIppon,totalPoints,wins,results,actionLog,whiteHansoku,redHansoku):
    print(totalPoints)
    if results[fn][0] == 2:
        return
    if results[fn][1] == 2:
        return
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
        updateIpponColumn('H',colour2,fn,colourIndex,window,whiteIppon,redIppon,totalPoints,wins,results,actionLog)
    #return points

def undoAction(actionLog,window,whiteIppon,redIppon,totalPoints,wins,results):
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

def nextFight(actionLog,window,results,hikiwake,wins,totalPoints,fn,currentWhiteTeam,currentRedTeam,whiteNames,redNames):
    print(fn)
    nextAction = 'none'
    results[fn][2] = 'finished'
    actionLog.append('hikiwake[' +str(fn) + ']')
    if results[fn][1] == results[fn][0]:
        hikiwake[fn] = 'X'
        window['hikiwake[' +str(fn) + ']'].Update('X')
        actionLog.append('draw')
    elif results[fn][1] > results[fn][0]:
        wins[1]+=1
        window['redSum'].Update('Wins: ' + str(wins[1]) + '  Points: ' + str(totalPoints[1]))
        actionLog.append('red')
    elif results[fn][1] < results[fn][0]:
        wins[0]+=1
        window['whiteSum'].Update('Wins: ' + str(wins[0]) + '  Points: ' + str(totalPoints[0]))
        actionLog.append('white')
    actionLog.append('nextFight')
    if fn < 4:
        window['white'+str(fn)].Update(background_color='white')
        window['red'+str(fn)].Update(background_color='white')
        fn = fn + 1
        window['white'+str(fn)].Update(background_color='grey')
        window['red'+str(fn)].Update(background_color='grey')
    elif fn == 4:
        window['white'+str(fn)].Update(background_color='white')
        window['red'+str(fn)].Update(background_color='white')
        if wins[1] > wins[0]:
            window['victor'].Update('Victor: ' + currentRedTeam)
            if sg.popup_yes_no('Next Match?',modal=True) == 'Yes':
                nextAction = 'New'
            else:
                nextAction = 'Exit'
        elif wins[0] > wins[1]:
            window['victor'].Update('Victor: ' + currentWhiteTeam)
            if sg.popup_yes_no('Next Match?',modal=True) == 'Yes':
                nextAction = 'New'
            else:
                nextAction = 'Exit'
        elif totalPoints[1] > totalPoints[0]:
            window['victor'].Update('Victor: ' + currentRedTeam)
            if sg.popup_yes_no('Next Match?',modal=True) == 'Yes':
                nextAction = 'New'
            else:
                nextAction = 'Exit'
        elif totalPoints[0] > totalPoints[1]:
            window['victor'].Update('Victor: ' + currentWhiteTeam)
            if sg.popup_yes_no('Next Match?',modal=True) == 'Yes':
                nextAction = 'New'
            else:
                nextAction = 'Exit'
        else:
            daihosen = sg.popup_yes_no('Daihosen?',title='Daihosen?',modal=True,)
            if daihosen == 'Yes':
                fn = 5
                window['victor'].Update('Daihosen')
                whiteD = selectPlayer('Select ' + currentWhiteTeam + ' representative', whiteNames,window)[0]
                redD = selectPlayer('Select ' + currentRedTeam + ' representative', redNames,window)[0]
                window['white5'].Update('D')
                window['whiteNames[5]'].Update(whiteD)
                window['redNames[5]'].Update(redD)
                window['red5'].Update('D')
                
            else:
                window['victor'].Update('Draw')
                if sg.popup_yes_no('Next Match?',modal=True) == 'Yes':
                    nextAction = 'New'
                    
                else:
                    nextAction = 'Exit'
    elif fn == 5:
        if wins[1] > wins[0]:
            window['victor'].Update('Victor: ' + currentRedTeam)
            if sg.popup_yes_no('Next Match?',modal=True) == 'Yes':
                nextAction = 'New'
            else:
                nextAction = 'Exit'
        elif wins[0] > wins[1]:
            window['victor'].Update('Victor: ' + currentWhiteTeam)
            if sg.popup_yes_no('Next Match?',modal=True) == 'Yes':
                nextAction = 'New'
            else:
                nextAction = 'Exit'
    return fn, nextAction

def selectPlayer(text, data,window):

    layout = [
        [sg.Text(text)],
        [sg.Listbox(data, size=(20,5), key='SELECTED')],
        [sg.Button('OK')],
    ]
    
    window = sg.Window('POPUP', layout).Finalize()
    
    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'OK':
            break
        else:
            print('OVER')

    window.close()

    print('[GUI_POPUP] event:', event)
    print('[GUI_POPUP] values:', values)

    if values and values['SELECTED']:
        return values['SELECTED']    
