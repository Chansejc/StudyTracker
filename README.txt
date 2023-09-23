

new(): adds a new user to the users file
    -This function will check to see if a username is already in the database to reduce the opportunity of duplicates
    -The username checking is case-sensitive
read_users(): Reads the file containing current users
    -Returns a comma separated list of usernames in the database
get_user_list(): Creates a list of all users in the database
    -Users are separated by commas and this command puts all usernames into a list
    -Returns the list of users as strings
get_time(): Gets current time
    -Returns an integer value of the current time that is use able for arithmetic
    -This number can be decrypted in order to get the current time as a time value
    -The number is originally put into a "time_list", then the arithmetic is done on the figure
send_time(): Sends data to the database
    -Sends a set of data that give name, time, and topic of study to the data.txt database
get_entries(): Get a list of all entries
    -Returns a list of all entities in the database
add_users(): Adds unique users to user database
    -Writes users file with new users that haven't already been added
    -This new user list is generated from checking the users in the list of entries
Entity.add(): Adds a record into the database including start time of session
    -The entry that gets added includes a 0 for the end time of the session as well as a 0 for the session time
        upon second entry by the same user the program will prompt the user to confirm "end of session".
Entitiy.show(): Shows the user the information of the sessions creation