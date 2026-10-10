"""
8-10. Sending Messages: Start with a copy of your program from Exercise 8-9.
Write a function called send_messages() that prints each text message and
moves each message to a new list called sent_messages as it’s printed. After
calling the function, print both of your lists to make sure the messages were
moved correctly.
"""
def show_messages(messages):
    """Show messages."""
    for messages in messages:
        print(f"{messages.title()}")

def send_messages(messages, sent_messages):
    """Send the messages."""
    while messages:
        sent_text = messages.pop()
        sent_messages.append(sent_text)

messages = ['good morning', 'good afternoon', 'good evening']
sent_messages = []

show_messages(messages)
send_messages(messages, sent_messages)

print(messages)
print(sent_messages)
