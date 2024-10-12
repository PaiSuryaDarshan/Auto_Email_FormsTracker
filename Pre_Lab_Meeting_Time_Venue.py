# Holds all required variables for code.

# Standard Values
email_sender   = "chemistryscgroup22@gmail.com"
email_password = "xzep lgdr ovky wnjd"
email_receiver_SCGrp = ["n.pai@kcl.ac.uk", "caitlin.skinner@kcl.ac.uk", "mohammed.hai@kcl.ac.uk", "jenifer.amenia@kcl.ac.uk"]
email_receiver_Test = []

# Variable Values
venue = "GS.4"
date = "14th October"
time  = "1 PM (13:00)"
grp_name = "SC Chemistry"
agenda = "Roles and strategy"
tod = """
<b> Points to cover </b><br>
<br><br>1. Understanding experimental procedures (Thoroughly)
<br> Why and *HOW* we use the apparatus we use? (Like Dean-stark), Purpose and order of washing procedure, precaution to limit unwanted reactions/problems (like dropwise addition etc.)
<br><br>2. What different tasks do we have?
<br> Synthesis Note taking, NMR AND IR checking for reagents and product, Printing the risk assessments, weighing and measuring reactants, setting up equipment, Make details on required/relevant chemical properties of reagents used (boiling points for understanding volatility etc.) (What else?)
<br><br>3. Decide how to delegate these tasks and other specific ones.
<br> Assign ourselves roles, 'x' min shifts when monitoring a reaction
<br><br>4. Briefly run through the risk assessment. 
<br> Understand that everyone knows what the risks are (Also to tell us what is bench-top safe and what is fumehood).
<br><br>
Additionally, let's also decide a time, date and place for the succeeding meeting.
<br><br>
Have a great day!, <br>
Pai (bot)
"""

# Content
subject = "[1 MIN READ] Meeting information"
body = f"""
<html>
<body>
<h3>Meeting details</h3>
<b>Venue: {venue} </b> <br>
<b>Time : {time} </b> <br>
<b>Group Name (used for booking) : {grp_name}</b> 
<br><br>
Hello everyone, 
<br><br>
    Hope you have all had a refreshing and a not too stressful weekend/week (hopefully). This is an automated email just to inform you regarding the meeting taking place. 
<br><br> 
As discussed the meeting is gonna happen on {time}, {date} at {venue}.
<br><br>
<b>Agenda : {agenda} </b>
<br><br>
{tod}
<br><br>
Hope I haven't forgotten anything (>_<). See you soon. <br>
Have a lovely Day!
Pai (bot)
"""
