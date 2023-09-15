class QuizBrain:

    def __init__(self, questions_list): 
        self.question_number = 0
        self.score = 0
        self.questions_list = questions_list #will take the question bank as an input


    
    def still_has_questions(self):
        return self.question_number < len(self.questions_list) #If question number is less than total questions return True


    def next_question(self):
        current_question = self.questions_list[self.question_number] #Gets hold of the current question using question number
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ") #Display question to user and ask for input
        self.check_answer(user_answer, current_question.answer) #Call the check_answer method using the users answer and the correct answers as parameters



    def check_answer(self, user_answer, correct_answer): #Compare users answer with the actual answer of question
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("Thats wrong :(")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n") #Prints line break after each question




