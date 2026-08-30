Turn 1:  User: "My name is Statlearn"
         Model: "Nice to meet you, Statlearn!"

Turn 2:  User: "What's my name?"
         Model: ??? 
         
         → Without history: "I don't know your name."
         → With history:    "Your name is Statlearn."

-----

Approach 1 — Manual history (build it yourself)
  You maintain a list of past messages in Python.
  You send the full history on every call.
  Full control. Full responsibility.

Approach 2 — previous_interaction_id (server-side state)
  You pass the ID of the last interaction.
  The server retrieves the history for you.

  m1 - > m2 -> m3
        ( m1)   (m2)


Learning :: core AI engineering skill.

