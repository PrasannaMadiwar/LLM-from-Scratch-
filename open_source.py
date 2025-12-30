from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()
llm = HuggingFaceEndpoint(repo_id="deepseek-ai/DeepSeek-V3.2",task="text-generation",temperature=0.7,max_new_tokens=150)
model = ChatHuggingFace(llm=llm) #its just tranferring the llm to chat model usimh this chathuggingFace wrapper

result = model.invoke("who is mahatma gandhi?")
print(result.content)