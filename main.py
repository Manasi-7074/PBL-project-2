import pandas as pd
import difflib
try:
    data = pd.read_csv(r"C:\Users\Manasi\pbl lab\college_chatbot_dataset.csv")
except FileNotFoundError:
    print(" Dataset file not found. Please make sure 'college_chatbot_dataset.csv' is in the same folder.")
    raise SystemExit
    
questions = data["Question"].tolist()
answers = data["Answer"].tolist()

def chatbot_response(user_input):
    """Returns the closest matched answer to the user's question."""
    user_input = user_input.lower().strip()
    match = difflib.get_close_matches(user_input, questions, n=1, cutoff=0.4)
    if match:
        index = questions.index(match[0])
        return answers[index]
    else:
        return "Sorry, I don't know the answer to that. Please contact the college office for more information."

print(" Welcome to the College ChatBot!")
print("Ask any question about the college. (Type 'exit' to stop)\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Bot: Thank you for chatting! Have a great day ")
        break
    response = chatbot_response(user_input)
    print("Bot:", response)
