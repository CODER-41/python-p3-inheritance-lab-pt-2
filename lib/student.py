class Student:
    def hello(self):
        """Prints out the phrase "Hey there! I'm so excited to learn stuff." from the student"""
        print("Hey there! I'm so excited to learn stuff.")

    def raise_hand(self):
        """Prints out the phrase "Pick me!" from the student when they raise their hand"""
        print("Pick me!")
    #pass

class ChattyStudent(Student):

    def hello(self):
        super().hello()

        #Add the chatty augmentation
        print("How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died...")
    
    def raise_hand(self):

        #call the parent's raise_hand method ten times
        super().raise_hand()
        super().raise_hand()
        super().raise_hand()
        super().raise_hand()
        super().raise_hand()
        super().raise_hand()
        super().raise_hand()
        super().raise_hand()
        super().raise_hand()
        super().raise_hand()









    #pass
