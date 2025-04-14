import os
import dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import(
    AIMessage,
    HumanMessage,
    SystemMessage,
    trim_messages
)


dotenv.load_dotenv()

llm = ChatGoogleGenerativeAI(
    model = 'gemini-2.0-flash',
    google_api_key = os.getenv('GEMENI_API_KEY')
)


# функція, яка повертає погоду в місті

def get_weather(city: str, time: str):
    
    """
    Шукає погоду в певному місті
    _summary_

    Returns:
        _type_: _description_
    """

    print('hello from get_weather')
    return f'В {city} сонячно'

def product(a: int, b: int):
    
    
    print('hello from product')
    return a*b


# створення агента
agent = create_react_agent(model=llm, tools=[get_weather, product])

data_input = {
    'messages':[
        SystemMessage(content='Ти ввічливий бот'),
        HumanMessage(content='У мене 4 кошика. У кожному кошику 3 яблука, скільки в мене яблук?')
    ]
}

response = agent.invoke(data_input)



# вивід

for mes in response['messages']:
    mes.pretty_print()
    
while True:
    user_input = input('You: ')
    
    if user_input == '':
        break
    
    # переведення в HumanMessage
    human_message = HumanMessage(content=user_input)
    
    # Додати в історію
    data_input['messages'].append(human_message)
        
    response = agent.invoke(data_input)
    
    # response знаходиться вся історія
    data_input = response
    
    last_message = data_input['messages'][-1]
    
    print(last_message.content)




