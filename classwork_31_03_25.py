import dotenv
import os
import warnings

from langchain_huggingface import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate


warnings.filterwarnings('ignore') # ігнорувати warnings
dotenv.load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = 'mistralai/Mistral-7B-Instruct-v0.3',
    temperature = 0.7,
)


# Prompt
# інструкція
# контекст
# дані користувача
# формат відповіді




# Аналіз тональності
#
# Визнач, чи є тональність тексту позитивною,
# негативною чи нейтральною.

# Приклад 1:
# Input:
# Output:
#
# Користувач:
# Модель:
#
# Human:
# AI:


prompt = """
Ти класифікатор текстів. Твоя задача віднести текст до
одного з класів: позитивний, негативний, нейтральний. 
Відповідь має бути одним словом з цих трьох.

Приклад 1:
Користувач: Чудове відео, мені неймовірно сподобалось
Модель: позитивний

Приклад 2:
Користувач: Дарма витратив час на це
Модель: негативний

Приклад 3:
Користувач: Непогано, на один вечір підійде
Модель: нейтральний

Користувач: Бездарна гра акторів
Модель:
"""

# response = llm.invoke(prompt)
# print(response)


prompt = PromptTemplate.from_template("""
[INST]Ти класифікатор текстів. Твоя задача віднести текст до
одного з класів: позитивний, негативний, нейтральний. 
Відповідь має бути одним словом з цих трьох.

Приклад 1:
Користувач: Чудове відео, мені неймовірно сподобалось
Модель: позитивний

##

Приклад 2:
Користувач: Дарма витратив час на це
Модель: негативний

##

Приклад 3:
Користувач: Непогано, на один вечір підійде
Модель: нейтральний
[/INST]

[INST]
Користувач: {user_data}
Модель: [/INST]
""")


# data = input("Введіть повідомлення: ")
#
# # формуємо промпт для конкретного повідомлення
# user_prompt = prompt.format(user_data=data)
#
# response = llm.invoke(user_prompt)
#
# print(f"Результат: {response}")



# Види промптів

# Zero shot -- без прикладів, просто інструкція
# Few shot -- з прикладом(ами)
# Chain of Thouht(COT, CoT) -- ланцюг думок(хід думок)


zero_shot_prompt = '''
Коли мені було 6 років, я був вдвічі молодший за свою сестру. 
Моїй сестрі зараз 40 років, скільки мені років?
'''

chain_of_thought_prompt = """
[INST]Ти розв'язуєш метематичні задачі.

Приклад:
Задача: Коли мені було 6 років, я був вдвічі молодший за свою сестру. 
Моїй сестрі зараз 40 років, скільки мені років?

Хід думок:
Коли мені було 6 років, моїй сестрі було 6*2=12 років
Моя сестра старша за мене на 12 - 6 = 6 років
Якщо моїй сестрі зараз 40 років, то мені 40 - 6 = 34 роки

Відповідь: 34 роки
[/INST]

[INST]
Задача: Коли мені було 4 років, я був втричі молодший за свою сестру. 
Моїй сестрі зараз 28 років, скільки мені років?

Відповідь:
[/INST]
"""

response = llm.invoke(chain_of_thought_prompt)
print(response)


#Порівняй двох людей за певною ознакою