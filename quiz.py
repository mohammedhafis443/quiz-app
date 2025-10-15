# quiz app
class Question :
    def __init__(self,prompt,options,answer):
        self.prompt=prompt
        self.options=options
        self.answer=answer



class Quiz :
    def __init__(self):
        self.questions=[]
     # add question into list   
    def add_question(self,question):
        self.questions.append(question)
    
    
    #start question
    
    def start(self):
        score =0
        print("\n quiz started \n")
        for q in self.questions:
            print(q.prompt)
            for idx , option in enumerate(q.options,start=1):
                print(f"{idx}. {option}")
            
            
            while True :
                try:
                    choice = int(input("enter number of your answer"))
                    if 1<=choice <= len(q.options):
                        break
                    else:
                        print("number out of range")
                except ValueError :
                    print("invalid input")
                    
                    
            selected = q.options[choice-1]
            if selected.lower()==q.answer.lower():
                print("correct")
                score+=1
            else:
                print("wrong answer")
        print(f"quiz is over your score is {score}/{len(self.questions)}")
        return score
    
    
        
        
        
        
        
        
        
        