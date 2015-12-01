import getpass
import pg8000

#############################################################################
# Functions
#############################################################################
def pickArrivalLocation():
    airport = input("Enter what airport you will be landing at(partial phrase works as well): ")
    query = """SELECT id, name FROM airports
                WHERE POSITION(LOWER(%s) IN LOWER(name)) > 0"""
    cursor.execute(query,(str(airport),))
    results = cursor.fetchall()
    #print albums
    for row in results:
        ID = row[0]
        name = row[1]
        print(ID, "|", name)
    if len(results) == 0:
        print("\nSorry airport not found.\n")
        pickAirport()
    else:
        airport_id = input("Type the ID number of your arrival location: ")
        display_venues(airport_id)

def display_venues(airport_id):
    rating = input("Enter the min rating of the venue you'd like to visit(1-5): ")
    query = """SELECT venue.name, venue.address, venue.stars FROM flight_data_restaurants as venue 
               JOIN airports ON venue.city = airports.city WHERE airports.id = %s AND venue.stars > %s"""
    cursor.execute(query, (airport_id, rating))
    results = cursor.fetchall()
    for row in results:
        name = row[0]
        address = row[1]
        stars = row[2]
        print(name, "|", address, "|", stars)
    print("\n")
    if len(results) == 0:
        print("No results found.\n")

#############################################################################
#login = input('login: ')
#secret = getpass.getpass('password: ')

login = 'defernan'
secret = 'ddf659'
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

while(True):
    pickArrivalLocation()


cursor.close()
db.close()
 
