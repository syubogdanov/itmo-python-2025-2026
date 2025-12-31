from multiprocessing import Queue

from ipc.internal.printer import Printer


def process(printer: Printer, input_queue: Queue, output_queue: Queue, /) -> None:
    """Imitate a process (``M``)."""
    while True:
        message = input()

        detail = f"Sending a message: {message}"
        printer.print(detail, name="M")

        input_queue.put(message)

        while not output_queue.empty():
            message = output_queue.get()

            detail = f"Received an encoded message: {message}"
            printer.print(detail, name="M")
