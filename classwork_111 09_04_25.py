import os
import dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage,
    trim_messages
)

dotenv.load_dotenv()

llm = ChatGoogleGenerativeAI(
    model='gemini-2.0-flash',
    google_api_key=os.getenv('GEMENI_API_KEY'),
)


# функція, яка повертає погоду в місті
def get_weather(city: str, time: str = 'сьогодні'):
    """
    Шукає погоду в певному місті в певний час

    :param
        city: str, місто в для якого треба знайти прогноз погоди
        time: str, час на який шукати прогноз погоди.
                може бути година, наприклад 16:30
                може бути день, наприклад завтра, сьогодні
    :return:
        str, опис погоди в місті
    """

    print('hello from get_weather')
    return f"В {city} сонячно {time}"


def product(a: int, b: int):
    """
    Повертає добуток двох чисел
    """

    print('hello from product')
    return a*b


# створення інтсрумента пошуку в інтернеті
search = DuckDuckGoSearchRun()

# створення агента
agent = create_react_agent(model=llm, tools=[get_weather, product, search])

data_input = {
    'messages': [
        SystemMessage(content='Ти ввічливий чат бот'),
    ]
}

# response = agent.invoke(data_input)
#
# # вивід
# for mes in response['messages']:
#     mes.pretty_print()


# консоль для спілкування

while True:
    user_input = input('YOU: ')

    if user_input == '':
        break

    # переведення в HumanMessage
    human_message = HumanMessage(content=user_input)

    # додати в історії
    data_input['messages'].append(human_message)

    response = agent.invoke(data_input)

    # в reponse знаходиться вся історія
    data_input = response

    # вивід результату(останнє повідомлення)
    last_message = data_input['messages'][-1]

    print(last_message.content)