import sqlite3
from person import Person

conn = sqlite3.connect('databases/staff.db', check_same_thread=False)
c = conn.cursor()


class Staff(Person):

    def __init__(self, staff_id, role, tax_number, first_name, last_name, dob):
        super().__init__(first_name, last_name, dob)
        self.staff_id = staff_id
        self.role = role
        self.tax_number = tax_number

    def add_staff(self):
        query = "INSERT into staff VALUES (:staff_id,:role,:tax_number,:first_name,:last_name)"
        with conn:
            c.execute(query, {
                'staff_id': self.staff_id,
                'role': self.role,
                'tax_number': self.tax_number,
                'first_name': self.first_name,
                'last_name': self.last_name,
            })

    def view_staff(self):
        query = "SELECT * FROM staff"
        with conn:
            c.execute(query)
            return c.fetchall()

    def modify_staff(self):
        query = "UPDATE staff " \
                "SET first_name = :first_name, " \
                "last_name = :last_name," \
                "role=:role," \
                "tax_number=:tax_number " \
                "WHERE  staff_id = :staff_id"

        with conn:
            c.execute(query, {
                'staff_id': self.staff_id,
                'first_name': self.first_name,
                'last_name': self.last_name,
                'role': self.role,
                'tax_number': self.tax_number
            })

    def delete_staff(self):
        query = "DELETE FROM staff WHERE staff_id = :staff_id"
        with conn:
            c.execute(query, {'staff_id': self.staff_id})

