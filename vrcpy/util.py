async def auto_page_coro(coro, *args, **kwargs):
    '''
    Auto-pages coroutines that return a list

        coro, coroutine method
        Coroutine to page, must return a list

        *args, any
        Args to pass to coro

        **kwargs, any
        Kwargs to pass to coro
    '''

    objs = []
    kwargs["offset"] = 0
    kwargs["n"] = 100
    while True:
        response = await coro(*args, **kwargs)

        objs += response
        kwargs["offset"] += 100

        if len(response) < 100:
            break

    return objs


def find_in_list_via_attribute(self, objlist, attribute, equals):
    '''
    Finds object in list via object.attribute
    Returns first matching object, or None if no match found

        objlist, list
        list to search

        attribute, str
        name of attribute to match

        equals, any
        what to match attribute to
    '''

    for x in objlist:
        if hasattr(x, attribute):
            if getattr(x, attribute) == equals:
                return x

    return None
