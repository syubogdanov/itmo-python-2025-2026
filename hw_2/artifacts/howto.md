# LaTex

## PyPI

### URL

* <https://test.pypi.org/project/junk-syubogdanov/>

### Installation

```shell
$ pip install -i https://test.pypi.org/simple/ junk-syubogdanov
```

## Docker

### Build

```shell
$ cd hw_2/
$ docker build --tag latex .
```

### Run

```shell
$ docker run --rm latex --width 10 --height 10 --image /itmo/images/image.png
/tmp/tmpi595_4gf/document.pdf
```

## Usage

### Help

```shell
$ python -m latex --help
usage: latex [-h] --width WIDTH --height HEIGHT --image IMAGE

latex -- like LaTex, but... worse...

options:
  -h, --help       show this help message and exit
  --width WIDTH    the matrix width
  --height HEIGHT  the matrix height
  --image IMAGE    path to the image
```

### PDF

```
$ python -m latex --width 10 --height 10 --image ./images/image.png
/var/folders/kq/qh0cn4dn107grmqkthnyk8ph0000gq/T/tmpzbujz6pp/document.pdf
```
