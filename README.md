## Описание
В проекте требуется написать набор бенчмарк-тестов, которые покажут скорость работы разных версий одного и того же метода. Время работы коротких методов обычно изменяется в наносекундах и сильно зависит от текущего состояния операционной системы, поэтому такие замеры делаются при помощи специальных библиотек.

## Функциональные требования
- Написать бенчмарк-тест для каждого варианта метода (см инструкцию по реализации).
- Использовать профильный фреймворк (подключить как библиотеку):
  - Java/Scala: JMH
  - Python: pytest-benchmark
  - Go: https://go.dev/wiki/Benchmarks

## Нефункциональные требования
Опубликуйте финальную таблицу результатов запуска тестов.

## Инструкции по реализации
Требуется реализовать и сравнить производительность следующих сценариев:
- Сравнение скорости создания списка при помощи:
  - списковых включений (list comprehensions)
  - обычных циклов for
  - библиотеки numpy
- Сравнение скорости сериализации и десериализации данных
  - Сравнить форматы pickle, json, msgpack
  - В сравнении нужно добавить параметризацию по размеру объекта: 1КБ, 1МБ, 10МБ
- Сравнение скорости конкатенации строк через += и .join

## Справочные материалы
Java / Scala

    Цикл статей про рефлексию:
    https://blogs.oracle.com/javamagazine/post/java-reflection-introduction
    https://blogs.oracle.com/javamagazine/post/java-reflection-performance
    https://blogs.oracle.com/javamagazine/post/java-reflection-method-handles
    Полезные ссылки:
    https://github.com/openjdk/jmh/tree/master/jmh-samples/src/main/java/org/openjdk/jmh/samples
    https://habr.com/ru/articles/318418/
    https://habr.com/ru/companies/haulmont/articles/431922/
    https://habr.com/ru/companies/haulmont/articles/432418/

Go

    https://blog.logrocket.com/benchmarking-golang-improve-function-performance

Python

    https://pytest-with-eric.com/pytest-best-practices/pytest-benchmark

## Критерии оценки
За задание можно получить 90 баллов.
