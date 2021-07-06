import sqlite3

aircraftdb = sqlite3.connect('databases/aircraft.db')

aircraftdb_curs = aircraftdb.cursor()


# c.execute("""CREATE TABLE aircraft_table (
#         aircraft_type text,
#         aircraft_id integer,
#         aircraft_capacity integer,
#         flight_id text
#     )""")
# conn.commit()

class Aircraft:
    def __init__(self):
        self.aircraft_type = aircraft_type
        self.aircraft_id = aircraft_id
        self.aircraft_capacity = aircraft_capacity
        self.flight_id = flight_id

    def view_available_aircraft(self):
        with aircraftdb:
            aircraftdb_curs.execute("SELECT * FROM aircraft_table")
            ac = aircraftdb_curs.fetchall()
            print('TYPE \t\t\tA/C ID \t\tCAPACITY \t\tFLIGHT ID')
            for item in ac:
                print(str(item[0]) + '\t\t' + str(item[1]) + '\t\t\t' + str(item[2]) + '\t\t\t\t' + str(item[3]))
        return ''

    def assign_aircraft_to_trip(self):
        with aircraftdb:
            aircraftdb_curs.execute("SELECT * FROM aircraft_table")
            return aircraftdb_curs.fetchall()
        pass

    def add_aircraft(self):
        aircraftdb_curs.execute("INSERT into aircraft_table VALUES (?, ?, ?, ?)",
                                (self.aircraft_type, self.aircraft_id, self.aircraft_capacity, self.flight_id))
        aircraftdb.commit()

    def remove_aircraft(self):
        aircraftdb_curs.execute("DELETE from aircraft_table WHERE")
        aircraft_remove = input('Please type the ID of the aircraft that is being deleted')
        user_confirmation = 'Are you sure you want to delete this aircraft from the database Y/N' \
                            '\nThis is IRREVERSIBLE'
        aircraftdb.commit()
        pass

    def change_aircraft_details(self):
        pass

# aircraft_remove = input('Please type the ID of the aircraft that is being deleted')
# user_confirmation = 'Are you sure you want to delete this aircraft from the database Y/N' \
#                             '\nThis is IRREVERSIBLE'

aircraft_type = str(input('Please enter the new aircraft type:  '))
aircraft_id = input('Please enter the registered ID of the aircraft:  ')
aircraft_capacity = input('Please enter the maximum capacity of the aircraft excluding crew:  ')
flight_id = input('Please enter the flight id this aircraft is registered to'
                  '\nOr if it is not registered, type "NOT ASSIGNED"  ')
AC = Aircraft()
# print(AC.add_aircraft())
print(AC.change_aircraft_details())
print(AC.view_available_aircraft())
