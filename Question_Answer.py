
class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    def checkAnswer(self,answer):
        return self.answer == answer 


class Quiz:
    def __init__(self,questions):
        self.questions = questions
        self.score = 0 # This line indicates how many questions the user correctly answered.
        self.questionIndex = 0 # This line indicates which question we are in.
    def getQuestion(self):
        return self.questions[self.questionIndex]
    def displayQuestion(self):
        question = self.getQuestion()
        print(f'Question {self.questionIndex + 1}: {question.text}') 
        
        for q in question.choices:
            print('-> '+ q)
        answer = input('Answer: ')
        self.guess(answer)
        self.loadQuestion()
        
    def guess(self,answer):
        question = self.getQuestion()
        
        if question.checkAnswer(answer):
            self.score +=1 # If the answer is correct, the score is increased by one.
        self.questionIndex += 1 # Even if the answer is incorrect, the index number is increased by one and the next question is passed.
        
    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion() 
    def showScore(self):
        print('Score: ',self.score)
        if self.score == 5:
            print("You're a huge Harry Potter fan!")
        elif self.score == 0:
            print("How would you like to rewatch the Harry Potter series?")
        
    def displayProgress(self):
        totalQuestion = len(self.questions) 
        questionNumber = self.questionIndex + 1
        
        if questionNumber > totalQuestion:
            print('The quiz is over.')
        else:
            print(f'Question {questionNumber} of {totalQuestion}'.center(50,'-')) 
        
        
        
q1 = Question("What is Harry Potter's birthday? ",['31 July 1980','30 July 1980','31 July 1981','30 July 1981'],'31 July 1980')
q2 = Question("Who was Harry Potter's first crush at school?",['Ginny Weasley','Cho Chang','Hermione Granger','Lavender Brown'],'Cho Chang')
q3 = Question("Which form does Harry Potter's Patronus take?",['A deer','A bull','A horse','A stag'],'A stag')
q4 = Question("Who accompained Harry Potter to the Yule ball?",['Padma Patil','Luna Lovegood','Romilda Vane','Parvati Patil'],'Parvati Patil')
q5 = Question("Which one is Harry Potter's original wand?",['Acacia,Phoenix feather','Elm,Phoenix feather','Elder,Phoenix feather','Holly,Phoenix feather'],'Holly,Phoenix feather')
questions = [q1,q2,q3,q4,q5]

quiz = Quiz(questions) 
quiz.loadQuestion()








