class TimeMap:

    # set("foo", "bar", 1)
    # set("foo", "baz", 3)
    # set("foo", "boo", 5)

    # store = {
    # "foo": [ ["bar", 1], ["baz", 3], ["boo", 5] ]
    #          ↑             ↑             ↑
    #        [value, ts]  [value, ts]  [value, ts]
    # }

    # TIMESTAMPS ARE ALWAYS SORTED BY DEFAULT (when added) - guaranteed by problem

    def __init__(self):
        self.store = {} # key = string, value = list of [value, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    # give me the value at timestamp time, or the closest one BEFORE timestamp
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, []) # get all timestamps under this key

        l, r = 0, len(values) - 1

        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp: # save current found best/smallest timestamp, keep searching for even higher one
                res = values[m][0]
                l = m + 1 
            else: # timestamp too big zone
                r = m - 1
        
        return res