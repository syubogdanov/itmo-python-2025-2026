import sys

from argparse import ArgumentParser
from pathlib import Path

import latex


def main() -> None:
    """Run the program."""
    parser = ArgumentParser("latex", description="latex -- like LaTex, but... worse...")
    parser.add_argument("--width", type=int, required=True, help="the matrix width")
    parser.add_argument("--height", type=int, required=True, help="the matrix height")
    parser.add_argument("--image", type=Path, required=True, help="path to the image")

    args = parser.parse_args()

    if args.width <= 0:
        detail = "'--width' must be positive"
        parser.error(detail)

    if args.height <= 0:
        detail = "'--height' must be positive"
        parser.error(detail)

    matrix = [[f"({row}, {col})" for col in range(args.width)] for row in range(args.height)]

    table = latex.table(matrix)
    image = latex.image(args.image)

    contents = latex.join(table, image)
    document = latex.document(contents)

    try:
        path = latex.to_pdf(document)

    except Exception as exception:
        detail = str(exception)
        parser.error(detail)

    print(path.as_posix(), file=sys.stdout)


if __name__ == "__main__":
    main()
