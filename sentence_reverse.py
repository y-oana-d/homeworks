class rearrange_sentence:

    def __init__(self):
        self.sentence = None

    def sentence_change(self):
        
        sentence = input('Please type your sentence here\n>>>')

        new_sentence = sentence.split()

       
        new_sentence.reverse()

        print(*new_sentence)

newclass = rearrange_sentence()
newclass.sentence_change()
