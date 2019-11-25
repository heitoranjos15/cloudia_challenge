def __is_buzz(number):
    return number % 5 == 0


def __is_fizz(number):
    return number % 3 == 0


def getAnswer(phrase):
    words = phrase.split(' ')
    answer = list()
    for word in words:
        text = str()
        try:
          number = int(word)
          if __is_fizz(number):
              text = 'Fizz'
          if __is_buzz(number):
              text = f'{text}Buzz'
          answer.append(text)
        except Exception:
          raise TypeError('Message is not valid')
    return ' '.join(answer)
