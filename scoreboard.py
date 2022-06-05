import PySimpleGUI as sg
import ast
import actions as a
import layout as l
import sys

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

def MAIN():
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
    #total number of  team ippon
    whitePoints = 0
    redPoints = 0
    #number of fights won
    whiteWins = 0
    redWins = 0
    totalPoints = [0,0]
    wins = [0,0]

    #results array - outer array is fights. Inner array is 'white points','red points','status of fight' (notStarted, started, finished)
    results = [[0,0,'started'],[0,0,'notStarted'],[0,0,'notStarted'],[0,0,'notStarted'],[0,0,'notStarted'],[0,0,'notStarted']]

    #string values of points, penalties and draws in lists for each fight.
    redIppon = [['',''],['',''],['',''],['',''],['',''],['','']]
    whiteIppon = [['',''],['',''],['',''],['',''],['',''],['','']]
    redHansoku = ['','','','','','']
    whiteHansoku = ['','','','','','']
    hikiwake = ['','','','','','']

    #board layout
    layout = l.layout(whiteNames,redNames,whiteIppon,whiteHansoku,hikiwake,redHansoku,redIppon,wins,currentWhiteTeam,currentRedTeam,nextWhiteTeam,nextRedTeam,totalPoints,nl)

    # Create the Window
    window = sg.Window('Scoreboard', layout, resizable=True, finalize=True)
    #window.Finalize()
    window.Maximize()
    fs = round(window.size[1]/17)
    l.fontResize(fs, window)
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
        #if event == "Configure":
            #fs = round(window.size[1]/17)
            #l.fontResize(fs, window)
        if event == 'b5':
            fn, nextAction = a.nextFight(actionLog,window,results,hikiwake,wins,totalPoints,fn,currentWhiteTeam,currentRedTeam,whiteNames,redNames)
            if nextAction == 'New':
                window.Close()
                MAIN()
            elif nextAction == 'Exit':
                window.Close()
                sys.exit()
                
        if event == 'undo':
            lastAction = a.undoAction(actionLog,window,whiteIppon,redIppon,totalPoints,wins,results)
            if lastAction[0] != 'error':
                exec(lastAction[0] + " = ''")
            if lastAction[2] == 'ippon':
                exec(lastAction[1] + 'Points = ' + lastAction[1] + 'Points -1')
                totalPoints[lastAction[3]]-=1
                window[lastAction[1] + 'Sum'].Update('Wins: ' + str(wins[lastAction[3]]) + '  Points: ' + str(totalPoints[lastAction[3]]))
                results[fn][lastAction[3]] = results[fn][lastAction[3]] - 1
            if lastAction[2] == 'nextFight':
                results[fn] = 0, 0, 'notStarted'
                if lastAction[1] != 'draw':
                    wins[lastAction[3]]-=1
                    window[lastAction[1] + 'Sum'].Update('Wins: ' + str(wins[lastAction[3]]) + '  Points: ' + str(totalPoints[lastAction[3]]))
                window['white'+str(fn)].Update(background_color='white')
                window['red'+str(fn)].Update(background_color='white')
                fn = fn - 1
                window['white'+str(fn)].Update(background_color='grey')
                window['red'+str(fn)].Update(background_color='grey')
        if event == 'b10':
            a.updateIpponColumn('M','red',fn, 1, window,whiteIppon,redIppon,totalPoints,wins,results,actionLog)
        if event == 'b9':
            a.updateIpponColumn('K','red',fn,1, window,whiteIppon,redIppon,totalPoints,wins,results,actionLog)
        if event == 'b8':
            a.updateIpponColumn('D','red',fn,1, window,whiteIppon,redIppon,totalPoints,wins,results,actionLog)
        if event == 'b7':
            a.updateIpponColumn('T','red',fn,1, window,whiteIppon,redIppon,totalPoints,wins,results,actionLog)
        if event == 'b6':
            a.addHansoku('red','white',fn,0, window,whiteIppon,redIppon,totalPoints,wins,results,actionLog,whiteHansoku,redHansoku)

        if event == 'b0':
            print('whitePoints Out of Sub: ', whitePoints)
            #print('whiteIppon: ', whiteIppon)
            #print('Results: ', results)
            a.updateIpponColumn('M','white',fn,0,window,whiteIppon,redIppon,totalPoints,wins,results,actionLog)
            print('whitePoints Out of Sub: ', whitePoints)
            print(totalPoints)
            #print('whiteIppon: ', whiteIppon)
            #print('Results: ', results)
        if event == 'b1':
            a.updateIpponColumn('K','white',fn,0, window,whiteIppon,redIppon,totalPoints,wins,results,actionLog)
        if event == 'b2':
            a.updateIpponColumn('D','white',fn,0, window,whiteIppon,redIppon,totalPoints,wins,results,actionLog)
        if event == 'b3':
            a.updateIpponColumn('T','white',fn,0, window,whiteIppon,redIppon,totalPoints,wins,results,actionLog)
        if event == 'b4':
            print(totalPoints)
            a.addHansoku('white','red',fn,1,window,whiteIppon,redIppon,totalPoints,wins,results,actionLog,whiteHansoku,redHansoku)


                
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        

    window.close()
#MAIN(  whitePoints, redPoints, 0)
MAIN()
