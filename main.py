# main.py
from connection import get_config
from agents import Agent, Runner

# Get the run configuration which includes our Gemini model
run_config = get_config()

# Define the Summarizer Agent
# This agent is instructed to summarize text.
summarizer_agent = Agent(
    name="Summarizer",
    instructions="You are a helpful summarization assistant. Your task is to provide concise and accurate summaries of the text provided.",
    model=run_config.model, # Assign the configured Gemini model to this agent
    tools=[] # No external tools needed for basic summarization
)

# Text to be summarized
text_to_summarize = """
The quick brown fox jumps over the lazy dog. This sentence is often used
to test typewriters and computer keyboards because it contains all 26
letters of the English alphabet. It's a well-known pangram. Pangrams are
sentences that contain every letter of the alphabet at least once. They
are popular for calligraphy and typography practice.
"""

# Prepare the input for the agent.
# We'll tell the agent what to do with the text.
agent_input = f"Please summarize the following text:\n\n{text_to_summarize}"

print("Running summarizer agent...")
print("-" * 30)

# Run the summarizer agent with the input text
# The Runner orchestrates the agent's interaction with its assigned model.
result = Runner.run_sync(summarizer_agent, agent_input)

print("Summary:")
print(result.final_output)
print("-" * 30)

# --- Optional: Try with another text ---
print("\nRunning summarizer agent with another text...")
print("-" * 30)

another_text = """
Artificial intelligence (AI) is intelligence demonstrated by machines,
unlike the natural intelligence displayed by humans and animals. Leading
AI textbooks define the field as the study of "intelligent agents": any
device that perceives its environment and takes actions that maximize its
chance of successfully achieving its goals. Colloquially, the term "AI"
is often used to describe machines that mimic "cognitive" functions that
humans associate with the human mind, such as "learning" and "problem-solving".
"""
another_agent_input = f"Summarize this text concisely:\n\n{another_text}"
another_result = Runner.run_sync(summarizer_agent, another_agent_input)

print("Another Summary:")
print(another_result.final_output)
print("-" * 30)