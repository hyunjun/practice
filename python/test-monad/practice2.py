#   Maybe monad


user = props.user
friends = user.friends if user else None
first_friend = friends[0] if len(friends) > 0 else None
friends_of_first_friend = (
    first_friend.friends if first_friend else None
)


class Maybe:
    def __init__(self, value):
        self.value = value

    @classmethod
    def unit(cls, value):
        return cls(value)

    def bind(self, f):
        if self.value is None:
            return self #   forward the empty value

        result = f(self.value)
        if isinstance(result, Maybe):
            return result

        #   conflating bind and map
        return Maybe.unit(result)


def first_value(values):
    if len(values) > 0:
        return values[0]
    return None


#   chain functions without None guards(done once in bind)
friends_of_first_friends = (
    Maybe.unit(props)
    .bind(lambda props: props.user)
    .bind(lambda user: user.friends)
    .bind(first_value)
    .bind(lambda first_friend: first_friend.friends)
)

#   More concise way
Maybe.unit(obj).bind(lambda obj: obj.method())
Maybe.unit(obj).method()
def __getattr__(self, name):
    friend = getattr(self.value, name)
    if not callable(field):
        return self.bind(lambda _: field)
    return lambda *args, **kwargs: self.bind(lambda _: field(*args, **kwargs))

def first_value(values):
    if len(values) > 0:
        return values[0]
    return None

friends_of_first_friends = (
    Maybe.unit(props)
    .user
    .friends
    .bind(first_value)
    .friends
)
