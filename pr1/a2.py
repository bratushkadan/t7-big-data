class DB:
    _data = dict()

    def add(self, name: str) -> str:
        l = self._data.get(name)
        if not l:
            l = list()
            self._data[name] = l
        if len(l) == 0:
            l.append(name)
            return "OK"
        inserted_name = f"{name}{len(l)}"
        l.append(inserted_name)
        return inserted_name


if __name__ == "__main__":
    n = int(input())
    db = DB()
    for i in range(n):
        name = input()
        print(db.add(name))
