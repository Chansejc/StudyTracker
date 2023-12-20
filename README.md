# Study Tracker
## Database Objects
### -These objects are initialized with the name of the database and either the name of the being accsessed or a list of the tables in the Database.
> db = Database("Database.db", "Table")
## Database Querying Data:
### get_entries(Table-name):
> Fetches all data from the table in the database.A
### send_entry(Table-name, list):
> Opens a connection to the database and adds a new record specified information for each field. The specified information comes from the list parameter.
### send_start_entry(Table-name, List-of-values):
> Specifically for the Records database and adding start times that can be queried later.
### send_sesh_length(Table-name, Username):
> Specifically for the Records database and adding an end time to the records that correlates with the specified username and doesn't have a value in the end_time field.
## ST_time
