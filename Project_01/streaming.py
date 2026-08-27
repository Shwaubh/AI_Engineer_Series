from google import genai
from dotenv import load_dotenv

load_dotenv('../.env')
client = genai.Client()

print("Starting streaming interaction...")
print("Lets watch realtime token")

stream = client.interactions.create(
    model='gemini-2.5-flash',
    input= "Create a simple maths formula and calculate its result",
    stream=True
)

for event in stream:
    event_type = event.event_type
    if event_type == 'interaction.created':
        print("Interaction Created", event.interaction.id)

    elif event_type == 'interaction.status_update':
        print("Interaction Status Update")

    elif event_type == 'step.start':
        print(f"Step Started : {event.step.type}")

    elif event_type == 'step.delta':
        if event.delta.type == "text":
            print("-->>> :: ",event.delta.text, end='\n')
        elif event.delta.type == "though_summary":
            print("THought Summary", event.delta.content)

    elif event_type == 'step.stop':
        print(f"Step Stopped")
    
    elif event_type == 'interaction.completed':
        print("Interaction Completed")

    else:
        print(f"Unknown Event Type: {event_type}")