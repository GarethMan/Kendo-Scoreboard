# Kendo-Scoreboard
Python Based Scoreboard for Kendo Taikai - VERY EARLY DAY's

Please don't flood me with bug reports just yet as there are loads and I need to clear off the obvious ones first.

Please do send mistakes. For example, "the symbol for Men is wrong" (it isn't, I'm not that dumb :) )
## Goal
This is meant to end up as a simple lightweight soreboard program to run on raspberry pi.
\
The philosophy should be to produce the electronic equivalent to a physical scoreboard.
\
It should end up not requiring networking as running a network in a sportshall can be challenging and even if networking capabilities are added they should not be neccesary it order to use the software.
## Prerequisites
So far it uses only Python 3.10 and pysimplegui.

I've provided an exe for non-coder windows users to check out. This may trigger you antivirus (it triggers mine). Obviously, procede at your own caution! I can't be responsible for any harm that may occur running this very very alpha stage program on your system.
## What does it look like?
![Animation of the board](/documentation/scoreboard.webp)
## Keyboard Shortcuts
q= White Men
\
w= White Kote
\
e= White Doh
\
r= White Tsuki
\
t= White Hansoku
\
p= Red Men
\
o= Red Kote
\
i= Red Doh
\
u= Red Tsuki
\
y= Red Hansoku
\
Return= Next fight
\
BackSpace or Delete = Undo Last Action
## Work List
I'll try to keep this bit up to date with stuff I'm working on.

Now
* Team Name entry and possibly import from text file
* Cleaning up a number of redundant variables
* Better selection of names for daihosen fights
* Reinitializing the board

Bugs!
* Cannot Put a score in daihosen without triggering an error that crashes the exe version.
* Undo on blank board (i.e. no ippon etc) errors.
* Lot's more

Future
* Not sure yet!
