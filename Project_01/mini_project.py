from config import client

SYSTEM_INSTRUCTION = """
    Your name is Jarvis.
    You are a helpful Football Assistant.
    Answer within 2 lines.
    When asked about any topic other than football, just say I don't know.
"""

conversation_history = []

def chat(user_message: str) -> str:
    msg = {
        "type": "user_input",
        "content": [ { "type": "text", "text" :  user_message  } ]
    }
    conversation_history.append(msg)
    interaction = client.interactions.create(
        model = 'gemini-2.5-flash',
        input = conversation_history,
        system_instruction = SYSTEM_INSTRUCTION
    )
    assitant_msg = interaction.output_text
    msg = {
        "type": "model_output",
        "content": [ { "type": "text", "text" :  assitant_msg  } ]
    }
    return assitant_msg

def chat_iti(user_message: str, previous_id=None) -> tuple:
    interaction = client.interactions.create(
        model = 'gemini-2.5-flash',
        input = user_message,
        system_instruction = SYSTEM_INSTRUCTION,
        previous_interaction_id=previous_id
    )
    return ( interaction.output_text, interaction.id )

print('Jarvis :: Welcome to Jarvis Football AI')

pid = None
while ( msg := input("You : ") ) != 'exit':
    # reply_manual = chat(msg)
    # print(f"Jarvis [Manual] :: {reply_manual}")
    reply_iti, pid = chat_iti(msg, pid)
    print(f"Jarvis [ITI] :: {reply_iti}")
    print()

print("Thanks !!! -> Jarvis")