import PySimpleGUI as sg
import actions as actions
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

def runSelectedMatches(actionLog, currentWhiteTeam, currentRedTeam, nextWhiteTeam, nextRedTeam, nameLengthLimit):

    whiteTeamName = currentWhiteTeam['Team Name']
    whiteTeamPlayerNames = currentWhiteTeam['Players']

    redTeamName = currentRedTeam['Team Name']
    redTeamPlayerNames = currentRedTeam['Players']

    # Initialize variables for tracking the match
    # fight number. Track what fight the match is on starting at 0 (1st fight) up to 5 (daihosen)
    fn = 0
    # Total number of wins the team has scored [white,red]. Used for determining the overall winner of a match
    wins = [0, 0]
    # Total number of points the team has scored [white,red]. Used for determining the overall winner of a match if tied on wins.
    totalPoints = [0, 0]

    # results array - outer array is fights. Inner array is 'white points','red points','status of fight' (notStarted, started, finished). Used to determine who won an individual fight.
    results = [[0, 0, 'started'], [0, 0, 'notStarted'], [0, 0, 'notStarted'], [0, 0, 'notStarted'],
               [0, 0, 'notStarted'], [0, 0, 'notStarted']]

    # string values of points, penalties and draws in lists for each fight. Keeps track of actual ippon etc, used in keeping the board displaying the correct info but could possibly be used for exporting a record of the match.
    redIppon = [['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', '']]
    whiteIppon = [['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', '']]
    redHansoku = ['', '', '', '', '', '']
    whiteHansoku = ['', '', '', '', '', '']
    hikiwake = ['', '', '', '', '', '']

    # board layout
    layout = l.layout(whiteTeamPlayerNames, redTeamPlayerNames, whiteIppon, whiteHansoku, hikiwake, redHansoku, redIppon, wins,
                      whiteTeamName, redTeamName, nextWhiteTeam, nextRedTeam, totalPoints, nameLengthLimit)

    # Create the Window
    window = sg.Window('Scoreboard', layout, resizable=True, finalize=True)
    # window.Finalize()
    window.Maximize()
    fs = round(window.size[1] / 17)
    l.fontResize(fs, window, len(whiteTeamPlayerNames))
    window.bind('<Configure>', "Configure")
    window.bind('<Key-q>', "b0")
    window.bind('<Key-w>', "b1")
    window.bind('<Key-e>', "b2")
    window.bind('<Key-r>', "b3")
    window.bind('<Key-t>', "b4")
    window.bind('<Key-p>', "b10")
    window.bind('<Key-o>', "b9")
    window.bind('<Key-i>', "b8")
    window.bind('<Key-u>', "b7")
    window.bind('<Key-y>', "b6")
    window.bind('<Delete>', "undo")
    window.bind('<BackSpace>', "undo")
    window.bind('<Return>', "b5")

    # fs = round(window.size[1]/20)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        print(actionLog)
        # if event == "Configure":
        # fs = round(window.size[1]/17)
        # l.fontResize(fs, window)
        if event == 'b5':
            fn, nextAction = actions.nextFight(actionLog, window, results, hikiwake, wins, totalPoints, fn, whiteTeamName,
                                               redTeamName, whiteTeamPlayerNames, redTeamPlayerNames)
            if nextAction == 'New':
                window.Close()
                # MAIN()
            elif nextAction == 'Exit':
                window.Close()
                sys.exit()

        if event == 'undo':
            lastAction = actions.undoAction(actionLog, window, whiteIppon, redIppon, totalPoints, wins, results)
            if lastAction[0] != 'error':
                exec(lastAction[0] + " = ''")
            if lastAction[2] == 'ippon':
                exec(lastAction[1] + 'Points = ' + lastAction[1] + 'Points -1')
                totalPoints[lastAction[3]] -= 1
                window[lastAction[1] + 'Sum'].Update(
                    'Wins: ' + str(wins[lastAction[3]]) + '  Points: ' + str(totalPoints[lastAction[3]]))
                results[fn][lastAction[3]] = results[fn][lastAction[3]] - 1
            if lastAction[2] == 'nextFight':
                results[fn] = 0, 0, 'notStarted'
                if lastAction[1] != 'draw':
                    wins[lastAction[3]] -= 1
                    window[lastAction[1] + 'Sum'].Update(
                        'Wins: ' + str(wins[lastAction[3]]) + '  Points: ' + str(totalPoints[lastAction[3]]))
                window['white' + str(fn)].Update(background_color='white')
                window['red' + str(fn)].Update(background_color='white')
                fn = fn - 1
                window['white' + str(fn)].Update(background_color='grey')
                window['red' + str(fn)].Update(background_color='grey')
        if event == 'b10':
            actions.updateIpponColumn('M', 'red', fn, 1, window, whiteIppon, redIppon, totalPoints, wins, results, actionLog)
        if event == 'b9':
            actions.updateIpponColumn('K', 'red', fn, 1, window, whiteIppon, redIppon, totalPoints, wins, results, actionLog)
        if event == 'b8':
            actions.updateIpponColumn('D', 'red', fn, 1, window, whiteIppon, redIppon, totalPoints, wins, results, actionLog)
        if event == 'b7':
            actions.updateIpponColumn('T', 'red', fn, 1, window, whiteIppon, redIppon, totalPoints, wins, results, actionLog)
        if event == 'b6':
            actions.addHansoku('red', 'white', fn, 0, window, whiteIppon, redIppon, totalPoints, wins, results, actionLog,
                               whiteHansoku, redHansoku)

        if event == 'b0':
            actions.updateIpponColumn('M', 'white', fn, 0, window, whiteIppon, redIppon, totalPoints, wins, results,
                                      actionLog)
        if event == 'b1':
            actions.updateIpponColumn('K', 'white', fn, 0, window, whiteIppon, redIppon, totalPoints, wins, results,
                                      actionLog)
        if event == 'b2':
            actions.updateIpponColumn('D', 'white', fn, 0, window, whiteIppon, redIppon, totalPoints, wins, results,
                                      actionLog)
        if event == 'b3':
            actions.updateIpponColumn('T', 'white', fn, 0, window, whiteIppon, redIppon, totalPoints, wins, results,
                                      actionLog)
        if event == 'b4':
            print(totalPoints)
            actions.addHansoku('white', 'red', fn, 1, window, whiteIppon, redIppon, totalPoints, wins, results, actionLog,
                               whiteHansoku, redHansoku)

        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break

    window.close()
