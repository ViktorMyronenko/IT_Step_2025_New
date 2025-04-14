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



# створення інтсрумента пошуку в інтернеті
search = DuckDuckGoSearchRun()

# створення агента
agent = create_react_agent(model=llm, tools=[search])

# Напишіть модель показує останні новини про певну
# людину. Якщо користувач вводить не ім’я людини, то вивести
# повідомлення «немає відповідної інформації»

data_input = {
    'messages': [
        SystemMessage(content=
                      '''
                      Ти ввічливий чат бот, який виводить останні новини про відомих людей який введе користувач.
                      Якщо користувач вводить не ім’я людини, то вивести повідомлення «немає відповідної інформації»
                      Результат має складатися з однієї новини.
                                           
                      '''
                      ),
    ]
}


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