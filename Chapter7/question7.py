correct_answers = ["A", "C", "A", "A", "D", "B", "C", "A", "C", "B", "A", "D", "C", "A", "D", "C", "B", "B", "D", "A"]

def grade_exam(filename):
    try:
        with open(filename, 'r') as file:
            student_answers = file.read().splitlines()

        if len(student_answers) != len(correct_answers):
            print("Error: The number of answers in the file doesn't match the expected number of questions.")
            return

        correct_count = 0
        incorrect_count = 0
        incorrect_questions = []

        for i in range(len(correct_answers)):
            if student_answers[i] == correct_answers[i]:
                correct_count += 1
            else:
                incorrect_count += 1
                incorrect_questions.append(i + 1)

        if correct_count >= 15:
            print("Congratulations! You passed the exam.")
        else:
            print("Sorry, you failed the exam.")

        print(f"Total correctly answered questions: {correct_count}")
        print(f"Total incorrectly answered questions: {incorrect_count}")
        if incorrect_count > 0:
            print(f"Questions answered incorrectly: {', '.join(map(str, incorrect_questions))}")

    except FileNotFoundError:
        print("Error: File not found.")

grade_exam('student_answers.txt')
