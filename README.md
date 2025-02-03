# qa_python

# Реализованные тесты

## 1. Добавление книг
- `test_add_new_book_add_two_books`: проверяет добавление двух книг.
- `test_add_new_book_adds_book_without_genre_success`: проверяет, что книга добавляется без жанра.
- `test_add_new_book_invalid_length`: проверяет, что книги не добавляются, если имя пустое или слишком длинное.
- `test_add_new_book_adds_duplicate_only_once`: проверяет, что дубликаты книг не добавляются.

## 2. Установка жанра книги
- `test_set_book_genre_sets_valid_genre_success`: проверяет успешное присвоение допустимого жанра.
- `test_set_book_genre_invalid_book_no_added`: проверяет, что нельзя установить жанр несуществующей книге.
- `test_set_book_genre_invalid_genre_no_added`: проверяет, что нельзя установить недопустимый жанр.

## 3. Получение информации о жанре книг
- `test_get_book_genre_existing_book_success_received`: проверяет, что возвращается корректный жанр существующей книги.
- `test_get_books_with_specific_genre_books_different_returns_exist_books`: проверяет, что возвращаются книги нужного жанра.
- `test_get_books_with_specific_genre_returns_empty_list_for_unknown_genre`: проверяет, что для неизвестного жанра возвращается пустой список.
- `test_get_books_genre_returns_all_books_success`: проверяет возврат всех книг с их жанрами.

## 4. Проверка возрастного ограничения
- `test_get_books_for_children_returns_books_without_age_rating`: проверяет, что возвращаются только книги, доступные детям.

## 5. Управление избранными книгами
- `test_add_book_one_book_in_favorites_success_added`: проверяет успешное добавление книги в избранное.
- `test_add_book_one_book_in_favorites_duplicate_added_only_once`: проверяет, что книгу можно добавить в избранное только один раз.
- `test_delete_book_from_favorites_success_removed`: проверяет успешное удаление книги из избранного.
- `test_get_list_of_favorites_books_returns_all`: проверяет возврат всех книг из избранного.

