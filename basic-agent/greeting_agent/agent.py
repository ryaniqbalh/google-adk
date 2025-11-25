from google.adk.agents import Agent

root_agent = Agent(
    name="greeting_agent", # The agent name must match the folder name.
    model="gemini-2.0-flash", # https://ai.google.dev/gemini-api/docs/models
    description="Greeting agent",
    instruction="""
    You are a helpful assistant that greets the user. 
    Ask for the user's name and greet them by name.
    """,

)
