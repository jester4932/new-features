# new-features
Allowing users to add new feature suggestions in a web interface
files needed:
Python2.7
    bottle 0.12.13
    cherrypy8.9.1
    sqlalchemy 1.2.5
npm
    bower (installed globally - npm install -g bower)
        knockoutjs 3.4.2

I have a running instance of this on AWS at 18.188.120.230

I am using sqlalchemy to create a local database using sqlite, but you could spin up a postgres database to do the same thing by changing the 'engine' variable in the database.py module to point to it.
When app is started it will create a file called newfeatures.db(this is the database) and put it in the working directory. The database will have 3 entries in it that are hard coded in the utilities.py module.
The database_reset function in utilities.py deletes all entries in the neweatures.db file and resets it to original 3. This id done so that every time the app is restarted, so it does not add 3 more of the
original entries into the database making it grow by 3 every time. When a new feature suggestion is added, the priority level will be chacked against the database and any with an equal or lower priority will be
moved to the next priority level with 1 being the most important and 10 being the least important.