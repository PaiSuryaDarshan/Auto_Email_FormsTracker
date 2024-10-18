# Holds all required variables for code.

# Standard Values
email_sender   = "chemistryscgroup22@gmail.com"
email_password = "xzep lgdr ovky wnjd"
email_receiver_SCGrp = ["n.pai@kcl.ac.uk", "caitlin.skinner@kcl.ac.uk", "mohammed.hai@kcl.ac.uk", "jenifer.amenia@kcl.ac.uk"]
email_receiver_Test = []

# Variable Values
venue = "Online (For everyone except Mohammed)"
date = "19th October"
time  = "2 PM (14:00)"
grp_name = "SC Chemistry"
agenda = "We will be discussing the synthesis/gelation plan and make sure what we need to clarify regarding the Analysis process"
tod = """
<b> Points to cover </b>
<br><br>1. What we understand so far?
<br> Understanding the synthesis and gelation thoroughly.
<br><br>2. Go through the risk assessment together perfectly. 
<br> Understand that everyone knows not only the risks, but also what is to be cautious of and why we chose the quantities and reagents we chose.
<br><br>3. Go through Dan's advice regarding spectroscopic analysis. 
<br> Make sure to highlight what part of what dan said we didn't understand so that we can ask him accordingly.
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
<b>Date : {date} </b> <br>
<b>Time : {time} </b> <br>
<b>Group Name (used for booking) : {grp_name} </b> 
<br><br>
Hello everyone, 
<br><br>
    Hope you have all had a refreshing and a not too stressful weekend/week (hopefully). This is an automated email just to inform you regarding the meeting taking place. 
<br><br> 
As discussed the meeting is gonna happen on {date}, {time} at {venue}.
<br><br>
<b>Agenda : {agenda} </b>
<br><br>
{tod}
<br><br>
Hope I haven't forgotten anything (>_<). See you soon. <br>
Have a lovely Day!
Pai (bot)
"""
