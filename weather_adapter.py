from chatterbot.logic import LogicAdapter
from city_list import extract_cities

# Logic adapter for weather related questions
class WeatherAdapter(LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        words = ['what', 'is', 'weather']
        if all(x in statement.text.split() for x in words):
            return True
        else:
            return False

    def process(self, input_statement, additional_response_selection_parameters=None):
        from chatterbot.conversation import Statement
        list_of_cities = extract_cities(input_statement)
        if list_of_cities == []:
            response_statement = Statement(text='I am only able to provide weather for')
        else:
            pass
        return response_statement

