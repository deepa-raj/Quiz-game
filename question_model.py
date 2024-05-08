# # TODO:
# #  Classes provide a means of bundling data and functionality together.
# #  Creating a new class creates a new type of object, allowing new instances of that type to be made.
# #  Each class instance can have attributes attached to it for maintaining its state.
# #  #
# #  ATTRIBUTES in Python are variables associated with an object and are used to store data related to the object.
# #  METHODS in Python are functions that are associated with an object, and they are used to perform operations on the object.
#
# class Question:
#     def __init__(self, q_text, q_answer): # We have our init function and inside the init function, in addition to this thing called self
#                                           # which is the actual object that's being created or being initialized,
#                                           # in addition, you can add as many parameters as you wish.
#                                           # And that parameter is going to be passed in, when an object gets constructed from this class.
#                                           # And once you receive that data, then you can use it to set the object's attributes.
#         self.text = q_text
#         self.answer = q_answer
#
#
#
# # new_q = Question("deepsi", "False")
# # print(new_q.text)
#






# TODO: PRACTICE PROBLEM ON MY OWN
# -----------------------------------------------------------------------------------------------------------------------------




class Questions:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer


