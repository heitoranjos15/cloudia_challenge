import pytest
from src.builders.user import build_user


def test_valid_user():
    name, plataform = build_user({"name": "john", "plataform": "twitter"})
    assert name == 'john'
    assert plataform == 'twitter'

def test_null_name():
    with pytest.raises(AttributeError):
      build_user({"name": "", "plataform": "twitter"})

def test_null_plataform():
    with pytest.raises(AttributeError):
      build_user({"name": "john", "plataform": ""})

def test_invalid_plataform():
    with pytest.raises(AttributeError):
      build_user({"name": "john", "plataform": "asd"})
