"""
8-11. Archived Messages: Start with your work from Exercise 8-10. Call the
function send_messages() with a copy of the list of messages. After calling the
function, print both of your lists to show that the original list has retained its
messages.
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
send_messages(messages[:], sent_messages)

print(messages)
print(sent_messages)