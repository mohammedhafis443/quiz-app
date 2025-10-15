class User :
    def __init__(self,name) :
        self.name=name
    #greet user
    def greet (self):
        print(f"hello,{self.name}\n welcome to quiz app")
        
    # method to take quiz
    def take_quiz(self,quiz):
        self.greet()
        score=quiz.start()
        
        #save score to a file
        try :
            with open ("score.txt","a") as f :
                f.write(f"{self.name}:{score}/{len(quiz.questions)}\n")
            print("your score has been saved ")
        
        except Exception as e:
            print("error saving score",e)
        