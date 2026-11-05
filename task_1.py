"""Task 1: simulate service-center requests with a FIFO queue."""

from itertools import count
from queue import Empty, Queue
from random import randint
from time import sleep


def generate_request(requests: Queue[int], request_id: int) -> None:
    """Add a new request with a unique ID to the end of the queue."""
    requests.put(request_id)
    print(f"Створено заявку №{request_id}")


def process_request(requests: Queue[int]) -> int | None:
    """Process the oldest request or report that the queue is empty."""
    try:
        request_id = requests.get_nowait()
    except Empty:
        print("Черга заявок порожня.")
        return None

    print(f"Оброблено заявку №{request_id}")
    requests.task_done()
    return request_id


def main() -> None:
    requests: Queue[int] = Queue()
    request_ids = count(start=1)
    print("Симуляція сервісного центру. Для виходу натисніть Ctrl+C.\n")

    try:
        while True:
            for _ in range(randint(1, 3)):
                generate_request(requests, next(request_ids))

            for _ in range(randint(1, 3)):
                process_request(requests)

            print(f"Очікують обробки: {requests.qsize()}\n")
            sleep(1)
    except KeyboardInterrupt:
        print("\nСимуляцію завершено.")


if __name__ == "__main__":
    main()
