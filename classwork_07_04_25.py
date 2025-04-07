import os
import dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
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

# response = llm.invoke('Привіт')

# print(type(response))
# print(response)

messages = [
    # набір інструкцій
    SystemMessage(content='Ти ввічиливий чат-бот. Давай короткі на чіткі відповіді'),
    
    # історія спілквання користувача
    HumanMessage(content='Привіт, я Віктор'),
    AIMessage(content='Привіт! Радий тебе бачити. Чим можу допомогти?'),
    HumanMessage(content='Яка столиця Франції?'),
    AIMessage(content='Столиця Франції - Париж.'),
    HumanMessage(content='Як мене звати?'),
]

# response = llm.invoke(messages)

# print(response)

# Простий чат-бот

messages = [
    SystemMessage(content='Ти чат-бот, який дає відповіді на запитання. Давай чіткі короткі відповіді. Додай до відповіді додаткову цікаву інформацію')
]

 # видалення зайвих повідомлень
trimmer = trim_messages(
    strategy='last', # залишати останні повідомлення
    token_counter = len, # рахуємо кількість повідомлень
    max_tokens=5, # залишати максимум три повідомлення
    start_on='human', # історія завжди починатеметься з HumanMessage
    end_on='human', # історія завжди закінчуватиметься з HumanMessage
    include_system=True # SystemMessage не чіпати
)

# Об"єднати llm trimmer
chain = trimmer | llm

while True:
    user_input = input('Ви: ')
    
    # зупинка розмови
    if user_input == '':
        break
    
    # створити human_message
    human_message = HumanMessage(content=user_input)
    
    # добавляємо до історії
    messages.append(human_message)
    
    # видалите зайве з історії
    messages = chain.invoke(messages)
    
    # застосовуємо llm
    response = chain.invoke(messages)
    
    # Добавляємо до історії
    messages.append(response)
    
    # print
    print(f'AI: {response.content}')
    # print(messages)
    
    
    
   
    
    