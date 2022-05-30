import PySimpleGUI as sg

p1r = 'Gareth'
p1w = 'Dez'
p2r = 'Sarah'
p2w = 'Dave'
p3r = 'Mat'
p3w = 'Baz'
p4r = 'Ru'
p4w = 'Daniel'
p5r = 'AN Other'
p5w = 'Auther'

nl = max(['name',p1w,p1r,p2w,p2r,p3r,p3w,p4r,p4w,p5r,p5w], key=len)
redNames = [p1r,p2r,p3r,p4r,p5r]
whiteNames = [p1w,p2w,p3w,p4w,p5w]

currentWhiteTeam = 'Team 1'
nextWhiteTeam = 'Team 3'
currentRedTeam = 'Team 2'
nextRedTeam = 'Team 4'

fs = 10

fn = 0
ip = 0
wp = 0
rp = 0
ww = 0
rw = 0

redIppon = [['',''],['',''],['',''],['',''],['','']]
whiteIppon = [['',''],['',''],['',''],['',''],['','']]
redHansoku = ['','','','','']
whiteHansoku = ['','','','','']
hikiwake = ['','','','','']

scoreboard = {'BACKGROUND': 'white',
                'TEXT': 'black',
                'INPUT': 'white',
                'TEXT_INPUT': 'black',
                'SCROLL': '#c7e78b',
                'BUTTON': ('black', 'white'),
                'PROGRESS': ('#01826B', '#D0D0D0'),
                'BORDER': 0,
                'SLIDER_DEPTH': 0,
                'PROGRESS_DEPTH': 0}
sg.theme_add_new('scoreboard', scoreboard)
sg.theme('scoreboard')
sg.set_options(element_padding=(0,0))     
def border(elem):
    return sg.Frame('', [[elem]])
