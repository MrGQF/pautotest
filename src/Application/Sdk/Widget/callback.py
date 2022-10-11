

def Agent(action, method, param):

    if action == "invoke":
        return invoke(method, param)
    elif action == "notify":
        return notify(method, param)
    elif action == "Query":
        return query(method, param)
    elif action == "Subscribe":
        return subscribe(method, param)
    elif action == "unsubscribe":
        return unsubscribe(method, param)


def invoke(method, param):
    return ""


def notify(method, param):
    return ""


def query(method, param):
    return ""


def subscribe(method, param):
    return method


def unsubscribe(method, param):
    return ""
