
class Scope():
    def add(self, other):
        # 集合的合并
        self.allow_api = self.allow_api | other.allow_api
        return self


class AdminScope(Scope):
    allow_api = {'super_get_user', 'super_delete_user'}

    def __init__(self):
        self.add(UserScope())


class UserScope(Scope):
    allow_api = {'user'}


def is_in_scope(scope, endpoint):
    scope = globals()[scope]()
    if endpoint in scope:
        return True
    else:
        return False


