from library.question_answer_store import QuestionAnswerStore
import random

class TrainingSession:
    def __init__(self):
        self.qa_store = QuestionAnswerStore('qa.json')
        self.session_queue = []

    def initialize_session(self):
        # Reduce the position of each record by 1, unless it's already 0
        for record in self.qa_store.qa_storage:
            if record["position"] > 0:
                record["position"] -= 1
                self.qa_store.update_record(record["id"], position=record["position"])

        # Form the session queue from questions with a position between 0 and 5
        for record in self.qa_store.qa_storage:
            if 0 <= record["position"] <= 5:
                # Add the question ID to the session queue 4 times
                self.session_queue.extend([record["id"]] * 4)

        # Shuffle the session queue
        random.shuffle(self.session_queue)

        # Limit the session queue to 20 entries
        self.session_queue = self.session_queue[:20]

    def execute_session(self):
        while self.session_queue:
            # Get the next question ID from the session queue
            question_id = self.session_queue.pop(0)
            # Get the corresponding question record
            question_record = next(record for record in self.qa_store.qa_storage if record["id"] == question_id)

            wrong_attempts = 0
            while True:
                # Ask the question and get the user's response
                user_response = input(f"\n{question_record['question']}\nYour answer: ")

                if user_response.lower() == "no content":
                    # If the user wants to leave the session, return immediately
                    return

                if user_response == question_record["expected_response"]:
                    # If the user's response is correct, break the loop and move on to the next question
                    print("Correct!")
                    break
                else:
                    # If the user's response is incorrect, add the question ID to the end of the session queue
                    print("Incorrect. Try again.")
                    self.session_queue.append(question_id)
                    wrong_attempts += 1

                if wrong_attempts == 3:
                    # If the user has attempted the question 3 times without success, reveal the correct answer
                    print(f"The correct answer is: {question_record['expected_response']}")
                    print(f"Explanation: {question_record['explanation']}")
                    break

            print(f"Questions remaining in the queue: {len(self.session_queue)}")

    def finalize_session(self):
        # Increase the position of each record by 10 if it was not answered wrong during the session
        for record in self.qa_store.qa_storage:
            if record["id"] not in self.session_queue:
                record["position"] += 10
                self.qa_store.update_record(record["id"], position=record["position"])

        # Save the updated qa_storage to the json file
        self.qa_store.save_storage()


if __name__ == "__main__":
    session = TrainingSession()
    session.initialize_session()
    session.execute_session()
    session.finalize_session()
