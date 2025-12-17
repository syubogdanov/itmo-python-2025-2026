from os import PathLike
from pathlib import Path
from textwrap import dedent


def is_table(matrix: list[list[str]]) -> bool:
    """Check if the matrix is a table."""
    if not matrix:
        return False

    if not all(row for row in matrix):
        return False

    width = len(matrix[0])
    return all(len(row) == width for row in matrix)


def join(*latex: str) -> str:
    """Join the *LaTex*."""
    return "\n".join(latex)


def document(
    latex: str,
    *,
    title: str = "title",
    author: str = "author",
) -> str:
    """Wrap as a document."""
    prefix = dedent(
        rf"""
        \documentclass{{article}}
        \usepackage[utf8]{{inputenc}}
        \usepackage[russian]{{babel}}
        \usepackage{{array}}
        \usepackage{{float}}
        \usepackage{{graphicx}}
        \title{{{title}}}
        \author{{{author}}}
        \begin{{document}}
        \maketitle
        """,
    )
    suffix = dedent(
        r"""
        \end{document}
        """,
    )
    chunks = [prefix, latex, suffix]
    return "\n".join(chunks)


def table(matrix: list[list[str]]) -> str:
    """Format the *LaTex* table."""
    if not is_table(matrix):
        detail = "The matrix is not a table"
        raise ValueError(detail)

    matrix = [[escape(cell) for cell in row] for row in matrix]
    width = len(matrix[0])

    formatter = "c".join("|" for _ in range(width + 1))
    lines = [r"\begin{center}", rf"\begin{{tabular}}{{{formatter}}}", r"\hline"]

    for row in matrix:
        line = " & ".join(row) + r" \\ \hline"
        lines.append(line)

    lines.append(r"\end{tabular}")
    lines.append(r"\end{center}")

    return "\n".join(lines)


def image(
    path: str | PathLike,
    *,
    label: str = "label",
    caption: str = "caption",
) -> str:
    """Format the *LaTex* image."""
    path = Path(path).resolve(strict=True)
    path = escape(path.as_posix())

    label = escape(label)
    caption = escape(caption)

    text = dedent(
        rf"""
        \begin{{figure}}[ht]
            \centering
            \includegraphics{{{path}}}
            \caption{{{caption}}}
            \label{{{label}}}
        \end{{figure}}
        """,
    )

    return text.strip()


def escape(text: str) -> str:
    """Escape the text."""
    replacements = {
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\^{}",
        "\\": r"\textbackslash{}",
        "<": r"\textless{}",
        ">": r"\textgreater{}",
    }
    chars = (replacements.get(char, char) for char in str(text))
    return "".join(chars)
