import os

import streamlit as st
<<<<<<< HEAD
from dotenv import load_dotenv
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.callbacks import StreamlitCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import MessagesPlaceholder

load_dotenv()

st.title("langchain-streamlit-app")

def create_agent_chain():
    chat = ChatOpenAI(
        model_name=os.environ["OPENAI_API_MODEL"],
        temperature=os.environ["OPENAI_API_TEMPERATURE"],
        streaming=True,
    )

    agent_kwargs = {
        "extra_prompt_messages": [MessagesPlaceholder(variable_name="memory")],
    }
    memory = ConversationBufferMemory(memory_key="memory", return_messages=True)

    tools = load_tools(["ddg-search", "wikipedia"])
    return initialize_agent(
        tools,
        chat,
        agent=AgentType.OPENAI_FUNCTIONS,
        agent_kwargs=agent_kwargs,
        memory=memory,
    )

    if "agent_chain" not in st.session_state:
        st.session_state.agent_chain = create_agent_chain()


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
prompt = st.chat_input("What is up?")
print(prompt)

if prompt: #入力の文字列（Noneでもから文字列でもない）がある場合

        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            chat = ChatOpenAI(
                model_name=os.environ["OPENAI_API_MODEL"],
                temperature=os.environ["OPENAI_API_TEMPERATURE"],
                )
                messages = [HumanMessage(content=prompt)]
                response = chat(messages)
                st.markdown(response.content)

        with st.chat_message("assistant"):
        callback = StreamlitCallbackHandler(st.container())
        response = st.session_state.agent_chain.run(prompt, callbacks=[callback])
        st.markdown(response)

        st.session_state.messages.append({"role": "assistant", "content": response})
=======

st.title("langchain-streamlit-app")

prompt = st.chat_input("What is up?")
print(prompt)
>>>>>>> 008dc1ddb7e5f76966a410d249a5ae8edb8a2618
