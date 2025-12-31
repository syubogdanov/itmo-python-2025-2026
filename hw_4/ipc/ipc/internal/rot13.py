from string import ascii_letters


def encode(string: str, /) -> str:
    """Encode a string using the ``rot13`` cipher."""
    buffer: list[str] = []

    for char in string:
        if char not in ascii_letters:
            buffer.append(char)
            continue

        code = ord(char) + 13

        z = "z" if char.islower() else "Z"
        if code > ord(z):
            code -= 26

        new_char = chr(code)
        buffer.append(new_char)

    return "".join(buffer)


def decode(string: str, /) -> str:
    """Decode a string using the ``rot13`` cipher."""
    return encode(string)
