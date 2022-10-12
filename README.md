### Hexlet tests and linter status:
[![Actions Status](https://github.com/vadim-gusak/python-project-lvl1/workflows/hexlet-check/badge.svg)](https://github.com/vadim-gusak/python-project-lvl1/actions)
<a href="https://codeclimate.com/github/vadim-gusak/python-project-lvl1/maintainability"><img src="https://api.codeclimate.com/v1/badges/7945af54480e986ea869/maintainability" /></a>
# Игры разума

Добро пожаловать в мой учебный проект "Игры разума" с портала Hexlet.io.

## Описание

«Игры разума» — набор из пяти консольных игр, построенных по принципу популярных мобильных приложений для прокачки мозга. Каждая игра задает вопросы, на которые нужно дать правильные ответы. После трех правильных ответов считается, что игра пройдена. Неправильные ответы завершают игру и предлагают пройти ее заново. Игры:

Калькулятор. Арифметические выражения, которые необходимо вычислить. Прогрессия. Поиск пропущенных чисел в последовательности чисел. Определение четного числа. Определение наибольшего общего делителя. Определение простого числа.

## Установка и использование

Для сборки проекта использовался Poetry ver. 1.1.14. Для установки вам также потребуется PIP.
В корневой дирректории подготовлен Makefile с необходимыми коммандами:

```commandline
make build
```
```commandline
make package-install
```

После установки игры можно запустить следующими командами:
```commandline
brain-even
```
```commandline
brain-calc
```
```commandline
brain-gcd
```
```commandline
brain-progression
```
```commandline
brain-prime
```

Ниже вы можете увидеть примеры запуска и работы игр:

**Brain even**:

<a href="https://asciinema.org/a/515591?t=20" target="_blank"><img src="https://asciinema.org/a/515591.svg" /></a>


**Brain calc**:

<a href="https://asciinema.org/a/515795" target="_blank"><img src="https://asciinema.org/a/515795.svg" /></a>


**Brain GCD**:

<a href="https://asciinema.org/a/515803" target="_blank"><img src="https://asciinema.org/a/515803.svg" /></a>


**Brain progression**:

<a href="https://asciinema.org/a/515831" target="_blank"><img src="https://asciinema.org/a/515831.svg" /></a>


**Brain prime**:

<a href="https://asciinema.org/a/515840" target="_blank"><img src="https://asciinema.org/a/515840.svg" /></a>
