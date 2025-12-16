# tail

## Окружение

```shell
$ cd tail/
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install poetry==2.1.3
$ poetry install
```

## Подсказка

```shell
$ python -m tail --help
usage: tail [-h] [file ...]

tail -- display the last part of a file

positional arguments:
  file        file to read (default: stdin)

options:
  -h, --help  show this help message and exit
```

## Стандартный поток ввода

```shell
$ echo "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n16\n17\n18" > text.txt
$ cat text.txt | python -m tail
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
```

## Файл

```shell
$ echo "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11" > text.txt
$ python -m tail text.txt
2
3
4
5
6
7
8
9
10
11
```

## Коллекция файлов

```shell
$ echo "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11" > text1.txt
$ echo "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11" > text2.txt
$ python -m tail text1.txt text2.txt
==> text1.txt <==
2
3
4
5
6
7
8
9
10
11

==> text2.txt <==
2
3
4
5
6
7
8
9
10
11
```

## Обработка ошибок

```shell
$ mkdir dir/
$ python -m tail dir/
usage: tail [-h] [file]
tail: error: [Errno 21] Is a directory: 'dir'
```
