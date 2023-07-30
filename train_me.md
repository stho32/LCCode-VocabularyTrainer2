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

Please utilize this as implementation of the question_answer_store.py:
```python
import json
import uuid

class QuestionAnswerStore:
    def __init__(self, storage_file):
        # storage_file is the path to the json file
        self.storage_file = storage_file
        self.qa_storage = []
        self.load_storage()

    def load_storage(self):
        # Load existing records from the json file
        try:
            with open(self.storage_file, 'r') as file:
                self.qa_storage = json.load(file)
        except FileNotFoundError:
            # If the file does not exist, we start with an empty list
            self.qa_storage = []

    def save_storage(self):
        # Save the current state of qa_storage to the json file
        with open(self.storage_file, 'w') as file:
            json.dump(self.qa_storage, file)

    def add_record(self, question, expected_response, explanation, position):
        # Generate a unique ID for the new record
        record_id = str(uuid.uuid4())

        # Create a new record
        new_record = {"id": record_id, "question": question, "expected_response": expected_response, "explanation": explanation, "position": position}

        # Add the new record to qa_storage
        self.qa_storage.append(new_record)

        # Save the updated qa_storage to the json file
        self.save_storage()

    def update_record(self, record_id, question=None, expected_response=None, explanation=None, position=None):
        # Find the record with the given ID
        for record in self.qa_storage:
            if record["id"] == record_id:
                # Update the fields of the record if new values were given
                if question is not None:
                    record["question"] = question
                if expected_response is not None:
                    record["expected_response"] = expected_response
                if explanation is not None:
                    record["explanation"] = explanation
                if position is not None:
                    record["position"] = position

                # Save the updated qa_storage to the json file
                self.save_storage()
                break

    def delete_record(self, record_id):
        # Find the record with the given ID and remove it from qa_storage
        for record in self.qa_storage:
            if record["id"] == record_id:
                self.qa_storage.remove(record)

                # Save the updated qa_storage to the json file
                self.save_storage()
                break
```

Please write a main file that utilizes the Storage Manager allow the following:

- When the script starts, it will load all questions at the start.
- It goes through all records in the file and reduces the "position" by 1 unless the position is 0 at which point the "position" is not reduced any more.

The session queue:
- The script creates a queue, for the ids of tasks it wants to ask the user. 
- The queue is formed from questions that have a record property "position" of between 0 and 5. All other tasks are not relevant to the training session at hand.
- The queue is shuffled at the start.
- The queue will only at maximum contain 5 different questions. 
- The queue is initialized in a way that every question is asked 4 times. That makes a total of 20 entries in the queue at the start.

The sessions execution:
- A question is asked again and again and again until the user gives the correct answer.
- In case the user does not know the correct answer, after 3 tries, the script will tell the user the correct answer. This should also show the explanation to the user for reference.
- Every time the user answers incorrectly, the task is added to the queue as the next task again.
- Additionally every time the user answers incorrectly, the task is added to the end of the queue.
- Make sure the user always knows how many questions remain in the queue.
- The user may at any time choose to leave the training session. He may do so by entering "no content" as a response to the question.

When the training session is left:
- Positions of the tasks in the training queue are modified like this:
  - If, during the session, the question has never been answered wrong, then 10 is added to the position.
  - All other tasks are not modified.
- In the end the qa-store is saved to disk.