import pytest

from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2  # --- исправил, метод был переименован

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # дальше я буду использовать фикстуру для создания объекта BooksCollector()
    def test_add_new_book_adds_book_without_genre_success(self,
                                                           collector):  # проверяет, что новая книга добавляется без жанра
        collector.add_new_book('Как ничего не понять и не подать виду')

        assert collector.books_genre['Как ничего не понять и не подать виду'] == ''

    name_book = ['', 'Жизнь перерождённого мудреца в другом мире. Получение второй профессии и становление сильнейшим']

    @pytest.mark.parametrize('book', name_book)
    def test_add_new_book_invalid_length(self, book,
                                         collector):  # проверяет, что не добавляется книга с пустым и очень длинным названием
        collector.add_new_book(book)

        assert len(collector.books_genre) == 0 and book not in collector.get_books_genre()

    def test_add_new_book_adds_duplicate_only_once(self,
                                                    collector):  # проверяет, книгу с одним наименованием можно добавить только один раз
        collector.add_new_book('Последняя фантазия')
        collector.add_new_book('Последняя фантазия')

        assert len(collector.books_genre) == 1

    def test_set_book_genre_sets_valid_genre_success(self,
                                                           collector):  # проверяет, что можно установить допустимый жанр у добавленной книги
        collector.add_new_book('Корона греха')
        collector.set_book_genre('Корона греха', 'Фантастика')

        assert collector.books_genre['Корона греха'] == 'Фантастика'

    def test_set_book_genre_invalid_book_no_added(self,
                                                  collector):  # проверяет, что нельзя установить жанр у несуществующей книги
        collector.set_book_genre('Ремейк бладборн на пк', 'Ужасы')

        assert collector.books_genre.get(
            'Ремейк бладборн на пк') == None and 'Ужасы' not in collector.books_genre.keys()

    def test_set_book_genre_invalid_genre_no_added(self,
                                                   collector):  # проверяет, что нельзя установить недопустимый жанр у существующей книги
        collector.add_new_book('Евангелион')
        collector.set_book_genre('Евангелион', 'Меха')

        assert collector.books_genre.get('Евангелион') == '' and 'Меха' not in collector.books_genre.keys()

    def test_get_book_genre_existing_book_success_received(self,
                                                           collector):  # проверяет, что возвращается правильный жанр для существующей книги
        collector.add_new_book('Крутой учитель Онидзука')
        collector.set_book_genre('Крутой учитель Онидзука', 'Комедии')

        assert collector.get_book_genre('Крутой учитель Онидзука') == 'Комедии'

    @pytest.mark.parametrize('genre, expected_books', [
        ('Комедии', ['Ван-Пис', 'Фури-Кури']),  # Жанр "Комедии" и ожидаемые книги
        ('Фантастика', ['Атака титанов']),  # Жанр "Фантастика" и ожидаемые книги
    ])
    def test_get_books_with_specific_genre_books_different_returns_exist_books(self, books_different_genres, genre,
                                                                                 expected_books):  # проверяет, что возвращается ожидаемый список книг по запрошенному жанру

        assert books_different_genres.get_books_with_specific_genre(genre) == expected_books

    def test_get_books_with_specific_genre_returns_empty_list_for_unknown_genre(self, books_different_genres): # проверяет, что возвращается пустой список если книг запрошеного жанра несуществует
        assert books_different_genres.get_books_with_specific_genre('Ужасы') == []


    def test_get_books_genre_returns_all_books_success(self, books_different_genres): # проверяет возврат всего списка книг из словаря

        assert  books_different_genres.get_books_genre() == books_different_genres.books_genre


    def test_get_books_for_children_returns_books_without_age_rating(self, books_different_genres): # проверяет, что не возвращаются книги недоступные детям
        expected_books = ['Ван-Пис', 'Фури-Кури', 'Атака титанов']
        assert 'Тетрадь смерти' not in books_different_genres.get_books_for_children() and expected_books == books_different_genres.get_books_for_children()


    def test_add_book_one_book_in_favorites_success_added(self, collector): # проверяет, что существующая книга успешно добавляется в избранное
        collector.add_new_book('Унесенные призраками')
        collector.add_book_in_favorites('Унесенные призраками')

        assert 'Унесенные призраками' in collector.favorites

    def test_add_book_one_book_in_favorites_duplicate_added_only_once(self, collector): # проверяет, что одну книгу можно добавить в избранное только один раз
        collector.add_new_book('Монолог фармацевта')
        collector.add_book_in_favorites('Монолог фармацевта')
        collector.add_book_in_favorites('Монолог фармацевта')

        assert  len(collector.favorites) == 1 and ['Монолог фармацевта'] == collector.favorites


    def test_delete_book_from_favorites_success_removed(self, collector): # проверяет, что существующая книга успешно удаляется из избранного
        collector.add_new_book('Истребитель демонов')
        collector.add_book_in_favorites('Истребитель демонов')
        collector.delete_book_from_favorites('Истребитель демонов')

        assert 'Истребитель демонов' not in collector.favorites and  len(collector.favorites) == 0

    def test_get_list_of_favorites_books_returns_all(self, collector): # проверяет возврат всего списка избранных книг
        collector.add_new_book('Кайдзю № 8')
        collector.add_new_book('Дороро')
        collector.add_book_in_favorites('Кайдзю № 8')
        collector.add_book_in_favorites('Дороро')

        assert ['Кайдзю № 8', 'Дороро'] == collector.get_list_of_favorites_books()












