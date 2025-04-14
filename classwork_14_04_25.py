import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage,
    trim_messages
)


llm = ChatGoogleGenerativeAI(
    model='gemini-2.0-flash',
    google_api_key=st.secrets.get('GEMENI_API_KEY'),
)

# головний заголовок
st.title('IT Step Chat-bot')

# простий текст
st.markdown('Простий чат-бот для спілкування. Модель gemini-2.0-flash')



# st.markdown(user_input)

# print(user_input)

# Додаємо історію повідомлень до сесії

# 
if 'messages' not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content='''
            Ти ввічливий чат-бот. Відповідай коротко та чітко
                    ''')
    ]
    
# Місце для вводу повідомлення від користувача
user_input = st.chat_input('Введіть ваше повідомлення')

# якщо користувач щось ввів
if user_input is not None:
    
    # додати повідомлення від користувача в історію
    human_message = HumanMessage(content=user_input)
    st.session_state.messages.append(human_message)
    
    # виклик моделі
    response = llm.invoke(st.session_state.messages)
    
    # Додати відповідь моделі до історії
    st.session_state.messages.append(response)
    
    # print(input.content)
    # print(response.content)
    
# відображення історії спілкування (in streamlit)
for message in st.session_state.messages:
    # check who wrote messages
    if isinstance(message, HumanMessage): # перевірка на тип данних
        role = 'human'
    elif isinstance(message, AIMessage): # перевірка на тип данних
        role = 'AI'
    else: # system message пропускаємо
        continue
    
    with st.chat_message(role):
        st.markdown(message.content)