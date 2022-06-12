import PySimpleGUI as sg
import ast
import scoreboard as scoreboard
import csv

def chooseInputMode():
    layout = [
        [sg.Text('Choose an input mode')],
        [sg.Push(), sg.Button('Manual'), sg.Push(),
         sg.FileBrowse('Import csv', target='file', key='import', file_types=(('CSV Files', '*.csv'),)),
         sg.Input(key='file', enable_events=True, visible=False)]
    ]

    window = sg.Window('Input Mode', layout, finalize=True)

    while True:
        event, values = window.read()
        print(event)
        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'Manual':
            window.close()
            return 0
            break
        elif event == 'file':
            with open(values['file'], 'r') as csv_file:

                teams = []

                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    if line_count > 0:

                        playerNames = {'Player 1': row[1],
                                       'Player 2': row[2],
                                       'Player 3': row[3],
                                       'Player 4': row[4],
                                       'Player 5': row[5]}

                        teams.append({'Team Name': row[0], 'Players': playerNames})

                    line_count += 1

                window.close()
                return teams
        else:
            print('OVER')
    window.close()

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
    window = sg.Window(colour.title() + ' Team', layout, finalize=True)
    print(window.get_screen_size())
    while True:
        event, values = window.read()
        print(event)
        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'OK':
            playerNames = {'Player 1': values['p1'][:nl],
                           'Player 2': values['p2'][:nl],
                           'Player 3': values['p3'][:nl],
                           'Player 4': values['p4'][:nl],
                           'Player 5': values['p5'][:nl]}

            window.close()
            return {'Team Name': values['teamName'][:nl], 'Players': playerNames}
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


def MAIN():
    # Initialize a list that tracks actions (e.g awarding a point). Used for the undo action.
    actionLog = ['started']

    # Set max character width of the names column
    # nl = len(max(['name'] + whiteNames + redNames + [currentWhiteTeam] + [currentRedTeam], key=len))
    nl = 11
    # initial font size variable
    fs = 10

    input = chooseInputMode()

    if input == 0:

        # Team input
        currentWhiteTeam = inputTeam('white', nl, True)
        currentRedTeam = inputTeam('red', nl, True)

        # get the team names
        nextWhiteTeam = inputTeam('next white', nl, False)[0]
        nextRedTeam = inputTeam('next red', nl, False)[0]

        scoreboard.runSelectedMatches(actionLog, currentWhiteTeam, currentRedTeam, nextWhiteTeam, nextRedTeam, nl)

    else:

        # Team input
        currentWhiteTeam = input[0]
        currentRedTeam = input[6]

        # get the team names
        nextWhiteTeam = input[7]
        nextRedTeam = input[4]

        scoreboard.runSelectedMatches(actionLog, currentWhiteTeam, currentRedTeam, nextWhiteTeam, nextRedTeam, nl)

MAIN()
