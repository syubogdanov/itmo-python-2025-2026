from multiprocessing import Queue

from ipc.internal import rot13
from ipc.internal.printer import Printer


def process(printer: Printer, input_queue: Queue, output_queue: Queue, /) -> None:
    """Imitate a process (``B``)."""
    while True:
        message = input_queue.get()

        detail = f"Received a message: {message}"
        printer.print(detail, name="B")

        new_message = rot13.encode(message)

        detail = f"Sending an encoded message: {new_message}"
        printer.print(detail, name="B")

        output_queue.put_nowait(new_message)
