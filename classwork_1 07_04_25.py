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


# Завдання 1
# Напишіть чат бота, який спілкується у стилі різних  персонажів книг\фільмів або відомих людей. 
# Ким саме бути  чат бот вирішує з повідомлення від користувача.
# Якщо персонаж або книга невідомі, то відповісти що невідома інформація та запропонувати декілька відомих прикладів на вибір

messages = [
   SystemMessage(content=''' 
                 Ти чат-бот. Ти надаєш відповіді у стилі різних  персонажів книг\фільмів або відомих людей.
                 Твої відповіді мають бути: чіткими, розмір відповіді до 5 речень.
                 Користувач має сказати тобі в стилі кого ти маєш відповідати.
                 Користувач може змінити стиль твоїх відповідей у будь-який час.
                 Після зміни стилю, привітайся у новій ролі.
                 Якщо ти не знаєш у стилі кого відповідати, то задай уточнюючі запитання.
                 Можеш запропонувати декілька відомих тобі варіантів на вибір користувачу.
                 ''')       
]




while True:
    
    input_message = input('Ви: ')
    
    if input_message == '':
        break
    
    human_message = HumanMessage(content=input_message)
    messages.append(human_message)
    
    answer = llm.invoke(messages)
    messages.append(answer)
    
    print(answer.content)