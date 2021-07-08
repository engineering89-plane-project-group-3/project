import sqlite3


class AircraftDatabase:

    aircraftdb = sqlite3.connect('app/databases/aircraft.db', check_same_thread=False)
    db_curs = aircraftdb.cursor()

    # db_curs.execute("""CREATE TABLE IF NOT EXISTS aircraft (
    #         aircraft_id integer,
    #         capacity integer,
    #         type text
    #     )""")
    # aircraftdb.commit()

    def view_all_aircraft(self):
        print('------------------------------------------------------')
        with self.aircraftdb:
            self.db_curs.execute("SELECT * FROM aircraft_table ORDER BY aircraft_id ASC")
            ac = self.db_curs.fetchall()
            print('AC ID \t\tFLIGHT ID \t\tCAPACITY \t\tTYPE')
            for item in ac:
                print(str(item[0]) + '\t\t\t' + str(item[1]) + '\t\t\t'
                      + str(item[2]) + '\t\t\t\t' + str(item[3]))
        return '------------------------------------------------------'

    def assign_aircraft_to_trip(self):
        with self.aircraftdb:
            self.db_curs.execute("SELECT * FROM aircraft_table WHERE flight_id = 'NONE' ORDER BY aircraft_id ASC")
            ac = self.db_curs.fetchall()
            print('------------------------------------------------------'
                  '\nAC ID \t\tFLIGHT ID \t\tCAPACITY \t\tTYPE')
            for item in ac:
                print(str(item[0]) + '\t\t\t' + str(item[1]) + '\t\t\t'
                      + str(item[2]) + '\t\t\t\t' + str(item[3]))
            print('-------------------------------------------------------'
                  '\nThese are the currently unassigned aircraft')
        self.aircraft_id = input('Please enter the registered ID of the aircraft you would like to re-assign:  ')
        self.new_flight_id = input('Please enter the new flight ID this aircraft is assigned to:')
        with self.aircraftdb:
            self.db_curs.execute(f"""UPDATE aircraft_table SET flight_id = ?
                                WHERE aircraft_id = ?""", (self.new_flight_id.upper(), self.aircraft_id))
        return f'The aircraft has been assigned to the trip {self.new_flight_id}'

    def add_aircraft(self):
        self.aircraft_id = input('Please enter the registered ID of the aircraft:  ')
        self.aircraft_capacity = input('Please enter the maximum capacity of the aircraft excluding crew:  ')
        self.aircraft_type = input('Please enter the new aircraft type:  ')
        with self.aircraftdb:
            self.db_curs.execute("INSERT into aircraft_table VALUES (?, ?, ?, ?)",
                                 (self.aircraft_id, self.aircraft_capacity,
                                  self.aircraft_type.lower()))
            self.aircraftdb.commit()
        return f'The aircraft, {self.aircraft_id} has been added'

    def remove_aircraft(self):
        with self.aircraftdb:
            self.db_curs.execute("DELETE from aircraft_table WHERE aircraft_id = ?", (self.search_aircraft_id,))
            self.aircraftdb.commit()
        return f'The aircraft, {self.search_aircraft_id} has been deleted'

    def change_aircraft_details(self):
        self.search_aircraft_id = input('Please enter the registered ID of the aircraft you would like to change:  ')
        self.aircraft_id = input('Please enter the registered ID of the aircraft:  ')
        self.aircraft_capacity = input('Please enter the maximum capacity of the aircraft excluding crew:  ')
        self.aircraft_type = input('Please enter the new aircraft type:  ')
        with self.aircraftdb:
            self.db_curs.execute("""UPDATE aircraft_table
                               SET aircraft_id = ?,
                                   aircraft_capacity = ?,
                                   aircraft_type = ?
                               WHERE aircraft_id = ?
                            """, (self.aircraft_id, self.aircraft_capacity,
                                  self.aircraft_type, self.search_aircraft_id))
        return 'The aircraft has been successfully changed'

    def get_capacity(self, ac_id):
        print(ac_id)
        self.db_curs.execute("SELECT capacity FROM aircraft WHERE aircraft_id = " + ac_id)
        return int(self.db_curs.fetchone()[0])
