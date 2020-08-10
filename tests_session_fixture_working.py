import json
import pytest
import random

from filelock import FileLock


def random_num():
    rand_num = random.randint(0, 3) * 3
    return rand_num


@pytest.fixture(scope="session")
def get_random_num(tmp_path_factory, worker_id,
                name="random_num"):
    if not worker_id:
        # not executing in with multiple workers, just produce the data and let
        # pytest's fixture caching do its job
        return random_num()

    # get the temp directory shared by all workers
    root_tmp_dir = tmp_path_factory.getbasetemp().parent

    fn = root_tmp_dir / "data.json"
    with FileLock(str(fn) + ".lock"):
        if fn.is_file():
            data = json.loads(fn.read_text())
        else:
            data = random_num()
            fn.write_text(json.dumps(data))
    return data


def test_1(get_random_num):
    assert get_random_num > 9

def test_2(get_random_num):
    assert get_random_num > 9

def test_4(get_random_num):
    assert get_random_num > 9

def test_5(get_random_num):
    assert get_random_num > 9

def test_6(get_random_num):
    assert get_random_num > 9

def test_7(get_random_num):
    assert get_random_num > 9

def test_8(get_random_num):
    assert get_random_num > 9