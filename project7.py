
import getpass
import pg8000



#############################################################################
# Functions
#############################################################################
def displayCities():
    query = """SELECT id, name FROM airports"""
    cursor.execute(query,)
    results = cursor.fetchall()
    #print albums
    for row in results:
        ID = row[0]
        name = row[1]
        print(ID, "|", name)
#############################################################################

login = input('login: ')
secret = getpass.getpass('password: ')

credentials = {'user'    : login, 
               'password': secret, 
               'database': 'csci403',
               'host'    : 'flowers.mines.edu'}

try:
    db = pg8000.connect(**credentials)
except pg8000.Error as e:
    print('Database error: ', e.args[2])
    exit()

# uncomment next line if you want every insert/update/delete to immediately
# be applied; you can remove all db.commit() and db.rollback() statements
#db.autocommit = True

cursor = db.cursor()

displayCities()



cursor.close()
db.close()
 
