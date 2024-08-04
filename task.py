from crewai import Task 
from tools import tool
from agents import news_writer,news_researcher
# Define the task details

#research task 

research_task = Task(
    description = (
         "Identify the next big trend in {topic}."
    "Focus on identifying pros and cons and the overall narrative."
    "Your final report should clearly articulate the key points,"
    "its market opportunities, and potential risks."
    ),
    expected_output = "A comprehensive 3 paragraphs long report on the latset AI trends",
    tools = [tool],
    agent = news_researcher)

# write news task
write_news_task = Task(
    description = (
        "Write a news article on the latest AI trends in {topic}."
        "The article should be engaging, informative, and accurate."
        "It should also be written in a style that is accessible to a wide audience."
        "The article should be no more than 500 words."
    ),
    expected_output = "A news article on the latest AI trends in {topic}.",
    tools = [tool],
    agent = news_writer,
    output_file = 'new_blog_post.md'
)