import sys
import os
# Add the parent directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ai_agents.toolboxs.tools.basic_calculation import basic_calculator
from ai_agents.toolboxs.tools.get_system_usage import get_system_usage
from ai_agents.toolboxs.tools.reverse_string import reverse_string
from ai_agents.models.OllamaModel import OllamaModel
from ai_agents.models.Agent import Agent

if __name__ == "__main__":
	"""
	Instructions for using this agent:

	Example queries you can try:
	1. Calculator operations:
		- "Calculate 15 plus 7"
		- "What is 100 divided by 5"
		- "Multiply 23 and 4"

	2. String reversal:
		- "Reverse the word 'hello world'"
		- "Can you reverse 'Python Programing'?"
	
	3. General questions (will get direct response):
		- "Who are you?"h
		- "What can you help me with?"
	
	Ollama Commands (run these in terminal):
	- Check available models:		'ollama list'
	- Check running models:			'ps aux | grep ollama'
	- List model tags:				'curl http://localhost:11434/api/tags'
	- Pill a new model:				'ollama pull mistral'
	- Run model server:				'ollama serve'
	"""

	tools = [basic_calculator, reverse_string, get_system_usage]

	# Using Ollama with  mistral model
	model_service = OllamaModel
	model_name = 'mistral' # Can be changed to other models like llama2 etc...
	stop = "<|eot_id|>"

	agent = Agent(tools=tools, model_service=model_service, model_name=model_name, stop=stop)

	print("\nWelcome to the AI Agent! Type 'exit' to quit.")
	print("You can ask me to:")
	print("1. Perform calculations (e.g., 'Calculate 15 plus 7')")
	print("2. Reverse strings (e.g., 'Reverse hello world')")
	print("3. Answer general questions")
	print("4. Get system usage statistics (e.g., 'What is the current CPU usage?')\n")
	while True:
		prompt = input("Ask me anything: ")
		if prompt.strip().lower() == "exit":
			break

		agent.work(prompt=prompt)