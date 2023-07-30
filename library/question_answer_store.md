# Prompt

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

## Storage for Questions and Answers

Please write a storage for questions and answers in the following way:
- The storage is actually a json file on the disk with the name "QuestionsAndAnswers.json".
- Every record in this file contains the following data elements:
	- an id (that is generated as a random guid when the data record is entered)
	- a question
	- an expected response
	- explanation: Contains an explanation about why the question should be answered like the expected response and why it should not be answered in another way. 
	- an int number "position" (which represents the position of the question in the current queue)  

Create the following possible operations:
- Loading all the contents of the storage into a variable (qaStorage).
- Saving the contents of a variable to the storage (qaStorage).
- A method that adds a new record to the variable qaStorage.
- A method that updates a record in the variable qaStorage.
- A method that will delete a record in the variable qaStorage.