FROM python:3.13-slim

WORKDIR /itmo/

RUN apt-get update && apt-get install -y \
    texlive-base \
    texlive-fonts-recommended \
    texlive-latex-recommended \
    texlive-latex-extra \
    texlive-lang-cyrillic \
    ghostscript \
    poppler-utils

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -i https://test.pypi.org/simple/ junk-syubogdanov

COPY images/ images/

ENTRYPOINT ["python", "-m", "latex"]
CMD ["--help"]
