from conn import r, rock_evict
import time

key = "_test_rock_"


def append():
    original_val = "abc"
    append_val = "_append_something"
    r.set(key, original_val)
    rock_evict(key)
    r.append(key, append_val)
    check = r.get(key)
    if check != original_val + append_val:
        raise "append fail"


def decr():
    original_num = 3433423492323
    r.set(key, original_num)
    rock_evict(key)
    res = r.decr(key)
    if res != original_num - 1:
        raise "decr fail"


def decrby():
    original_num = 3433423492323
    r.set(key, original_num)
    decrement = 123
    rock_evict(key)
    res = r.decrby(key, decrement)
    if res != original_num - decrement:
        raise "decrby fail"


def get():
    val = "abc_test_for_get"
    r.set(key, val)
    rock_evict(key)
    res = r.get(key)
    if res != val:
        raise "get fail"


def getdel():
    val = "uu_random_anything_"
    r.set(key, val)
    rock_evict(key)
    res = r.execute_command("getdel", key)  # only for 6.2
    if res != val:
        raise "getdel fail"
    exist = r.get(key)
    if exist is not None:
        raise "getdel fail2"


def getex():
    val = "hello"
    r.set(key, val)
    rock_evict(key)
    res = r.execute_command("getex", key, "ex", "1")
    if res != val:
        raise "getex fail"
    time.sleep(2)
    res = r.get(key)
    if res is not None:
        raise "getex fail"


def getset():
    original_val = "ddd"
    r.set(key, original_val)
    new_val = "ppp"
    rock_evict(key)
    res = r.getset(key, new_val)
    if res != original_val:
        raise "getset fail"
    res = r.get(key)
    if res != new_val:
        raise "getset fail2"


def incr():
    num = 34234042903402
    r.set(key, num)
    rock_evict(key)
    res = r.incr(key)
    if res != num + 1:
        raise "incr fail"


def incrby():
    num = 3249238423094
    r.set(key, num)
    rock_evict(key)
    increment = 321
    res = r.incrby(key, increment)
    if res != num + increment:
        raise "incrby fail"


def incrbyfloat():
    num = 10.5
    r.set(key, num)
    rock_evict(key)
    increment = 0.1
    res = r.incrbyfloat(key, increment)
    if res != num + increment:
        raise "incrbyfloat fail"


def mget():
    k1 = "_k1"
    v1 = "v1"
    r.set(k1, v1)
    k2 = "_k2"
    v2 = 2
    r.set(k2, v2)
    k3 = "_k3"
    v3 = 10.1
    r.set(k3, v3)
    k4 = "_k4"
    r.execute_command("del", k4)
    rock_evict(k1, k2, k3, k4)
    res = r.mget(k1, k2, k3, k4)
    if res != [v1, str(v2), str(v3), None]:
        raise "mget fail"


def psetex():
    val = "abc"
    r.set(key, val)
    rock_evict(key)
    r.psetex(key, 1, val)
    res = r.get(key)
    if res != val:
        raise "psetex fail"
    time.sleep(2)
    res = r.get(key)
    if res is not None:
        raise "psetex fail2"


def set():
    old_val = "hhh"
    r.set(key, old_val)
    rock_evict(key)
    new_val = "pxp"
    r.execute_command("set", key, new_val, "ex", "1")
    res = r.get(key)
    if res != new_val:
        raise "set fail"
    time.sleep(2)
    res = r.get(key)
    if res is not None:
        raise "set fail2"


def setex():
    val = "abc"
    r.set(key, val)
    rock_evict(key)
    new_val = "tx-"
    r.setex(key, "1", new_val)
    res = r.get(key)
    if res != new_val:
        raise "setex fail"
    time.sleep(2)
    res = r.get(key)
    if res is not None:
        raise "setex fail2"


def setrange():
    val = "Hello World"
    r.set(key, val)
    rock_evict(key)
    r.setrange(key, "6", "Redis")
    res = r.get(key)
    if res != "Hello Redis":
        raise "setrange fail"


def strlen():
    val = "akdreirjew"
    r.set(key, val)
    rock_evict(key)
    res = r.strlen(key)
    if res != len(val):
        raise "strlen fail"


def _main():
    append()
    decr()
    decrby()
    get()
    getdel()
    getex()
    getset()
    incr()
    incrby()
    incrbyfloat()
    mget()
    psetex()
    set()
    setex()
    setrange()
    strlen()


if __name__ == '__main__':
    _main()

