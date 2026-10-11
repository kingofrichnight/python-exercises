"""Notification service with injected delivery

Concepts: composition, dependency injection, duck typing
Prerequisites: Earlier exercises in this section and the preceding sections.

PROBLEM
Build a notifier that strips a message and sends it using an injected
object’s send(message) method. Reject blank messages. Test with an in-memory
recorder so the exercise never sends an actual message.

HINT
The notifier depends on behavior, not a concrete transport.

STRETCH
Define a Protocol for the delivery dependency.

HOW TO PRACTICE
Read the problem, implement your own solution, then compare with the reference
below. Run this file to execute its examples and edge-case checks. Assertions
are learning checks, not a replacement for production input validation.
"""

class Recorder:
    def __init__(self):
        self.messages = []

    def send(self, message):
        self.messages.append(message)

class Notifier:
    def __init__(self, delivery):
        self.delivery = delivery

    def notify(self, message):
        message = message.strip()
        if not message:
            raise ValueError('message is empty')
        self.delivery.send(message)


def check():
    recorder = Recorder()
    notifier = Notifier(recorder)
    notifier.notify(' hello ')
    assert recorder.messages == ['hello']
    try:
        notifier.notify(' ')
    except ValueError:
        pass
    else:
        raise AssertionError('blank message accepted')
    assert recorder.messages == ['hello']


if __name__ == "__main__":
    check()
    print("PASS: Notification service with injected delivery")
