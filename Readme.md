### Problem statement
Given a set of JSON objects (in a file is fine), for each unique ID field show the unique IPs associated with it and
the number of times that IP appeared.  Also, sum the score for that ID.  Make no assumptions about the incoming JSON.
Example input:
{"id":"test","score":12,"ip":"1.2.3.4","message":"Hi"}
{"id":"test","score":5,"ip":"1.2.3.5"}
{"id":"test","score":17,"ip":"1.2.3.4"}
{"id":"test2","score":9,"ip":"1.2.3.4"}

### Example output:

    test:
        1.2.3.5: 1
        1.2.3.4: 2
        score: 34
    test2:
        1.2.3.4: 1
        score: 9

### Goal: 
Design and implement both the program to accomplish this, and the script to test the program.  Any language you
want to use is fine.  Send back the source code for each, along with any assumptions you made.

### Usage:

        instance = Parser()
        instance.data_in(data) # where data is a valid JSON string
        print(instance)
        instance.clear()
        ... Do something else with it ...


### Desirable Feature List:

* Create json input &#x2611;
* Clear object &#x2611;
* Output a str &#x2611;
* Output an object
* Create file input
* Logging
* Update input
* String Formatting
* Command Line Interface

### Assumptions:

1. That input can be a malformed attempt at JSON and should trigger an error.
3. That Create, Retrieve, Update and Destroy operations should be implemented to some extent.
4. That Retrieval is of the Output format contracted. (I left dictionary curly brackets in the interest of time.)
5. That Update is not implemented because we don't lose the input file and can modify it running the program again.
6. That the input file should use a input system that is encapsulated. (File input feature left out in the interest of time.)
