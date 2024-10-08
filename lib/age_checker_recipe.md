As an admin
So that I can determine whether a user is old enough
I want to allow them to enter their date of birth as a string in the format `YYYY-MM-DD`.

As an admin
So that under-age users can be denied entry
I want to send a message to any user under the age of 16 saying their access is denied
And telling them their current age and the required age (16).

As an admin
So that old enough users can be granted access
I want to send a message to any user aged 16 or older to say that access has been granted.

-- DESIGN INTERFACE --

Function: age_checker

- Parameters:

DoB (STR)

- Side effects:

- Returns:

"Access granted"/"Access denied - You have to be 16 or older to enter" (STR)

-- TESTS --

DoB = 2022-01-01 --> "Access denied - You have to be 16 or older to enter"
DoB = 2001-01-01 --> "Access granted"
DoB = 2018-10-08 --> "Access granted"