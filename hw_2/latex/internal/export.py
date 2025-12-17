import subprocess

from pathlib import Path
from subprocess import CalledProcessError
from tempfile import NamedTemporaryFile, TemporaryDirectory


def to_tex(latex: str) -> Path:
    """Save *LaTex* as ``*.tex``."""
    with NamedTemporaryFile(mode="w", suffix=".tex", delete=False) as file:
        file.write(latex)
    return Path(file.name)


def to_pdf(latex: str) -> Path:
    """Save *LaTex* as ``*.pdf``."""
    with TemporaryDirectory(delete=False) as tmpdir:
        root = Path(tmpdir)

        tex = root / "document.tex"
        tex.write_text(latex)

        try:
            args = ["pdflatex", "-output-directory", root.as_posix(), tex.as_posix()]
            subprocess.run(args, capture_output=True, check=True)  # noqa: S603

        except CalledProcessError as exception:
            detail = "Failed to compile the document"
            raise RuntimeError(detail) from exception

    return root / "document.pdf"
