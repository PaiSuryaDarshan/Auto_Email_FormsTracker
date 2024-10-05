# Holds all required variables for code.

# Standard Values
email_sender   = "chemistryscgroup22@gmail.com"
email_password = "xzep lgdr ovky wnjd"
# email_receiver = ["Suryadarshan82@gmail.com", "k22012568@kcl.ac.uk"]
email_receiver = ["Suryadarshan82@gmail.com", "k22012568@kcl.ac.uk"]

# Variable Values
venue = "GS.13"
date = "7th October"
time  = "1 PM (13:00)"
grp_name = "SC Chemistry"
agenda = "We will be discussing an overall guide and provide structure to how we want to organise our work"
tod = """
<b> Points to cover </b><br>
1. pnt. <br>
2. pnt. <br>
3. pnt. <br>

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
    Hope you have all had a refreshing weekend (hopefully). This is an automated email just to inform you regarding the meeting taking place. 
As discussed the meeting is gonna happen at {time}, {date} at {venue}.
<br><br>
<b>Agenda : {agenda} </b>
<br><br>
{tod}
<br><br>
Hope I haven't forgotten anything (>_<). See you soon. <br>
Have a lovely Day!
"""
