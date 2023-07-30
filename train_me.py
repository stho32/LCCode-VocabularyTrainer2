from library.question_answer_store import QuestionAnswerStore
import random

# Initialize the QuestionAnswerStore
store = QuestionAnswerStore("qa.json")

# Load the questions and reduce the "position" by 1 unless it's already 0
for record in store.qa_storage:
    if record["position"] > 0:
        record["position"] -= 1

# Create a session queue with questions that have "position" between 0 and 5
session_queue = [record for record in store.qa_storage if 0 <= record["position"] <= 5]

# At most, we only take 5 different questions
session_queue = session_queue[:5]

# Initialize the session queue so that each question is asked 4 times
session_queue *= 4

# Shuffle the session queue
random.shuffle(session_queue)

# Track the questions that have been answered correctly on the first attempt
first_attempt_correct = set()

while session_queue:
    print(f"\nQuestions remaining in the queue: {len(session_queue)}")

    # Ask the next question in the queue
    current_question = session_queue.pop(0)
    incorrect_attempts = 0

    while True:
        user_answer = input(f"\n{current_question['question']} ")

        if user_answer == "":
            print("You have chosen to leave the training session.")
            break

        if user_answer == current_question["expected_response"]:
            print("Correct!")
            if incorrect_attempts == 0:
                first_attempt_correct.add(current_question["id"])
            break
        else:
            print("Incorrect. Try again.")
            incorrect_attempts += 1
            if incorrect_attempts >= 3:
                print(f"The correct answer is: {current_question['expected_response']}")
                break
            # Add the current question back to the queue as the next question and at the end
            session_queue.insert(0, current_question)
            session_queue.append(current_question)

    if user_answer == "":
        break

# Update the positions of the tasks in the training queue
for record in store.qa_storage:
    if record["id"] in first_attempt_correct:
        record["position"] += 10

# Save the updated qa_storage to the json file
store.save_storage()
