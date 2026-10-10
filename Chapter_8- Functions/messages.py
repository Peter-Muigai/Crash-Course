"""
8-9. Messages: Make a list containing a series of short text messages. Pass the
list to a function called show_messages(), which prints each text message.
"""
def show_messages(messages):
    """Show messages."""
    for messages in messages:
        print(f"{messages.title()}")

messages = ['good morning', 'good afternoon', 'good evening']
show_messages(messages)
