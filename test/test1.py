# from langchain_core.messages import HumanMessage, SystemMessage
# from langchain_openai import ChatOpenAI
# import os


# # 1. 定义模型
# model = ChatOpenAI(model="deepseek-v4-pro",
#                    api_key=os.getenv("DEEPSEEK_API_KEY"),
#                 base_url="https://api.deepseek.com",
#                 temperature=0,)

# # 2. 定义消息
# messages = [
#     SystemMessage(content="你是AI方面的专家"),
#     HumanMessage(content="请用三句话解释LangChain")
# ]

# # 3. 调用大模型
# result = model.invoke(messages)
# print(result) 
import os
import string
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

load_dotenv()

# 1. 定义模型
model = ChatOpenAI(
    model="deepseek-chat",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
    temperature=0,
)

# 2. 定义消息
messages = [
    SystemMessage(content="你是 AI 方面的专家。"),
    HumanMessage(content="请用三句话解释 LangChain。"),
]

# 3. 调用大模型(实际调用过程会发生在chain中)
# result = model.invoke(messages)

# print(result.content)


# 4. 定义输出解析器组件
parser = StrOutputParser()

# 5. 定义链
# 执行链
chain = model | parser
print(chain.invoke(messages))