# Описание задачи: 
Компания «Чётенькое такси» собрала исторические данные о заказах такси в аэропортах. Чтобы привлекать больше водителей в период пиковой нагрузки, нужно спрогнозировать количество заказов такси на следующий час. Постройте модель для такого предсказания.
Значение метрики *RMSE* на тестовой выборке должно быть не больше 48.

# План работы:
- Загрузить данные и выполнить их ресемплирование по одному часу.
- Проанализировать данные.
- Обучить разные модели с различными гиперпараметрами. Сделать тестовую выборку размером 10% от исходных данных.
- Проверить данные на тестовой выборке и сделать выводы.

# Общий вывод:
В ходе исследования была подобрана лучшая модель - CatBoost, метрика на тестовой выборке составила 42,63. В модели явно прослеживается сильное переобучени. Так же по графику предсказания видно, что модель обучилась не лучшим образом и "заучила" ответы.