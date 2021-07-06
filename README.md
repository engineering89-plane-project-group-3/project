# Plane Project

# Aircraft
The `Helicopter` and `Plane` class inherit all the attributes and functions from the `Aircraft` parent class
## Aircraft Class
pseudo-code
```
function: view_available_aircraft()
- user requests to view available aircraft
- the program locates the aircraft database
- the program filters the data into available aircraft
- and displays the data to the user

function: assign_aircraft_to_trip()
- If the user sees an aircraft from the view_available_aircraft() function that they want to use,
- They can select that aircraft
- And assign that aircraft to a trip, either pre-planned or enter trip details manually

function: add_aircraft()
- If the user doesn't see their desired aircraft
- They want to add a new aircraft to the database
- Allows the user to add a new aircraft to the database and enter their respective details

function: remove_aircraft()
- If the user would like to remove an aircraft from the database for whatever reason
- Allow the user to search the specific aircraft from the database
- And prompt the user to confirm the deletion
- Removes the aircraft permanently from the database

function: modify_aircraft()
- If the user would like to modify an aircraft, maybe its been updated or the seating arrangement has been changed.
- The user can search for that specific aircraft and allow the user to select the aircraft
- Ask the user if they would like to modify the aircraft data
- If answered yes, show all available editable fields to the user.
- When the user has finished editing the data, save the data
```
