import PySimpleGUI as sg
import ast


def fontResize(fs):
    [window[f'blank{i}'].Update(font=('arial',fs)) for i in range(0,9)]
    window['whiteName'].Update(font=('arial',fs))
    window['redName'].Update(font=('arial',fs))
    window['nextMatch'].Update(font=('arial',fs))
    window['nextWhiteTeam'].Update(font=('arial',fs))
    window['nextRedTeam'].Update(font=('arial',fs))
    window['redSum'].Update(font=('arial',fs))
    window['whiteSum'].Update(font=('arial',fs))
    window['victor'].Update(font=('arial',fs))
    [window[f'white{i}'].Update(font=('arial',fs)) for i in range(0,6)]
    [window[f'red{i}'].Update(font=('arial',fs)) for i in range(0,6)]
    [window[f'whiteNames[{i}]'].Update(font=('arial',fs)) for i in range(0,6)]
    [window[f'redNames[{i}]'].Update(font=('arial',fs)) for i in range(0,6)]
    [window[f'whiteIppon[{i}][0]'].Update(font=('arial',fs)) for i in range(0,6)]
    [window[f'whiteIppon[{i}][1]'].Update(font=('arial',fs)) for i in range(0,6)]
    [window[f'whiteHansoku[{i}]'].Update(font=('arial',fs)) for i in range(0,6)]
    [window[f'redIppon[{i}][0]'].Update(font=('arial',fs)) for i in range(0,6)]
    [window[f'redIppon[{i}][1]'].Update(font=('arial',fs)) for i in range(0,6)]
    [window[f'redHansoku[{i}]'].Update(font=('arial',fs)) for i in range(0,6)]
    [window[f'hikiwake[{i}]'].Update(font=('arial',fs)) for i in range(0,6)]
    [window[f'b{i}'].Widget.config(font=('arial',round(fs/2))) for i in range(0,11)]
    window['undo'].Widget.config(font=('Wingdings 3',round(fs/2)))
    
def updateIpponColumn(symbol,colour,fn,colourIndex):
    global actionLog
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
    points = eval(colour + 'Points') + 1
    results[fn][colourIndex] = results[fn][colourIndex] + 1
    window[colour + 'Sum'].Update('Wins: ' + str(eval(colour + 'Wins')) + '  Points: ' + str(points))
    return points

def addHansoku(colour1,colour2,fn,colourIndex):
    global actionLog
    if eval(colour1 + 'Hansoku[fn]') == '':
        exec(colour1 + 'Hansoku[fn] = "▲"')
        window[colour1 + 'Hansoku[' + str(fn) + ']'].Update('▲')
        actionLog.append(colour1 + 'Hansoku[' + str(fn) + ']')
        actionLog.append(colour1)
        actionLog.append('hansoku')
        points = eval(colour2 + 'Points')
    elif eval(colour1 + 'Hansoku[fn]') == '▲':
        exec(colour1 + 'Hansoku[fn] = ""')
        window[colour1 + 'Hansoku[' + str(fn) + ']'].Update('')
        points = updateIpponColumn('H',colour2,fn,colourIndex)
    return points

def undoAction():
    global actionLog
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

def selectPlayer(text, data):

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

def inputTeam(colour, nl, playersVisible):
    layout = [
        [sg.Text('Input ' + colour + ' team'), sg.Push(), sg.FileBrowse('Import', target='file', key='import', file_types=(('Text Files', '*.txt'), )),sg.Input(key='file', enable_events=True, visible=False)]
        ,[sg.Text('')]
        ,[sg.Push(),sg.Text('Team Name'), sg.Input('', size=(20, 1), key='teamName')]
        ,[sg.Push(),sg.Text('Player 1', visible=playersVisible), sg.Input('', size=(20, 1), key='p1', visible=playersVisible)]
        ,[sg.Push(),sg.Text('2', visible=playersVisible), sg.Input('', size=(20, 1), key='p2', visible=playersVisible)]
        ,[sg.Push(),sg.Text('3', visible=playersVisible), sg.Input('', size=(20, 1), key='p3', visible=playersVisible)]
        ,[sg.Push(),sg.Text('4', visible=playersVisible), sg.Input('', size=(20, 1), key='p4', visible=playersVisible)]
        ,[sg.Push(),sg.Text('5', visible=playersVisible), sg.Input('', size=(20, 1), key='p5', visible=playersVisible)]
        ,[sg.Button('OK')]
        ]
    window = sg.Window('White Team', layout).Finalize()
    while True:
        event, values = window.read()
        print(event)
        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'OK':
            teamName = values['teamName'][:nl]
            players = [values['p1'][:nl],values['p2'][:nl],values['p3'][:nl],values['p4'][:nl],values['p5'][:nl]]
            window.close()
            return teamName, players
            break
        elif event == 'file':
            with open(values['file'], 'r') as file:
                data = file.read().rstrip()
                data = ast.literal_eval(data)
                teamName = data[0]
                players = data[1]
                print(teamName)
                print(players)
                window['teamName'].Update(teamName)
                window['p1'].Update(players[0])
                window['p2'].Update(players[1])
                window['p3'].Update(players[2])
                window['p4'].Update(players[3])
                window['p5'].Update(players[4])
        else:
            print('OVER')
    window.close()

