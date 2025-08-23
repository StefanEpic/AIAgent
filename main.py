import os

from langchain_gigachat.chat_models import GigaChat
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent

from tools.ms_office import create_work_permit, create_info_list

import dotenv

dotenv.load_dotenv()

giga = GigaChat(
    credentials=os.environ.get('AUTH_KEY'),
    scope="GIGACHAT_API_PERS",
    model="GigaChat-2",
    verify_ssl_certs=False,
)
functions = [create_work_permit, create_info_list]
system_prompt = (
        "Твоя задача спросить у пользователя, что он хочет сгенерировать — допуск к работе или лист ознакомления или оба документа. "
        "Затем нужно сгенерировать допуск к работе или лист ознакомления. "
        "Допуск к работе делается на одного сотрудника и для его создания тебе надо получить от пользователя дату "
        "начала стажировки сотрудника, дату окончания стажировки сотрудника, "
        "фамилию имя отчество и дату выхода на работу сотрудника. "
        "Лист ознакомления может делаться на несколько сотрудников и для его создания тебе надо получить от пользователя "
        "фамилию имя отчество, должность, название топливной базы для каждого сотрудника."
    )
giga_with_functions = giga.bind_functions(functions)
agent_executor = create_react_agent(giga_with_functions, functions, prompt=system_prompt)

if __name__ == "__main__":
    while True:
        user_input = input("Пользователь: ")
        if user_input == "":
            break
        print(f"Пользователь: {user_input}")
        resp = agent_executor.invoke({"messages": [HumanMessage(content=user_input)]})
        bot_answer = resp['messages'][-1].content
        print("\033[93m" + f"Bot: {bot_answer}" + "\033[0m")
