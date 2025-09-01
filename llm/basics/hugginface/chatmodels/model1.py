from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3.1",
    task="text-generation"

)

model = ChatHuggingFace(llm=llm)

result = model.invoke("Explain machine learning types with 2 point each and , with eg ")

print(result.content)