#look and feel
scoreboard = {'BACKGROUND': 'white',
                'TEXT': 'black',
                'INPUT': 'white',
                'TEXT_INPUT': 'black',
                'SCROLL': '#c7e78b',
                'BUTTON': ('black', 'white'),
                'PROGRESS': ('#01826B', '#D0D0D0'),
                'BORDER': 1,
                'SLIDER_DEPTH': 0,
                'PROGRESS_DEPTH': 0}
sg.theme_add_new('scoreboard', scoreboard)
sg.theme('scoreboard')
sg.set_options(element_padding=(0,0))


#Initialize a list that tracks actions (e.g awarding a point). Used for the undo action.   
actionLog = ['started']

#Set max character width of the names column
#nl = len(max(['name'] + whiteNames + redNames + [currentWhiteTeam] + [currentRedTeam], key=len))
nl = 11
#initial font size variable
fs = 10

#Team input
whiteTeam = inputTeam('white', nl, True)
redTeam = inputTeam('red', nl, True)

#get the player names
whiteNames = whiteTeam[1]
redNames = redTeam[1]

#get the team names
currentWhiteTeam = whiteTeam[0]
nextWhiteTeam =  inputTeam('next white', nl, False)[0]
currentRedTeam = redTeam[0]
nextRedTeam = inputTeam('next red', nl, False)[0]

#Initialize variables for tracking the match
#fight number
fn = 0
#ip = 0
#total number of  team ippon
whitePoints = 0
redPoints = 0
#number of fights won
whiteWins = 0
redWins = 0

#results array - outer array is fights. Inner array is 'white points','red points','status of fight' (notStarted, started, finished)
results = [[0,0,'started'],[0,0,'notStarted'],[0,0,'notStarted'],[0,0,'notStarted'],[0,0,'notStarted'],[0,0,'notStarted']]

#string values of points, penalties and draws in lists for each fight.
redIppon = [['',''],['',''],['',''],['',''],['',''],['','']]
whiteIppon = [['',''],['',''],['',''],['',''],['',''],['','']]
redHansoku = ['','','','','','']
whiteHansoku = ['','','','','','']
hikiwake = ['','','','','','']


