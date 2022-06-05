import PySimpleGUI as sg
def layout(whiteNames,redNames,whiteIppon,whiteHansoku,hikiwake,redHansoku,redIppon,wins,currentWhiteTeam,currentRedTeam,nextWhiteTeam,nextRedTeam,totalPoints,nl):
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
                    ,[sg.Text('Wins: ' + str(wins[0]) + '  Points: ' + str(totalPoints[0]), key='whiteSum')
                      ,sg.Push()
                      ,sg.Text('Wins: ' + str(wins[1]) + '  Points: ' + str(totalPoints[1]), key='redSum')]
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
    return layout

def fontResize(fs, window):
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
