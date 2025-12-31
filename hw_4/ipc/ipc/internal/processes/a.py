from collections import deque
from datetime import UTC, datetime, timedelta
from multiprocessing import Queue

from ipc.internal.printer import Printer


def process(
    printer: Printer,
    input_queue: Queue,
    output_queue: Queue,
    /,
    *,
    interval: timedelta = timedelta(seconds=5.0),
) -> None:
    """Imitate a process (``A``)."""
    buffer: deque[str] = deque()
    put_at = datetime.now(UTC)

    while True:
        if buffer and datetime.now(UTC) >= put_at:
            message = buffer.popleft()

            detail = f"Flushing the buffer: {message}"
            printer.print(detail, name="A")

            output_queue.put_nowait(message)
            put_at = datetime.now(UTC) + interval

        if not input_queue.empty():
            message = input_queue.get()
            new_message = message.lower()
            buffer.append(new_message)

            detail = f"Received a message: {message}"
            printer.print(detail, name="A")
