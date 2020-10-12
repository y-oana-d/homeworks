class rearrange_sentence:

    def __init__(self):
        self.sentence = None

    def sentence_change(self):
        # get a string from the console
        sentence = input('Please type your sentence here\n>>>')

        # split the string into a list
        new_sentence = sentence.split()

        # reverse the list
        new_sentence.reverse()


        # print all the list items using print (*)
        print(*new_sentence)

newclass = rearrange_sentence()
newclass.sentence_change()