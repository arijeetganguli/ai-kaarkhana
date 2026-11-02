import threading


def run_concurrently(inventory, workers, qty=1):
    results = []
    barrier = threading.Barrier(workers)

    def worker():
        barrier.wait()
        results.append(inventory.reserve(qty))

    threads = [threading.Thread(target=worker) for _ in range(workers)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return results


def test_sequential_reservations_work(target):
    inv = target.Inventory(2)
    assert inv.reserve(1) is True
    assert inv.reserve(1) is True
    assert inv.reserve(1) is False
    assert inv.stock == 0


def test_never_oversells_under_concurrency(target):
    inv = target.Inventory(10)
    results = run_concurrently(inv, workers=50)
    assert sum(results) == 10, "exactly the available stock may be reserved"
    assert inv.stock == 0, "stock must never go negative"


def test_a_large_request_cannot_sneak_in_between_check_and_update(target):
    inv = target.Inventory(5)
    results = run_concurrently(inv, workers=8, qty=3)
    assert sum(results) == 1  # only one request of 3 fits into 5
    assert inv.stock == 2
