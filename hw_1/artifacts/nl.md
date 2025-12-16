# nl

## Окружение

```shell
$ cd nl/
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install poetry==2.1.3
$ poetry install
```

## Подсказка

```shell
$ python -m nl --help
usage: nl [-h] [file]

nl -- line numbering filter

positional arguments:
  file        file to read (default: stdin)

options:
  -h, --help  show this help message and exit
```

## Стандартный поток ввода

```shell
$ echo "Hello\nPython" > text.txt
$ cat text.txt | python -m nl
     1  Hello
     2  Python
```

## Файл

```shell
$ echo "Hello\nPython" > text.txt
$ python -m nl text.txt
     1  Hello
     2  Python
```

## Обработка ошибок

```shell
$ mkdir dir/
$ python -m nl dir/
usage: nl [-h] [file]
nl: error: [Errno 21] Is a directory: 'dir'
```
