import random

def load_quiz_questions():
    
    questions = [
        {"question": "What is the capital of India?", "choices": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"], "correct_answer": "B"},
        {"question": "Which river is the longest in India?", "choices": ["A. Ganges", "B. Yamuna", "C. Brahmaputra", "D. Godavari"], "correct_answer": "A"},
        {"question": "When will be the 'Pran Pratisthan' of the 'Ram Mandir' in Ayodhya happen?", "choices": ["A. 22nd January 2021", "B. 22nd January 2022", "C. 22nd January 2023", "D. 22nd January 2024"], "correct_answer": "D. 22nd January 2024"},
        {"question": "Which famous monument is located in Agra, India?", "choices": ["A. Hawa Mahal", "B. Taj Mahal", "C. Qutub Minar", "D. Red Fort"], "correct_answer": "B"},
        {"question": "Who is known as the 'Father of the Nation' in India?", "choices": ["A. Jawaharlal Nehru", "B. Subhas Chandra Bose", "C. Mahatma Gandhi", "D. Sardar Patel"], "correct_answer": "C"},
        {"question": "Which festival is widely celebrated as the 'Festival of Lights' in India?", "choices": ["A. Diwali", "B. Holi", "C. Eid", "D. Navratri"], "correct_answer": "A"},
    ]
    return questions

def display_welcome_message():
    print("Welcome to the Quiz Game!")
    print("Let's test your knowledge about India with the following questions.")
    print("Each correct answer earns you a point. Enter your answer by choosing the corresponding letter.")

def present_quiz_questions(questions):
    score = 0
    for question in questions:
        print("\n" + question["question"])
        for choice in question["choices"]:
            print(choice)
        
        user_answer = input("Enter your answer: ").upper()
        if user_answer == question["correct_answer"].split('.')[0].strip():
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Incorrect. The correct answer is: {question['correct_answer']}")

    return score

def display_final_results(score):
    print("\nQuiz completed!")
    print(f"Your final score is: {score}")
    print("Thanks for playing!")

def play_quiz_game():
    questions = load_quiz_questions()
    display_welcome_message()
    score = present_quiz_questions(questions)
    display_final_results(score)

play_quiz_game()
