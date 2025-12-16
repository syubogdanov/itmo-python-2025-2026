# wc

## Окружение

```shell
$ cd wc/
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install poetry==2.1.3
$ poetry install
```

## Подсказка

```shell
$ python -m wc --help
usage: wc [-h] [file ...]

wc -- word, line, character, and byte count

positional arguments:
  file        file to read (default: stdin)

options:
  -h, --help  show this help message and exit
```

## Стандартный поток ввода

```shell
$ echo "a\nb c\nd e f" > text.txt
$ cat text.txt | python -m wc
       3        6       12
```

## Файл

```shell
$ echo "a\nb c\nd e f" > text.txt
$ python -m wc text.txt
       3        6       12 text.txt
```

## Коллекция файлов

```shell
$ echo "a\nb c\nd e f" > text1.txt
$ echo "g\nh i\nj k l" > text2.txt
$ python -m wc text1.txt text2.txt
       3        6       12 text1.txt
       3        6       12 text2.txt
       6       12       24 total
```

## Обработка ошибок

```shell
$ mkdir dir/
$ python -m wc dir/
usage: wc [-h] [file]
wc: error: [Errno 21] Is a directory: 'dir'
```
