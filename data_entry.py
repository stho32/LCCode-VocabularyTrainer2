from library.question_answer_store import QuestionAnswerStore

# Initialize the QuestionAnswerStore
store = QuestionAnswerStore("qa.json")

while True:
    # Display the menu
    print("\nWhat would you like to do?")
    print("1. Add a record")
    print("2. Update a record")
    print("3. Delete a record")
    print("4. View all records")
    print("5. Exit")

    # Get the user's choice
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        # Add a record
        question = input("Enter the question: ")
        expected_response = input("Enter the expected response: ")
        store.add_record(question, expected_response, 0)
        print("Record added successfully!")
    elif choice == "2":
        # Update a record
        record_id = input("Enter the id of the record you want to update: ")

        print("Leave fields blank if you do not wish to update them.")
        question = input("Enter the new question: ")
        expected_response = input("Enter the new expected response: ")

        # Only update fields for which new values were provided
        store.update_record(record_id, question or None, expected_response or None)
        print("Record updated successfully!")
    elif choice == "3":
        # Delete a record
        record_id = input("Enter the id of the record you want to delete: ")
        store.delete_record(record_id)
        print("Record deleted successfully!")
    elif choice == "4":
        # View all records
        for record in store.qa_storage:
            print(record)
    elif choice == "5":
        # Exit
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

# Save any changes to the JSON file before exiting
store.save_storage()
