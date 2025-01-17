# Определение жанра по изображению обложки музыкального диска
## *Описание задачи:*
- Необходимо разработать модель, которая определит жанр музыкального альбома по изображению его обложки.

## *Данные:*
- Изображения в формате PNG, упакованные в zip-архивы. Имя архива соответствует музыкальному жанру. Каждый zip-архив содержит папку с изображениями музыкальных обложек соответствующего жанра.
- Данные для скачивания находится по ссылке https://disk.yandex.ru/d/2FCB3uEl411KpQ

## *План работ:*
- Загрузка датасета с картинками
- Анализ изображений
- Создание baseline
- Улучшение baseline
- Исследование результатов лучшей модели



# Общий вывод:
>В ходе работы были выполнены следующие операции:
>- Сформирован датасет
>- Исследованы все изображения датасета
>- Сформированы выборки для обучения различных моделей
>- Сформированы baseline'ы разных решений
>- Проведены попытки улучшения базовых моделей
>- Проведелно финальное тестирование лучшей модели

> В ходе исследования была изучена информация о имеющихся данных для обучения. Были сформированы и трансформированы датасеты для различных моделей . Выбраны основные метрики, на которых основывалось обучения моделей (f1 и accuracy). В ходе исследования лучший результат был у baseline Catboost. Так же удалось обучить нейросеть CV используя модель ResNet50. Модель обучалась на train и test, из-за чего модель подогнолась под тестовую выборку. Но на текущий момент это лучший из вариантов по метрике f1 = 0.635
    
