correct_answers = ["A", "C", "A", "A", "D", "B", "C", "A", "C", "B", "A", "D", "C", "A", "D", "C", "B", "B", "D", "A"]

# This function grades an exam based on the answers in a file compared to the correct answers.
def grade_exam(filename):
    try:
        # Open the file with the given filename to read student's answers.
        with open(filename, 'r') as file:
            # Read the entire file and split by lines to get individual answers.
            student_answers = file.read().splitlines()

        if len(student_answers) != len(correct_answers):
            print("Error: The number of answers in the file doesn't match the expected number of questions.")
            return

        correct_count = 0
        incorrect_count = 0
        incorrect_questions = []

        # Iterate over the list of correct answers to compare them with the student's answers.
        for i in range(len(correct_answers)):
            if student_answers[i] == correct_answers[i]:
                # Increment the correct answer count if the student's answer matches the correct answer.
                correct_count += 1
            else:
                # Otherwise, increment the incorrect answer count and record the question number.
                incorrect_count += 1
                incorrect_questions.append(i + 1)

        # Determine if the student has passed or failed based on the correct count.
        if correct_count >= 15:
            print("Congratulations! You passed the exam.")
        else:
            print("Sorry, you failed the exam.")

        print(f"Total correctly answered questions: {correct_count}")
        print(f"Total incorrectly answered questions: {incorrect_count}")
        if incorrect_count > 0:
            print(f"Questions answered incorrectly: {', '.join(map(str, incorrect_questions))}")

    except FileNotFoundError:
        # If the file doesn't exist，error message.
        print("Error: File not found.")

grade_exam('student_answers.txt')
