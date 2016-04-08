Revolvers is a prototype of a possible security feature for hashed passwords
A revolver is a pseudo-random changing variable that a user chooses 
A database would typically have hundreds of revolvers a user can choose from such as:
local temperature
local hour
local minute
hour of specific time zone
local forecast
most recent score of sports team
..etc

Revolvers make it so that even if someone hacked into the database, they would only access the hashed password that has the revolver added to it
This complicates for a hacker figuring out the actaul hash in the database.
A normal hash for the password "password1" would look like
0b14d501a594442a01c6859541bcb3e8164d183d32937b851835442f69d5c94e
While a hash with the revolver would look like
0b14d501a594442a01c68595413bcb3e81614d183d332937b0851835442f69d5c94e

Hashes would be stored in the DB ONLY with the revolver included
In this case, the added revolver is 3130


