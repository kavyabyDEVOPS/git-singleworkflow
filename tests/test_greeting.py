from app.greeting import create_greeting


def test_create_greeting():
    assert create_greeting("Kavyavenugopal", "Hello") == "Hello, Kavyavenugopal!"
