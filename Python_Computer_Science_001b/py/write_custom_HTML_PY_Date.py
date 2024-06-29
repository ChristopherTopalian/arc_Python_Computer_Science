# write_custom_HTML_PY_Date.py

import datetime as dt

currentDate = dt.datetime.now().strftime('%Y-%m-%d')

ourHTMLContent = f"""
<html>
<head>
<title> Our HTML Page </title>

<style>

body {{
    padding: 10px;
    background-color: rgb(30, 30, 30);
    font-family: Arial;
    font-size: 20px;
    color: rgb(255, 255, 255);
}}

</style>

</head>

<body>

<div> Current Date: {currentDate} </div>

<div> Hi Everyone </div>

</body>

</html>

"""

with open('ourNewWebpage.html', 'w') as theFile:
    theFile.write(ourHTMLContent)

