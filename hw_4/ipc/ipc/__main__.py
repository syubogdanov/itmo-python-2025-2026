from multiprocessing import Process, Queue

from ipc.internal.printer import Printer
from ipc.internal.processes import a, b, m


def main() -> None:
    """Run the program."""
    printer = Printer()

    m_to_a = Queue()
    a_to_b = Queue()
    b_to_m = Queue()

    p1 = Process(target=a.process, args=(printer, m_to_a, a_to_b), daemon=True)
    p2 = Process(target=b.process, args=(printer, a_to_b, b_to_m), daemon=True)

    p1.start()
    p2.start()

    # Just run in the main process
    m.process(printer, m_to_a, b_to_m)


if __name__ == "__main__":
    main()
