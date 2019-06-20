import cgi

form = cgi.FieldStorage()
text1 = form.getfirst("TEXT_1", "doesn't set")
text2 = form.getfirst("TEXT_2", "doesn't set")

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Processing of form data</title>
        </head> 
        <body>""")

print("<h1>Processing of form data!</h1>")
print("<p>TEXT_1: {}</p>".format(text1))
print("<p>TEXT_2: {}</p>".format(text2))

print("""</body>
        </html>""")