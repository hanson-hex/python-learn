def customer():
    r = ''
    print("111")
    while True:
        n = yield r
        print("custome 序号{}".format(n))
        r = "200 OK"

def producer(c):
    print("000")
    c.send(None)
    print("333")
    n = 0
    while n < 5:
        n += 1
        print("produce 序号{}".format(n))
        r = c.send(n)
        print(r)


c = customer()
producer(c)

