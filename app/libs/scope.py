class scope:
    def __add__(self, other):
        pass


class UserScope():
    allow_api = ['api.get_user']


class AdminScope():
    allow_api = []


def is_in_scope(scope, endpoint):
    scope = globals()[scope]()
    print(endpoint)
    if endpoint in scope.allow_api:
        return True
    else:
        return False
