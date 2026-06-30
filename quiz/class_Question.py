class Question:
    def __init__(self, question, ans_1, ans_2,
                 ans_3, ans_4, real_answer):
        self.__question = question
        self.__ans_1 = ans_1
        self.__ans_2 = ans_2
        self.__ans_3 = ans_3
        self.__ans_4 = ans_4
        self.__real_answer = real_answer
        
    def set_question(self, question):
        self.__question = question
        
    def set_ans_1(self, ans_1):
        self.__ans_1 = ans_1
    
    def set_ans_2(self, ans_2):
        self.__ans_2 = ans_2
        
    def set_ans_3(self, ans_3):
        self.__ans_3 = ans_3
        
    def set_ans_4(self, ans_4):
        self.__ans_4 = ans_4
        
    def set_real_answer(self, real_answer):
        self.__real_answer = real_answer
        
    def get_question(self):
        return self.__question
        
    def get_ans_1(self):
        return self.__ans_1
    
    def get_ans_2(self):
        return self.__ans_2
        
    def get_ans_3(self):
        return self.__ans_3
        
    def get_ans_4(self):
        return self.__ans_4
        
    def get_real_answer(self):
        return self.__real_answer