# Challenge Problem #2

From the last challenge, we allowed the user to lookup the County and County Site using the license plate prefix number. 

In this challenge, we're going to allow the user to lookup the license plate prefix number using the name of the City.

Unfortunately, we don't have a complete list of cities.  So, we're going to write a program that will allow the user to enter a city, and if that city is already known, then to return the county name.  However, if that city is unknonwn, the user will be asked to provide either the County Name or license prefix (you get to choose), and that information will be stored for future lookups.

For this challenge, you will need to create a persistent data store containing the list of known cities and their associated license plate number. For this challenge, this store should be stored as a text file.

You can choose to write a brand-new program, or extend the existing program you wrote previously.  Note, you should be able to initially populate this file with 56 city and county pairs, and you already have the name of the county seat for each county.

The program should allow the user to make as many queries as desired, and then exit when given some specific input.

If you extend the initial program, please ensure the user has the ability to specify which functionality they are choosing (license plate number lookup or city lookup).



Hints:

* Load the data store at startup, and then do the lookups against a data structure contained in memory.
* Choose a data structure that allows you to quickly return a result when giving a properly formatted city.
* Is there a way to avoid issues with the case of the city that the user enters, and still return valid results?  (What if the user enters all upper or lowercase, and the data is stored mixed case?)
* If a user enters an unknown city, immediately open up the data store, store the new information in it, and then close the data store after, and then update the in-memory structure (the order of updating the in-memory vs. on-disk storage doesn't matter).
  * This avoids the potential for corrupting the file if you fail to close  the file due to program error where the content is not fully written out due to the operating system not flushes out the written data on open files.