layout = [  [sg.Text('', size=(2, 1), key='blank0')
             ,sg.VerticalSeparator()
             ,sg.Text(currentWhiteTeam, size=(len(nl), 1), key='whiteName')
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
             ,sg.Text(currentRedTeam, size=(len(nl), 1),border_width = 0, background_color='red', key='redName')
             ,sg.VerticalSeparator()
             ,sg.Text('', size=(2, 1), key='blank8')]
            ,[sg.HorizontalSeparator()]
            ,[sg.Text('1', size=(2, 1), key='white0', background_color='grey')
             ,sg.VerticalSeparator()
             ,sg.Text(whiteNames[0], size=(len(nl), 1), key='whiteNames[0]')
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
             ,sg.Text(redNames[0], size=(len(nl), 1), key='redNames[0]')
             ,sg.VerticalSeparator()
             ,sg.Text('1', size=(2, 1), key='red0', background_color='grey')]
            ,[sg.HorizontalSeparator()]
            ,[sg.Text('2', size=(2, 1), key='white1')
             ,sg.VerticalSeparator()
             ,sg.Text(whiteNames[1], size=(len(nl), 1), key='whiteNames[1]')
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
             ,sg.Text(redNames[1], size=(len(nl), 1), key='redNames[1]')
             ,sg.VerticalSeparator()
             ,sg.Text('2', size=(2, 1), key='red1')]
            ,[sg.HorizontalSeparator()]
            ,[sg.Text('3', size=(2, 1), key='white2')
             ,sg.VerticalSeparator()
             ,sg.Text(whiteNames[2], size=(len(nl), 1), key='whiteNames[2]')
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
             ,sg.Text(redNames[2], size=(len(nl), 1), key='redNames[2]')
             ,sg.VerticalSeparator()
             ,sg.Text('3', size=(2, 1), key='red2')]
            ,[sg.HorizontalSeparator()]
            ,[sg.Text('4', size=(2, 1), key='white3')
             ,sg.VerticalSeparator()
             ,sg.Text(whiteNames[3], size=(len(nl), 1), key='whiteNames[3]')
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
             ,sg.Text(redNames[3], size=(len(nl), 1), key='redNames[3]')
             ,sg.VerticalSeparator()
             ,sg.Text('4', size=(2, 1), key='red3')]
            ,[sg.HorizontalSeparator()]
            ,[sg.Text('5', size=(2, 1), key='white4')
             ,sg.VerticalSeparator()
             ,sg.Text(whiteNames[4], size=(len(nl), 1), key='whiteNames[4]')
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
             ,sg.Text(redNames[4], size=(len(nl), 1), key='redNames[4]')
             ,sg.VerticalSeparator()
             ,sg.Text('5', size=(2, 1), font=('arial',fs), key='red4')]
            ,[sg.HorizontalSeparator()]
            ,[sg.Text('Wins: ' + str(ww) + '  Points: ' + str(wp), key='wSum')
              ,sg.Push()
              ,sg.Text('Wins: ' + str(rw) + '  Points: ' + str(rp), key='rSum')]
            ,[sg.HorizontalSeparator()]
            ,[sg.Text('Next Match:', key='nextMatch')]
            ,[sg.Text(nextWhiteTeam, key='nextWhiteTeam')
              ,sg.Push()
              ,sg.Text(nextRedTeam, background_color='red', key='nextRedTeam')
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
              ,sg.Button('Q', button_color=('black', 'white'), key='u0')
              ,sg.VerticalSeparator()
              ,sg.Push()
              ,sg.VerticalSeparator()
              ,sg.Button('Q', button_color=('black', 'white'), key='u2')
              ,sg.VerticalSeparator()
              ,sg.Button('Next Fight', key='b5')
              ,sg.VerticalSeparator()
              ,sg.Push()
              ,sg.VerticalSeparator()
              ,sg.Button('Q', button_color=('black', 'white'), key='u1')
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
window = sg.Window('Window Title', layout, resizable=True, finalize=True)
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
window.bind('<Key-a>',"u0")
window.bind('<Key-l>',"u1")
window.bind('<space>',"u2")
window.bind('<Return>',"b5")

#fs = round(window.size[1]/20)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == "Configure":
        #print('configure')
        #print(window.size)
        #print (window.size[1])
        fs = round(window.size[1]/16)
        window.refresh
        [window[f'blank{i}'].Update(font=('arial',fs)) for i in range(0,9)]
        window['whiteName'].Update(font=('arial',fs))
        window['redName'].Update(font=('arial',fs))
        window['nextMatch'].Update(font=('arial',fs))
        window['nextWhiteTeam'].Update(font=('arial',fs))
        window['nextRedTeam'].Update(font=('arial',fs))
        window['rSum'].Update(font=('arial',fs))
        window['wSum'].Update(font=('arial',fs))
        [window[f'white{i}'].Update(font=('arial',fs)) for i in range(0,5)]
        [window[f'red{i}'].Update(font=('arial',fs)) for i in range(0,5)]
        [window[f'whiteNames[{i}]'].Update(font=('arial',fs)) for i in range(0,5)]
        [window[f'redNames[{i}]'].Update(font=('arial',fs)) for i in range(0,5)]
        [window[f'whiteIppon[{i}][0]'].Update(font=('arial',fs)) for i in range(0,5)]
        [window[f'whiteIppon[{i}][1]'].Update(font=('arial',fs)) for i in range(0,5)]
        [window[f'whiteHansoku[{i}]'].Update(font=('arial',fs)) for i in range(0,5)]
        [window[f'redIppon[{i}][0]'].Update(font=('arial',fs)) for i in range(0,5)]
        [window[f'redIppon[{i}][1]'].Update(font=('arial',fs)) for i in range(0,5)]
        [window[f'redHansoku[{i}]'].Update(font=('arial',fs)) for i in range(0,5)]
        [window[f'hikiwake[{i}]'].Update(font=('arial',fs)) for i in range(0,5)]
        [window[f'b{i}'].Widget.config(font=('arial',round(fs/2))) for i in range(0,11)]
        [window[f'u{i}'].Widget.config(font=('Wingdings 3',round(fs/2))) for i in range(0,3)]
    if event == 'b5':
        if len(redIppon[fn][0]+redIppon[fn][1]) == len(whiteIppon[fn][0]+whiteIppon[fn][1]):
            #print('draw')
            hikiwake[fn] = 'X'
            window['hikiwake[' +str(fn) + ']'].Update('X')
        elif len(redIppon[fn][0]+redIppon[fn][1]) > len(whiteIppon[fn][0]+whiteIppon[fn][1]):
            rw = rw + 1
            window['rSum'].Update('Wins: ' + str(rw) + '  Points: ' + str(rp))
        elif len(redIppon[fn][0]+redIppon[fn][1]) < len(whiteIppon[fn][0]+whiteIppon[fn][1]):
            ww = ww + 1
            window['wSum'].Update('Wins: ' + str(ww) + '  Points: ' + str(wp))
        if fn < 4:
            window['white'+str(fn)].Update(background_color='white')
            window['red'+str(fn)].Update(background_color='white')
            fn = fn + 1
            window['white'+str(fn)].Update(background_color='grey')
            window['red'+str(fn)].Update(background_color='grey')
            #print(fn)
    if event == 'u2':
        if fn > 0:
            print(fn)
            window['white'+str(fn)].Update(background_color='white')
            window['red'+str(fn)].Update(background_color='white')
            fn = fn - 1
            window['white'+str(fn)].Update(background_color='grey')
            window['red'+str(fn)].Update(background_color='grey')
            hikiwake[fn] = ''
            window['hikiwake[' +str(fn) + ']'].Update('')
            print(fn)
    if event == 'b10':
        #print('Men')
        #print('fn:',fn)
        if redIppon[fn][0] == '':
            redIppon[fn][0] = 'M'
            window['redIppon[' + str(fn) + '][0]'].Update('M')
            rp = rp + 1
            window['rSum'].Update('Wins: ' + str(rw) + '  Points: ' + str(rp))
            print(rp)
        elif redIppon[fn][1] == '':
            redIppon[fn][1] = 'M'
            window['redIppon[' + str(fn) + '][1]'].Update('M')
            rp = rp + 1
            window['rSum'].Update('Wins: ' + str(rw) + '  Points: ' + str(rp))
            print(rp)
        else:
            print('error')
    if event == 'b9':
        #print('Kote')
        #print('fn:',fn)
        if redIppon[fn][0] == '':
            redIppon[fn][0] = 'K'
            window['redIppon[' + str(fn) + '][0]'].Update('K')
            rp = rp + 1
            window['rSum'].Update('Wins: ' + str(rw) + '  Points: ' + str(rp))
            print(rp)
        elif redIppon[fn][1] =='':
            redIppon[fn][1] = 'K'
            window['redIppon[' + str(fn) + '][1]'].Update('K')
            rp = rp + 1
            window['rSum'].Update('Wins: ' + str(rw) + '  Points: ' + str(rp))
            print(rp)
        else:
            print('error')
    if event == 'b8':
        if redIppon[fn][0] == '':
            redIppon[fn][0] = 'D'
            window['redIppon[' + str(fn) + '][0]'].Update('D')
            rp = rp + 1
            window['rSum'].Update('Wins: ' + str(rw) + '  Points: ' + str(rp))
            print(rp)
        elif redIppon[fn][1] == '':
            redIppon[fn][1] = 'D'
            window['redIppon[' + str(fn) + '][1]'].Update('D')
            rp = rp + 1
            window['rSum'].Update('Wins: ' + str(rw) + '  Points: ' + str(rp))
            print(rp)
        else:
            print('error')
    if event == 'b7':
        if redIppon[fn][0] == '':
            redIppon[fn][0] = 'T'
            window['redIppon[' + str(fn) + '][0]'].Update('T')
            rp = rp + 1
            window['rSum'].Update('Wins: ' + str(rw) + '  Points: ' + str(rp))
            print(rp)
        elif redIppon[fn][1] == '':
            redIppon[fn][1] = 'T'
            window['redIppon[' + str(fn) + '][1]'].Update('T')
            rp = rp + 1
            window['rSum'].Update('Wins: ' + str(rw) + '  Points: ' + str(rp))
            print(rp)
        else:
            print('error')

    if event == 'b6':
        #print('Hansoku:',redHansoku[fn])
        if redHansoku[fn] == '':
            redHansoku[fn] = '▲'
            window['redHansoku[' + str(fn) + ']'].Update('▲')
        else:
            redHansoku[fn] = ''
            window['redHansoku[' + str(fn) + ']'].Update('')
            if whiteIppon[fn][0] == '':
                whiteIppon[fn][0] = 'H'
                window['whiteIppon[' + str(fn) + '][0]'].Update('H')
                wp = wp + 1
                window['wSum'].Update('Wins: ' + str(ww) + '  Points: ' + str(wp))
                print(wp)
            elif whiteIppon[fn][1] == '':
                whiteIppon[fn][1] = 'H'
                window['whiteIppon[' + str(fn) + '][1]'].Update('H')
                wp = wp + 1
                window['wSum'].Update('Wins: ' + str(ww) + '  Points: ' + str(wp))
                print(wp)
            else:
                print('error')
    if event == 'b0':
        #print('Men')
        #print('fn:',fn)
        if whiteIppon[fn][0] == '':
            whiteIppon[fn][0] = 'M'
            window['whiteIppon[' + str(fn) + '][0]'].Update('M')
            wp = wp + 1
            window['wSum'].Update('Wins: ' + str(ww) + '  Points: ' + str(wp))
            print(wp)
        elif whiteIppon[fn][1] == '':
            whiteIppon[fn][1] = 'M'
            window['whiteIppon[' + str(fn) + '][1]'].Update('M')
            wp = wp + 1
            window['wSum'].Update('Wins: ' + str(ww) + '  Points: ' + str(wp))
            print(wp)
        else:
            print('error')
    if event == 'b1':
        #print('Kote')
        #print('fn:',fn)
        if whiteIppon[fn][0] == '':
            whiteIppon[fn][0] = 'K'
            window['whiteIppon[' + str(fn) + '][0]'].Update('K')
            wp = wp + 1
            window['wSum'].Update('Wins: ' + str(ww) + '  Points: ' + str(wp))
            print(wp)
        elif whiteIppon[fn][1] == '':
            whiteIppon[fn][1] = 'K'
            window['whiteIppon[' + str(fn) + '][1]'].Update('K')
            wp = wp + 1
            window['wSum'].Update('Wins: ' + str(ww) + '  Points: ' + str(wp))
            print(wp)
        else:
            print('error')
    if event == 'b2':
        #print('Doh')
        #print('fn:',fn)
        if whiteIppon[fn][0] == '':
            whiteIppon[fn][0] = 'D'
            window['whiteIppon[' + str(fn) + '][0]'].Update('D')
            wp = wp + 1
            window['wSum'].Update('Wins: ' + str(ww) + '  Points: ' + str(wp))
            print(wp)
        elif whiteIppon[fn][1] == '':
            whiteIppon[fn][1] = 'D'
            window['whiteIppon[' + str(fn) + '][1]'].Update('D')
            wp = wp + 1
            window['wSum'].Update('Wins: ' + str(ww) + '  Points: ' + str(wp))
            print(wp)
        else:
            print('error')
    if event == 'b3':
        if whiteIppon[fn][0] == '':
            whiteIppon[fn][0] = 'T'
            window['whiteIppon[' + str(fn) + '][0]'].Update('T')
            wp = wp + 1
            window['wSum'].Update('Wins: ' + str(ww) + '  Points: ' + str(wp))
            print(wp)
        elif whiteIppon[fn][1] == '':
            whiteIppon[fn][1] = 'T'
            window['whiteIppon[' + str(fn) + '][1]'].Update('T')
            wp = wp + 1
            window['wSum'].Update('Wins: ' + str(ww) + '  Points: ' + str(wp))
            print(wp)
        else:
            print('error')

    if event == 'b4':
        if whiteHansoku[fn] == '':
            whiteHansoku[fn] = '▲'
            window['whiteHansoku[' + str(fn) + ']'].Update('▲')
        elif whiteHansoku[fn] == '▲':
            whiteHansoku[fn] = ''
            window['whiteHansoku[' + str(fn) + ']'].Update('')
            if redIppon[fn][0] == '':
                redIppon[fn][0] = 'H'
                window['redIppon[' + str(fn) + '][0]'].Update('H')
                rp = rp + 1
                window['rSum'].Update('Wins: ' + str(rw) + '  Points: ' + str(rp))
                print(rp)
            elif redIppon[fn][1] == '':
                redIppon[fn][1] = 'H'
                window['redIppon[' + str(fn) + '][1]'].Update('H')
                rp = rp + 1
                window['rSum'].Update('Wins: ' + str(rw) + '  Points: ' + str(rp))
                print(rp)
            else:
                print('error')

    if event == 'u0':
        if whiteIppon[fn][1] != '':
            whiteIppon[fn][1] = ''
            window['whiteIppon[' + str(fn) + '][1]'].Update('')
            wp = wp - 1
            window['wSum'].Update('Wins: ' + str(ww) + '  Points: ' + str(wp))
            print(wp)
        elif whiteIppon[fn][0] != '':
            whiteIppon[fn][0] = ''
            window['whiteIppon[' + str(fn) + '][0]'].Update('')
            wp = wp - 1
            window['wSum'].Update('Wins: ' + str(ww) + '  Points: ' + str(wp))
            print(wp)
        else:
            print('error')
            

    if event == 'u1':
        if redIppon[fn][1] != '':
            redIppon[fn][1] = ''
            window['redIppon[' + str(fn) + '][1]'].Update('')
            rp = rp - 1
            window['rSum'].Update('Wins: ' + str(rw) + '  Points: ' + str(rp))
            print(wp)
        elif redIppon[fn][0] != '':
            redIppon[fn][0] = ''
            window['redIppon[' + str(fn) + '][0]'].Update('')
            rp = rp - 1
            window['rSum'].Update('Wins: ' + str(rw) + '  Points: ' + str(rp))
            print(wp)
        else:
            print('error')
            
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    

window.close()
