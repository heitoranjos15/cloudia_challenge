import pytest
from src.builders.bot_answer import get_answer


def test_send_valid_phrase():
    answer = get_answer('3 5 9 120')
    assert answer == 'Fizz Buzz Fizz FizzBuzz'

def test_send_invalid_phrase():
    with pytest.raises(TypeError):
      get_answer('Ola, tenho alguns numeros 2')

def test_send_number_who_is_not_mutilple_3_or_5():
    answer = get_answer('2 4 7')
    assert answer == ''

def test_send_variety_of_number_multiples_and_not():
    answer = get_answer('3 4 10 120 502')
    assert answer == 'Fizz Buzz FizzBuzz'