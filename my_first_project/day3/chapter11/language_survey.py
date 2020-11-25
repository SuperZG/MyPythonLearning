from survey import AnonymousSurvey

question = "What kind of language are you using?"
my_survey = AnonymousSurvey(question)
my_survey.show_question()
print('Enter quit to exit.')
while True:
    response = input('Language:')
    if response == 'quit':
        break
    my_survey.store_responses(response)


print('The final result for this survey')
my_survey.show_results()
