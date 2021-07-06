import sqlite3

aircraftdb = sqlite3.connect('databases/aircraft.db')

db_curs = aircraftdb.cursor()

db_curs.execute("""CREATE TABLE IF NOT EXISTS aircraft_table (
        aircraft_id integer,
        flight_id text,
        aircraft_capacity integer,
        aircraft_type text
    )""")
aircraftdb.commit()


class Aircraft:
    def __init__(self, aircraft_type, aircraft_id, aircraft_capacity, flight_id, new_flight_id, search_aircraft_id):
        self.aircraft_type = aircraft_type
        self.aircraft_id = aircraft_id
        self.aircraft_capacity = aircraft_capacity
        self.flight_id = flight_id
        self.new_flight_id = new_flight_id
        self.search_aircraft_id = search_aircraft_id

    def view_all_aircraft(self):
        print('------------------------------------------------------')
        with aircraftdb:
            db_curs.execute("SELECT * FROM aircraft_table ORDER BY aircraft_id ASC")
            ac = db_curs.fetchall()
            print('AC ID \t\tFLIGHT ID \t\tCAPACITY \t\tTYPE')
            for item in ac:
                print(str(item[0]) + '\t\t\t' + str(item[1]) + '\t\t\t'
                      + str(item[2]) + '\t\t\t\t' + str(item[3]))
        return '------------------------------------------------------'

    def assign_aircraft_to_trip(self):
        with aircraftdb:
            db_curs.execute("SELECT * FROM aircraft_table WHERE flight_id = 'NONE' ORDER BY aircraft_id ASC")
            ac = db_curs.fetchall()
            print('------------------------------------------------------'
                  '\nAC ID \t\tFLIGHT ID \t\tCAPACITY \t\tTYPE')
            for item in ac:
                print(str(item[0]) + '\t\t\t' + str(item[1]) + '\t\t\t'
                      + str(item[2]) + '\t\t\t\t' + str(item[3]))
            print('-------------------------------------------------------')
        db_curs.execute(f"""UPDATE aircraft_table SET flight_id = ?
                                WHERE aircraft_id = ?""", (self.new_flight_id.upper(), self.aircraft_id))
        return f'The aircraft has been assigned to the trip {self.new_flight_id}'

    def add_aircraft(self):
        self.aircraft_id = input('Please enter the registered ID of the aircraft:  ')
        self.flight_id = input('Please enter the flight ID this aircraft is registered to:'
                             '\nOr if it is not registered, type "none"  ')
        self.aircraft_capacity = input('Please enter the maximum capacity of the aircraft excluding crew:  ')
        self.aircraft_type = input('Please enter the new aircraft type:  ')
        with aircraftdb:
            db_curs.execute("INSERT into aircraft_table VALUES (?, ?, ?, ?)",
                            (self.aircraft_id, self.flight_id.upper(), self.aircraft_capacity,
                             self.aircraft_type.lower()))
            aircraftdb.commit()
        return f'The aircraft, {self.aircraft_id} has been added'

    def remove_aircraft(self):
        with aircraftdb:
            db_curs.execute("DELETE from aircraft_table WHERE aircraft_id = ?", (self.search_aircraft_id,))
            aircraftdb.commit()
        return f'The aircraft, {self.search_aircraft_id} has been deleted'

    def change_aircraft_details(self):
        self.search_aircraft_id = input('Please enter the registered ID of the aircraft you would like to change:  ')
        self.aircraft_id = input('Please enter the registered ID of the aircraft:  ')
        self.flight_id = input('Please enter the flight ID this aircraft is registered to:'
                               '\nOr if it is not registered, type "none"  ')
        self.aircraft_capacity = input('Please enter the maximum capacity of the aircraft excluding crew:  ')
        self.aircraft_type = input('Please enter the new aircraft type:  ')
        with aircraftdb:
            db_curs.execute("""UPDATE aircraft_table
                               SET aircraft_id = ?,
                                   flight_id = ?,
                                   aircraft_capacity = ?,
                                   aircraft_type = ?
                               WHERE aircraft_id = ?
                            """, (self.aircraft_id, self.flight_id.upper(), self.aircraft_capacity,
                                  self.aircraft_type, self.search_aircraft_id))
        return 'The aircraft has been successfully changed'


aircraft_id = ''
flight_id = ''
aircraft_capacity = ''
aircraft_type = ''
new_flight_id = ''
search_aircraft_id = ''
AC = Aircraft(aircraft_type, aircraft_id, aircraft_capacity, flight_id, new_flight_id, search_aircraft_id)

print(AC.view_all_aircraft())
prompt = input('test')
if prompt.lower() == 'change':
    print(AC.change_aircraft_details())
if prompt.lower() == 'add':
    print(AC.add_aircraft())
if prompt.lower() == 'delete':
    AC.search_aircraft_id = input('Please enter the registered ID of the aircraft you would like to delete:  ')
    confirmation = input(f'Your selected aircraft id is {AC.search_aircraft_id}. Are you sure you would like to delete '
                         f'this aircraft? (YES/NO)  ')
    if confirmation.upper() == 'YES':
        print(AC.remove_aircraft())
if prompt.lower() == 'trip':
    AC.search_aircraft_id = input('Please enter the registered ID of the aircraft you would like to assign:  ')
    print(AC.assign_aircraft_to_trip())
