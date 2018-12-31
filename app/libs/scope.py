class Scope:
    allow_api = []

    def __add__(self, other):
        self.allow_api = self.allow_api + other.allow_api
        self.allow_api = list(set(self.allow_api))


class UserScope(Scope):
    allow_api = ['api.get_user', 'api.book_search', 'api.book_detail',
                 'api.save_to_gifts', 'api.get_wishes', 'api.save_to_wish']


class AdminScope(Scope):
    allow_api = ['api.get_admin_users']

    def __init__(self):
        self+UserScope()
        print(self.allow_api)

# class SuperScope(Scope):
#     allow_api = ['api.C', 'api.D']
#
#     def __init__(self):
#         self+AdminScope()
#         print(self.allow_api)


def is_in_scope(scope, endpoint):
    scope = globals()[scope]()
    if endpoint in scope.allow_api:
        return True
    else:
        return False