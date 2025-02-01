import pytest

from main import BooksCollector

@pytest.fixture()
def collector(): # создания объекта BooksCollector()
    return BooksCollector()

@pytest.fixture() # создаем список книг с жанрами для объекта BooksCollector()
def books_different_genres(collector):
    collector.add_new_book('Ван-Пис')
    collector.set_book_genre('Ван-Пис', 'Комедии')
    collector.add_new_book('Фури-Кури')
    collector.set_book_genre('Фури-Кури', 'Комедии')
    collector.add_new_book('Атака титанов')
    collector.set_book_genre('Атака титанов', 'Фантастика')
    collector.add_new_book('Тетрадь смерти')
    collector.set_book_genre('Тетрадь смерти', 'Детективы')
    return collector
