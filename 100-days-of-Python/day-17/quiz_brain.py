class Quizbrain(object):
    def __init__(self,q_list):
        self.q_number = 0
        self.q_list = q_list
        self.score = 0
        self.r_u_still_smart = True
        
    def next_question(self):
        current_q = self.q_list[self.q_number]
        self.q_number +=1
        t_ans = input(f"Q.{self.q_number}: {current_q.text} (True/False)? ")
        self.checker(t_ans,current_q.answer)
        
    
    
    def checker(self,usr_ans, corr_ans):
        if usr_ans.lower() == corr_ans.lower():
            print("You're still smart.")
            self.score += 1
        else:
            print("You stopped being smart")
            self.r_u_still_smart = False
        
        print(f"The correct answer is : {corr_ans}")
        print(f"Your current score is : {self.score}/{self.q_number}")
        print("\n")
            