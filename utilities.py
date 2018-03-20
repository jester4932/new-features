from database import Features,db_connection




# Builds the first three feature suggestions
def databse_build(sqlconn):
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
    sqlconn = db_connection()
    sqlconn.query(Features).delete()
    databse_build(sqlconn)
    sqlconn.close()


# Select query to get all the current feature suggestions in the database
def db_call():
    sqlconn = db_connection()
    data = []
    for row in sqlconn.query(Features).order_by(Features.priority):
        data.append(row)
    chart = make_chart(data)
    sqlconn.close()
    return data, chart


# Inserts new feature suggestions into the database
def db_insert(rows):
    sqlconn = db_connection()
    priority = check_priority(int(rows['priority']))
    if priority:
        priority_update(priority)
    feature = Features(title=rows['title'], description=rows['description'], client=rows['client'],
                         priority=int(rows['priority']), targetdate=rows['targetdate'], productarea=rows['productarea'])
    sqlconn.add(feature)
    sqlconn.commit()
    sqlconn.close()
    return True


#check if priority of submitted feature suggestion is higher than existing feature suggestions
def check_priority(priority):
    sqlconn = db_connection()
    info = []
    for data in sqlconn.query(Features).filter(Features.priority>=priority):
        info.append(data)
    sqlconn.close()
    return info


# Updates priority if priority suggested is higher than any suggestions already in database
def priority_update(data):
    sqlconn = db_connection()
    for info in data:
        x = str(info).split(',')
        row=sqlconn.query(Features).filter(Features.id == int(x[0])).first()
        row.priority = int(x[4])+1
        sqlconn.commit()
    sqlconn.close()


# Makes the table on the web page of current feature suggestions
def make_chart(data):
    chart = ''
    for row in data:
        info = str(row).split(',')
        chart += '''<tr>
        <td align="right" style="border-bottom: 1px solid #d8d8d8">%s</td>
        <td align="right" style="border-bottom: 1px solid #d8d8d8">%s</td>
        <td align="right" style="border-bottom: 1px solid #d8d8d8">%s</td>
        <td align="right" style="border-bottom: 1px solid #d8d8d8">%s</td>
        <td align="right" style="border-bottom: 1px solid #d8d8d8">%s</td>
        <td align="right" style="border-bottom: 1px solid #d8d8d8">%s</td>
    </tr >'''%(info[1],info[2],info[3],info[4],info[5],info[6])
    return chart