#board layout
layout = [  [sg.Text('', size=(2, 1), key='blank0')
             ,sg.VerticalSeparator()
             ,sg.Text(currentWhiteTeam, size=(nl, 1), key='whiteName')
             ,sg.Push()
             ,sg.VerticalSeparator()
             ,sg.Text('', size=(2, 1), key='blank1')
             ,sg.VerticalSeparator()
             ,sg.Text('', size=(2, 1), key='blank2')
             ,sg.VerticalSeparator()
             ,sg.Text('', size=(2, 1), key='blank3')
             ,sg.VerticalSeparator()
             ,sg.Text('', size=(2, 1), key='blank4')
             ,sg.VerticalSeparator()
             ,sg.Text('', size=(2, 1), key='blank5')
             ,sg.VerticalSeparator()
             ,sg.Text('', size=(2, 1), key='blank6')
             ,sg.VerticalSeparator()
             ,sg.Text('', size=(2, 1), key='blank7')
             ,sg.VerticalSeparator()
             ,sg.Push()
             ,sg.Text(currentRedTeam, size=(nl, 1),border_width = 0, justification = 'right', background_color='red', key='redName')
             ,sg.VerticalSeparator()
             ,sg.Text('', size=(2, 1), key='blank8')]
            ,[sg.HorizontalSeparator()]
            ,[sg.Text('1', size=(2, 1), key='white0', background_color='grey')
             ,sg.VerticalSeparator()
             ,sg.Text(whiteNames[0], size=(nl, 1), key='whiteNames[0]')
             ,sg.Push()
             ,sg.VerticalSeparator()
             ,sg.Text(whiteIppon[0][0], size=(2, 1), key='whiteIppon[0][0]')
             ,sg.VerticalSeparator()
             ,sg.Text(whiteIppon[0][1], size=(2, 1), key='whiteIppon[0][1]')
             ,sg.VerticalSeparator()
             ,sg.Text(whiteHansoku[0], size=(2, 1), key='whiteHansoku[0]')
             ,sg.VerticalSeparator()
             ,sg.Text(hikiwake[0], size=(2, 1), key='hikiwake[0]')
             ,sg.VerticalSeparator()
             ,sg.Text(redHansoku[0], size=(2, 1), key='redHansoku[0]')
             ,sg.VerticalSeparator()
             ,sg.Text(redIppon[0][1], size=(2, 1), key='redIppon[0][1]')
             ,sg.VerticalSeparator()
             ,sg.Text(redIppon[0][0], size=(2, 1), key='redIppon[0][0]')
             ,sg.VerticalSeparator()
             ,sg.Push()
             ,sg.Text(redNames[0], size=(nl, 1), justification = 'right', key='redNames[0]')
             ,sg.VerticalSeparator()
             ,sg.Text('1', size=(2, 1), key='red0', justification = 'right', background_color='grey')]
            ,[sg.HorizontalSeparator()]
            ,[sg.Text('2', size=(2, 1), key='white1')
             ,sg.VerticalSeparator()
             ,sg.Text(whiteNames[1], size=(nl, 1), key='whiteNames[1]')
             ,sg.Push()
             ,sg.VerticalSeparator()
             ,sg.Text(whiteIppon[1][0], size=(2, 1), key='whiteIppon[1][0]')
             ,sg.VerticalSeparator()
             ,sg.Text(whiteIppon[1][1], size=(2, 1), key='whiteIppon[1][1]')
             ,sg.VerticalSeparator()
             ,sg.Text(whiteHansoku[1], size=(2, 1), key='whiteHansoku[1]')
             ,sg.VerticalSeparator()
             ,sg.Text(hikiwake[1], size=(2, 1), key='hikiwake[1]')
             ,sg.VerticalSeparator()
             ,sg.Text(redHansoku[1], size=(2, 1), key='redHansoku[1]')
             ,sg.VerticalSeparator()
             ,sg.Text(redIppon[1][1], size=(2, 1), key='redIppon[1][1]')
             ,sg.VerticalSeparator()
             ,sg.Text(redIppon[1][0], size=(2, 1), key='redIppon[1][0]')
             ,sg.VerticalSeparator()
             ,sg.Push()
             ,sg.Text(redNames[1], size=(nl, 1), justification = 'right', key='redNames[1]')
             ,sg.VerticalSeparator()
             ,sg.Text('2', size=(2, 1), justification = 'right', key='red1')]
            ,[sg.HorizontalSeparator()]
            ,[sg.Text('3', size=(2, 1), key='white2')
             ,sg.VerticalSeparator()
             ,sg.Text(whiteNames[2], size=(nl, 1), key='whiteNames[2]')
             ,sg.Push()
             ,sg.VerticalSeparator()
             ,sg.Text(whiteIppon[2][0], size=(2, 1), key='whiteIppon[2][0]')
             ,sg.VerticalSeparator()
             ,sg.Text(whiteIppon[2][1], size=(2, 1), key='whiteIppon[2][1]')
             ,sg.VerticalSeparator()
             ,sg.Text(whiteHansoku[2], size=(2, 1), key='whiteHansoku[2]')
             ,sg.VerticalSeparator()
             ,sg.Text(hikiwake[2], size=(2, 1), key='hikiwake[2]')
             ,sg.VerticalSeparator()
             ,sg.Text(redHansoku[2], size=(2, 1), key='redHansoku[2]')
             ,sg.VerticalSeparator()
             ,sg.Text(redIppon[2][1], size=(2, 1), key='redIppon[2][1]')
             ,sg.VerticalSeparator()
             ,sg.Text(redIppon[2][0], size=(2, 1), key='redIppon[2][0]')
             ,sg.VerticalSeparator()
             ,sg.Push()
             ,sg.Text(redNames[2], size=(nl, 1), justification = 'right', key='redNames[2]')
             ,sg.VerticalSeparator()
             ,sg.Text('3', size=(2, 1), justification = 'right', key='red2')]
            ,[sg.HorizontalSeparator()]
            ,[sg.Text('4', size=(2, 1), key='white3')
             ,sg.VerticalSeparator()
             ,sg.Text(whiteNames[3], size=(nl, 1), key='whiteNames[3]')
             ,sg.Push()
             ,sg.VerticalSeparator()
             ,sg.Text(whiteIppon[3][0], size=(2, 1), key='whiteIppon[3][0]')
             ,sg.VerticalSeparator()
             ,sg.Text(whiteIppon[3][1], size=(2, 1), key='whiteIppon[3][1]')
             ,sg.VerticalSeparator()
             ,sg.Text(whiteHansoku[3], size=(2, 1), key='whiteHansoku[3]')
             ,sg.VerticalSeparator()
             ,sg.Text(hikiwake[3], size=(2, 1), key='hikiwake[3]')
             ,sg.VerticalSeparator()
             ,sg.Text(redHansoku[3], size=(2, 1), key='redHansoku[3]')
             ,sg.VerticalSeparator()
             ,sg.Text(redIppon[3][1], size=(2, 1), key='redIppon[3][1]')
             ,sg.VerticalSeparator()
             ,sg.Text(redIppon[3][0], size=(2, 1), key='redIppon[3][0]')
             ,sg.VerticalSeparator()
             ,sg.Push()
             ,sg.Text(redNames[3], size=(nl, 1), justification = 'right', key='redNames[3]')
             ,sg.VerticalSeparator()
             ,sg.Text('4', size=(2, 1), justification = 'right', key='red3')]
            ,[sg.HorizontalSeparator()]
            ,[sg.Text('5', size=(2, 1), key='white4')
             ,sg.VerticalSeparator()
             ,sg.Text(whiteNames[4], size=(nl, 1), key='whiteNames[4]')
             ,sg.Push()
             ,sg.VerticalSeparator()
             ,sg.Text(whiteIppon[4][0], size=(2, 1), key='whiteIppon[4][0]')
             ,sg.VerticalSeparator()
             ,sg.Text(whiteIppon[4][1], size=(2, 1), key='whiteIppon[4][1]')
             ,sg.VerticalSeparator()
             ,sg.Text(whiteHansoku[4], size=(2, 1), key='whiteHansoku[4]')
             ,sg.VerticalSeparator()
             ,sg.Text(hikiwake[4], size=(2, 1), key='hikiwake[4]')
             ,sg.VerticalSeparator()
             ,sg.Text(redHansoku[4], size=(2, 1), key='redHansoku[4]')
             ,sg.VerticalSeparator()
             ,sg.Text(redIppon[4][1], size=(2, 1), key='redIppon[4][1]')
             ,sg.VerticalSeparator()
             ,sg.Text(redIppon[4][0], size=(2, 1), key='redIppon[4][0]')
             ,sg.VerticalSeparator()
             ,sg.Push()
             ,sg.Text(redNames[4], size=(nl, 1), justification = 'right', key='redNames[4]')
             ,sg.VerticalSeparator()
             ,sg.Text('5', size=(2, 1), justification = 'right', key='red4')]
            ,[sg.HorizontalSeparator()]
            ,[sg.Text('', size=(2, 1), key='white5')
             ,sg.VerticalSeparator()
             ,sg.Text('', size=(nl, 1), key='whiteNames[5]')
             ,sg.Push()
             ,sg.VerticalSeparator()
             ,sg.Text('', size=(2, 1), key='whiteIppon[5][0]')
             ,sg.VerticalSeparator()
             ,sg.Text('', size=(2, 1), key='whiteIppon[5][1]')
             ,sg.VerticalSeparator()
             ,sg.Text('', size=(2, 1), key='whiteHansoku[5]')
             ,sg.VerticalSeparator()
             ,sg.Text('', size=(2, 1), key='hikiwake[5]')
             ,sg.VerticalSeparator()
             ,sg.Text('', size=(2, 1), key='redHansoku[5]')
             ,sg.VerticalSeparator()
             ,sg.Text('', size=(2, 1), key='redIppon[5][1]')
             ,sg.VerticalSeparator()
             ,sg.Text('', size=(2, 1), key='redIppon[5][0]')
             ,sg.VerticalSeparator()
             ,sg.Push()
             ,sg.Text('', size=(nl, 1), justification = 'right', key='redNames[5]')
             ,sg.VerticalSeparator()
             ,sg.Text('', size=(2, 1), justification = 'right', key='red5')]
            ,[sg.HorizontalSeparator()]
            ,[sg.Text('Wins: ' + str(whiteWins) + '  Points: ' + str(whitePoints), key='whiteSum')
              ,sg.Push()
              ,sg.Text('Wins: ' + str(redWins) + '  Points: ' + str(redPoints), key='redSum')]
            ,[sg.HorizontalSeparator()]
            ,[sg.Push(),sg.Text('', key='victor'),sg.Push()]
            ,[sg.Text(nextWhiteTeam, key='nextWhiteTeam')
              ,sg.Push()
              ,sg.Text('Next Match', key='nextMatch')
              ,sg.Push()
              ,sg.Text(nextRedTeam, background_color='red', justification = 'right', key='nextRedTeam')
            ]
            ,[sg.HorizontalSeparator()]
            ,[sg.Button('M', button_color=('black', 'white'), key='b0')
              ,sg.VerticalSeparator()
              ,sg.Button('K', button_color=('black', 'white'), key='b1')
              ,sg.VerticalSeparator()
              ,sg.Button('D', button_color=('black', 'white'), key='b2')
              ,sg.VerticalSeparator()
              ,sg.Button('T', button_color=('black', 'white'), key='b3')
              ,sg.VerticalSeparator()
              ,sg.Button('▲', button_color=('black', 'white'), key='b4')
              ,sg.VerticalSeparator()
              ,sg.Push()
              ,sg.VerticalSeparator()
              ,sg.Button('Next Fight', key='b5')
              ,sg.VerticalSeparator()
              ,sg.Button('Q', button_color=('black', 'white'), key='undo')
              ,sg.VerticalSeparator()
              ,sg.Push()
              ,sg.VerticalSeparator()
              ,sg.Button('▲', button_color=('black', 'white'), key='b6')
              ,sg.VerticalSeparator()
              ,sg.Button('T', button_color=('black', 'white'), key='b7')
              ,sg.VerticalSeparator()
              ,sg.Button('D', button_color=('black', 'white'), key='b8')
              ,sg.VerticalSeparator()
              ,sg.Button('K', button_color=('black', 'white'), key='b9')
              ,sg.VerticalSeparator()
              ,sg.Button('M', button_color=('black', 'white'), key='b10')
              ]
            
            ]

