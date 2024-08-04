from crewai import Agent 
from tools import tool
from dotenv import load_env
load_env()
from langchain_google_genai import ChatGoogleGenrativeAI


# Create an agent

llm = ChatGoogleGenrativeAI(model="gemini-1.5-flash",verbose=True,temperature=0.2,google_api_key= os.getenv("GOOGLE_API_KEY"))

#agent = Agent(llm=llm)


#senior research agent 

news_researcher = Agent(
    role = "senior Researcher",
    goal = "Uncover ground breaking technologies in {topic} ",
    verbose = True,
    memory = True,
    backstory = (
        "Driven by curisoity ,you are at the forefront og innovaion eager to explore and share knowledge that could change the world"
    ),
    llm = llm,
    tools = [tool],
    allow_delegation = True
)

news_writer = Agent(
    role = "news Researcher",
    goal = "Uncover ground breaking technologies in {topic} ",
    verbose = True,
    memory = True,
    backstory = (
        "Driven by curisoity ,you are at the forefront og innovaion eager to explore and share knowledge that could change the world"
    ),
    llm = llm,
    tools = [],
    allow_delegation = False
    
)

#creating a writer agents with custo tools responsible in writing a news blog 

