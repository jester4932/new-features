from database import Features,db_connection

sqlconn = db_connection()


def databse_build():
    features = [Features(title='First Feature', description='Description of first feature', client='Client A',
                         priority=1, targetdate='2018-04-23', productarea='Policies'),
                Features(title='Second Feature', description='Description of second feature', client='Client C',
                         priority=2, targetdate='2018-05-01', productarea='Claims'),
                Features(title='Third Feature', description='Description of third feature', client='Client B',
                         priority=3, targetdate='2018-05-08', productarea='Billing')]
    sqlconn.add_all(features)
    sqlconn.commit()


# This only for this app. this so the database_build function doesn't continue to add 3 entries every time the app is restarted. it will delete all entries and reset back to the original 3 entries above
def database_reset():
    sqlconn.query(Features).delete()
    databse_build()