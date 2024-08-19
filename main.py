
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_experimental.agents.agent_toolkits import create_csv_agent



load_dotenv()

llm = ChatOpenAI(model = "gpt-3.5-turbo-0125")

agent = create_csv_agent(llm, r"cleaned_web_traffic_data (1).csv", verbose=True, allow_dangerous_code=True)

def query_data(query):
    response = agent.invoke(query)
    return response

if __name__ == "__main__":
    user_input = input("> ")
    query = user_input
    response = query_data(query)
