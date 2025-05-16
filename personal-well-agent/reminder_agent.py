# personal_wellness_agent/reminder_agent.py
from langchain_openai import ChatOpenAI
from crewai import Agent, Task, Crew

class ReminderAgent:
    def __init__(self):
        self.llm = ChatOpenAI(model_name="gpt-4", temperature=0.5)
        self.agent = Agent(
            role="Wellness Assistant",
            goal="Send daily reminders to wake up, hydrate, and exercise",
            backstory="You are a helpful assistant ensuring users follow their wellness routines.",
            llm=self.llm
        )

    def generate_reminder(self, task_description):
        task = Task(
            description=task_description,
            expected_output="A motivational or polite reminder.",
            agent=self.agent
        )

        crew = Crew(
            agents=[self.agent],
            tasks=[task],
            verbose=False
        )

        return str(crew.kickoff())