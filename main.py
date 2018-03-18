from bottle import template, run, get, post
import database
import utilities
import socket
import os

HOSTname = socket.gethostname()
HOSTdir = os.getcwd()
STATICdir = os.path.join(HOSTdir, 'static')

WEBhost = "0.0.0.0"
WEBsrvr = 'cherrypy'
if HOSTdir == '/var/www':
    WEBport = '80'
    HOSTurl = 'NewFeatures'
else:
    WEBport = '8090'
    HOSTurl = 'http://localhost:8090'


@get('/')
def home():
    sqlconn = database.db_connection()
    Features = database.Features
    data = []
    for row in sqlconn.query(Features).order_by(Features.id):
        data.append(row)
    return '<h1>%s</h1>'%str(data)

# Web Server Start and Database initial build
utilities.database_reset()
serverurl = 'http://localhost:8090'
print(HOSTurl)
run(host=WEBhost, server=WEBsrvr, port=WEBport, debug=True)