# Create the Window
window = sg.Window('Scoreboard', layout, resizable=True, finalize=True)
window.Maximize()
window.bind('<Configure>', "Configure")
window.bind('<Key-q>',"b0")
window.bind('<Key-w>',"b1")
window.bind('<Key-e>',"b2")
window.bind('<Key-r>',"b3")
window.bind('<Key-t>',"b4")
window.bind('<Key-p>',"b10")
window.bind('<Key-o>',"b9")
window.bind('<Key-i>',"b8")
window.bind('<Key-u>',"b7")
window.bind('<Key-y>',"b6")
window.bind('<Delete>',"undo")
window.bind('<BackSpace>',"undo")
window.bind('<Return>',"b5")


#fs = round(window.size[1]/20)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    print(actionLog)
    if event == "Configure":
        fs = round(window.size[1]/17)
        fontResize(fs)
    if event == 'b5':
##        results[fn][0] = len(whiteIppon[fn][0]+whiteIppon[fn][1])
##        results[fn][1] = len(redIppon[fn][0]+redIppon[fn][1])
        print(fn)
        results[fn][2] = 'finished'
        print(results)
        print(redWins)
        print(whiteWins)
        print(redPoints)
        print(whitePoints)
        actionLog.append('hikiwake[' +str(fn) + ']')
        if results[fn][1] == results[fn][0]:
            hikiwake[fn] = 'X'
            window['hikiwake[' +str(fn) + ']'].Update('X')
            actionLog.append('draw')
        elif results[fn][1] > results[fn][0]:
            redWins = redWins + 1
            window['redSum'].Update('Wins: ' + str(redWins) + '  Points: ' + str(redPoints))
            actionLog.append('red')
        elif results[fn][1] < results[fn][0]:
            whiteWins = whiteWins + 1
            window['whiteSum'].Update('Wins: ' + str(whiteWins) + '  Points: ' + str(whitePoints))
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
            if redWins > whiteWins:
                window['victor'].Update('Victor: ' + currentRedTeam)
            elif whiteWins > redWins:
                window['victor'].Update('Victor: ' + currentWhiteTeam)
            elif redPoints > whitePoints:
                window['victor'].Update('Victor: ' + currentRedTeam)
            elif whitePoints > redPoints:
                window['victor'].Update('Victor: ' + currentWhiteTeam)
            else:
                daihosen = sg.popup_yes_no('Daihosen?',title='Daihosen?',modal=True,)
                if daihosen == 'Yes':
                    fn = 5
                    window['victor'].Update('Daihosen')
                    whiteD = selectPlayer('Select ' + currentWhiteTeam + ' representative', whiteNames)[0]
                    redD = selectPlayer('Select ' + currentRedTeam + ' representative', redNames)[0]
                    window['white5'].Update('D')
                    window['whiteNames[5]'].Update(whiteD)
                    window['redNames[5]'].Update(redD)
                    window['red5'].Update('D')
                    
                else:
                    window['victor'].Update('Draw')
        elif fn == 5:
            if redWins > whiteWins:
                window['victor'].Update('Victor: ' + currentRedTeam)
            elif whiteWins > redWins:
                window['victor'].Update('Victor: ' + currentWhiteTeam)
            
                
            
    if event == 'undo':
        lastAction = undoAction()
        if lastAction[0] != 'error':
            exec(lastAction[0] + " = ''")
        if lastAction[2] == 'ippon':
            exec(lastAction[1] + 'Points = ' + lastAction[1] + 'Points -1')
            window[lastAction[1] + 'Sum'].Update('Wins: ' + str(eval(lastAction[1] + 'Wins')) + '  Points: ' + str(eval(lastAction[1] + 'Points')))
            results[fn][lastAction[3]] = results[fn][lastAction[3]] - 1
        if lastAction[2] == 'nextFight':
            results[fn] = 0, 0, 'notStarted'
            if lastAction[1] != 'draw':
                exec(lastAction[1] + 'Wins = ' + lastAction[1] + 'Wins -1')
                window[lastAction[1] + 'Sum'].Update('Wins: ' + str(eval(lastAction[1] + 'Wins')) + '  Points: ' + str(eval(lastAction[1] + 'Points')))
            window['white'+str(fn)].Update(background_color='white')
            window['red'+str(fn)].Update(background_color='white')
            fn = fn - 1
            window['white'+str(fn)].Update(background_color='grey')
            window['red'+str(fn)].Update(background_color='grey')
    if event == 'b10':
        redPoints = updateIpponColumn('M','red',fn)
        results[fn][1] = results[fn][1] + 1
        print (redPoints)
        print(results[fn])
    if event == 'b9':
        redPoints = updateIpponColumn('K','red',fn,1)
        #results[fn][1] = results[fn][1] + 1
    if event == 'b8':
        redPoints = updateIpponColumn('D','red',fn,1)
        #results[fn][1] = results[fn][1] + 1
    if event == 'b7':
        redPoints = updateIpponColumn('T','red',fn,1)
        #results[fn][1] = results[fn][1] + 1
    if event == 'b6':
        whitePoints = addHansoku('red','white',fn,0)

    if event == 'b0':
        whitePoints = updateIpponColumn('M','white',fn,0)
        #results[fn][0] = results[fn][0] + 1
        #print (whitePoints)
        #print(results[fn])
    if event == 'b1':
        whitePoints = updateIpponColumn('K','white',fn,0)
        #results[fn][0] = results[fn][0] + 1
    if event == 'b2':
        whitePoints = updateIpponColumn('D','white',fn,0)
        #results[fn][0] = results[fn][0] + 1
    if event == 'b3':
        whitePoints = updateIpponColumn('T','white',fn,0)
        #results[fn][0] = results[fn][0] + 1
    if event == 'b4':
        redPoints = addHansoku('white','red',fn,1)


            
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    

window.close()
