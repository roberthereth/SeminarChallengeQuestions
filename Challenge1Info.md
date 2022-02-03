# Challenge Problem #1

In the state of Montana, there are 56 counties. As a resident of Montana, you license your vehicle in the county where you reside, and receive a license plate. Normal (non-personalized) license plates indicate which county you reside in by having a numeric prefix in front of the license plate that allows a resident to know where the vehicle (and therefore, the owner) resides. So, if you see a license plate with a number similar to '1-AAA12345', they are a resident of Butte-Silberbow county.  Similarly, if the license plate number is '5-BBB98765', they are a resident of Lewis and Clark County.  A license plate of '12-12345AB' would be a resident of Hill county, and so on.

Provided is a comma-separated (CSV) file that contains a list of counties, the county seat (city), and the license plate prefix number. Your programming challenge is to write a program that allows the user to provide you the county number from a license plate, and have the program respond with the County name and seat city. The program should allow the user to make as many queries as desired, and then exit when given some specific input.

For an extra challenge, allow the user to specify what information is returned from the query, County Name, Seat City, or both at runtime.



Hints:

- Knowing how to read in a file and store the results in memory is a good skill to have, and will come into play for later programming challenges.
- Choosing the correct data structure for doing lookups is important.
  - What structure would you choose if the lookup was done using the county name instead of license plate number?
- The next programming challenge will build on this problem, so make sure you complete and understand this program.
