
class Scope():
    def add(self, other):
        # 集合的合并
        self.allow_api = self.allow_api | other.allow_api
        return self


class AdminScope(Scope):
    allow_api = {'super_get_user', 'super_delete_user'}

    def __init__(self):
        self.add(UserScope())
        print(self.allow_api)


class UserScope(Scope):
    allow_api = {'user'}


AdminScope()