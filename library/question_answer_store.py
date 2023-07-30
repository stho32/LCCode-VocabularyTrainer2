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

    def add_record(self, question, expected_response, position):
        # Generate a unique ID for the new record
        record_id = str(uuid.uuid4())

        # Create a new record
        new_record = {"id": record_id, "question": question, "expected_response": expected_response, "position": position}

        # Add the new record to qa_storage
        self.qa_storage.append(new_record)

        # Save the updated qa_storage to the json file
        self.save_storage()

    def update_record(self, record_id, question=None, expected_response=None, position=None):
        # Find the record with the given ID
        for record in self.qa_storage:
            if record["id"] == record_id:
                # Update the fields of the record if new values were given
                if question is not None:
                    record["question"] = question
                if expected_response is not None:
                    record["expected_response"] = expected_response
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
