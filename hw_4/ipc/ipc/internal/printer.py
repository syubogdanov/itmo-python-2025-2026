from datetime import UTC, datetime
from multiprocessing import Lock


class Printer:
    """The printer."""

    def __init__(self) -> None:
        """Initialize the object."""
        self._lock = Lock()

    def print(self, message: str, /, *, name: str) -> None:
        """Print a message."""
        timestamp = datetime.now(UTC).isoformat()
        with self._lock:
            print(f"[{timestamp}] [{name}] {message}", flush=True)
