from langchain_community.tools.file_management import ReadFileTool
from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI

from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Step 1: Initialize the ReadFileTool
read_file_tool = Tool(
    name="Read File",
    func=ReadFileTool().run,
    description="Use this tool to read the content of a text file in the current working directory. Provide the file name as input."
)

# Step 2: Initialize the LLM
llm = OpenAI(temperature=0.5)

# Step 3: Combine the tool into a list
tools = [read_file_tool]

# Step 4: Initialize the Agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)

# Step 5: Query the Agent with a file name
file_name = "content.txt"

response = agent.run(f"Read the content of the file named {file_name}.")
print("Response from Agent:")
print(response)