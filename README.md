Краткая информация по запуску тестов:
В файле pytest.ini уже всё настроено. Для запуска тестов необходимо лишь ввести в терминале команду: pytest.

Отчёт о тестировании хранится в папке result_tests. Для его генерации нужно ввести в терминал команду: allure serve result_tests. (В случае, если не получится, я загрузил 4 HTML-файла, которые можно скачать и открыть для просмотра отчёта.)

Структура проекта:

    Папка tests:
        Файл conftest.py обычно содержит функции, которые используются многократно, чтобы избежать дублирования кода.
        Файл json.py, хранит структуры JSON для удобочитаемости кода.
        Файл settings.py содержит настройки для каждого теста.
        Файл test_pet.py, пишутся тесты.
    Папка env, хранит хосты и другие данные, например, по хранилищам, базам данных и тд.
    Папка result_tests, автоматически сгенерированная папка командой pytest --alluredir result_tests.
    Файл pytest.ini хранит настройки для запуска pytest.
    Файл requirements.txt используется для установки зависимостей.

Теперь кратко опишу найденные ошибки:

Хочу сразу пояснить, что данный ресурс содержит огромное количество багов. Можно было написать множество разных проверок, но, честно говоря, я не вижу в этом смысла. Опишу то, что было выявлено.

    Метод POST:
    В документации указано, что два поля обязательны для заполнения: name и photoUrl. На эти поля я и ориентировался в тестах. Однако, как выяснилось позже, запись можно создать и без этих полей, что является багом.

    Метод PUT:
    Этот метод реализован некорректно и не соответствует REST-принципам. Поле для указания id отсутствует, хотя оно необходимо для дальнейшего редактирования записи. В текущей реализации id указывается в теле JSON, что неправильно. Более того, метод PUT, по сути, создаёт записи, хотя должен только редактировать, и позволяет изменять само id, что также является ошибкой.

    Метод DELETE:
    При попытке удалить несуществующий id метод ведёт себя некорректно. Правильным поведением было бы возвратить тело ответа для сравнения, но на практике при проверке с помощью assert тест падает с ошибкой.

Другие ошибки: например, запись с существующим id можно создать повторно, что тоже является багом. В целом, багов много, но делать проверки на все и писать много кода не имеет смысла, так как основная задача — оценка метода написания кода, тестов, структуры проекта и т.д.

Хочу в конце добавить кое что, на самом деле вариантов написать кода очень множество, выбрал как мне кажется более читаемый и оптимальный, поэтому если будут нарекания к структуре проекта или самого теста, готов без проблем написать еще несколько варинтов. Кстати при желании можете посмотреть тут же у меня в гите, есть еще 2 проекта, с разным форматом. Имейте введу! Спасибо)

Так же вы могли заметить что в проекте тут я не использовал ООП, классы и тд. Дейсвительно у себя в работе я их использую, однако там более сложная структура API, и оно того требует. Здесь же более легкая - стандартная API без зависимойте, интеграций и тд. Поэтому того что написал, более чем достаточно для проверок в базовом уровне.
