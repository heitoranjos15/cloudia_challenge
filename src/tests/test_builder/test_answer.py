from src.builders.bot_answer import getAnswer


def test_send_valid_phrase():
    answer = getAnswer('3 5 9 120')
    assert answer == 'Fizz Buzz Fizz FizzBuzz'
