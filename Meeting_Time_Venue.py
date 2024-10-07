# Holds all required variables for code.

# Standard Values
email_sender   = "chemistryscgroup22@gmail.com"
email_password = "xzep lgdr ovky wnjd"
email_receiver_SCGrp = ["n.pai@kcl.ac.uk", "caitlin.skinner@kcl.ac.uk", "mohammed.hai@kcl.ac.uk", "jenifer.amenia@kcl.ac.uk"]
email_receiver_Test = []

# Variable Values
venue = "GS.13"
date = "7th October"
time  = "1 PM (13:00)"
grp_name = "SC Chemistry"
agenda = "We will be discussing the overall plan and provide structure to how we want to organize our work"
tod = """
<b> Points to cover </b><br>
<br>1. What we understand so far?
<br> Understanding both the chemistry and what exactly is expected of us.
<br>2. Discuss how we would like to conduct the overall project. 
<br> Establish which variant exactly we will synthesize. Arranging and planning lab days; some days for synthesis and others for analysis (maybe)
<br>3. Discuss actual deadlines 
<br> maybe we could attempt to set a personal deadline so we give ourselves room to cross-check it one another)

Additionally, let's also decide a time, date and place for the succeeding meeting.

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
"""
