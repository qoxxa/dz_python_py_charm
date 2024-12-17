# Для формирования отчета необходимо:
1. Перейти в папку lesson_10
2. Ввести в терминале команду 'pytest --alluredir=./results' для создания отчёта
3. Сгенерировать отчёт в отдельную папку (final-report) командой  allure generate results -o final-report
4. Для вывода результата, ввести в терминал команду 'allure serve results' или allure open final-report (для локального просмотра)