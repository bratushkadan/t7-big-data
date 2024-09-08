class Processor:
    _files = dict()
    _action_permission_map = {
        "read": "r",
        "write": "w",
        "execute": "x",
    }

    @staticmethod
    def _get_default_permissions() -> dict:
        return {"r": False, "w": False, "x": False}

    def add(self, file: str, permissions: list[str]):
        p = self._files.get(file)
        if not p:
            p = Processor._get_default_permissions()
            self._files[file] = p
        for _, perm in enumerate(permissions):
            self._files[file][perm] = True

    def authorize(self, file: str, action: str) -> str:
        perm = self._action_permission_map[action]
        if self._files[file][perm]:
            return "OK"
        return "Access denied"


if __name__ == "__main__":
    n = int(input())
    p = Processor()
    for i in range(n):
        file, *permissions = input().split()
        p.add(file, permissions)
    k = int(input())
    for i in range(k):
        action, file = input().split()
        print(p.authorize(file, action))
