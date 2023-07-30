```
Please write the code in the following way: 

1. The source code must be capable of achieving the required technical result.
2. The source code should use all available elements not relevant to the first goal, to adhere to the principles of clear communication, thereby preserving its connection to the business problem.

The elements you may use to communicate the connection with the business problem are:
- variable names
- class names
- method names
- the general structure of the code (e.g. how you split it into separate functions)
- comments

The rules are:
- Make sure that the elements are used unambiguous and remain connected to the business problem context.
- Does the code make sense? ("Can you comprehend what is being said?")
- Is the connection to the business problem convincing "at face value"?
- Are no intermediate steps missing?
  
Please write the code in python.
```

Please write a main file that utilizes the Storage Manager allow the following:

- The file we edit through the StorageManager is called qa.json and is placed right next to the script.
- The main file will read the contents of the qa.json file at the start.
- It will then present us with a text based menu that will allow us to add, update and delete records and of cause allow us to exit.
- When we exit the menu the changes are written to disk and the program exits.

Please note that the property "position" will be automatically set to 0 while adding, so it does not need to be entered by the user when he or she adds new records.

Also when updating a record make sure that the user only really needs to change the individual values that the user wants to change.