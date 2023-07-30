from library.question_answer_store import QuestionAnswerStore

def main():
    # Initialize the QuestionAnswerStore with the qa.json file
    qa_store = QuestionAnswerStore('qa.json')

    while True:
        # Display the menu
        print("\n1. Add a record")
        print("2. Update a record")
        print("3. Delete a record")
        print("4. Exit")
        
        # Get the user's choice
        choice = input("\nPlease enter your choice (1-4): ")
        
        if choice == '1':
            # Add a record
            question = input("Enter the question: ")
            expected_response = input("Enter the expected response: ")
            explanation = input("Enter the explanation: ")
            qa_store.add_record(question, expected_response, explanation, 0)

        elif choice == '2':
            # Update a record
            record_id = input("Enter the id of the record to update: ")
            print("Enter the new values (or leave blank to keep the old values):")
            question = input("New question: ")
            expected_response = input("New expected response: ")
            explanation = input("New explanation: ")
            qa_store.update_record(record_id, question or None, expected_response or None, explanation or None)

        elif choice == '3':
            # Delete a record
            record_id = input("Enter the id of the record to delete: ")
            qa_store.delete_record(record_id)

        elif choice == '4':
            # Exit the program
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
