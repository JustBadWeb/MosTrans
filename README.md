# МосТрансПроект

### Цель задачи
Разработка модуля, способного анализировать и выдавать пассажиропоток на станциях метро на основе данных о количестве пассажиров

### Реализованное решение
Модульная архитектура решения позволяет решать несколько задач параллельно в команде,
а так же даёт возможность "надстраивать" решение над решением.


В папке `data/` содержатся датасет,
база данных и её настраивающие скрипты (позволяют подключаться сразу к нескольким базам при нужде), содержащая уже отформатированный датасет
и вспомогательный файл для системы транскрибирования речи.


В папке `recognition/` находятся программы, работающие с языком -
`extractor.py` умеет доставать из ввода дату, станцию и линию (как с помощью языковой модели, так и с помощью алгоритма Левенштейна),
а `speech_to_text.py` использует OpenSource модель для распознавания и транскрибирования русской речи.
В папке `tests/` - юниттесты, демонстрирующие стабильность обработки языка. Наше решение очень хорошо себя показывает в поиске названий станций.


`frontend/` и `backend/` - пара, реализующая взаимодействие конечного пользователя с нашим продуктом.
Реализованы следующие способы:
1. Выбор конкретной даты, станции и линии через интерфейс html-форм (дешево и сердито, а главное - эффективно).
2. Ввод произвольного текста (модель попытается узнать дату, станцию и линию из сообщения или угадать при отсутствии конкретных данных).
3. Голосовой ввод с последующим анализом сообщения.

В папке `ai/` хранится математическая модель, предсказывающая пассажиропоток на определённой станции в будущем или в прошлом на основании имеющихся данных.
Модель способна дообучаться на новых данных, из чего следует универсальность и ценность конкретного решения.
