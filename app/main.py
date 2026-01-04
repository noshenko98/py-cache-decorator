from typing import Callable


def cache(func: Callable) -> Callable:
    save_result = {}

    def wrapper(*args, **kwargs) -> Callable:
        key = tuple([f"{key} - {values}" for key, values in kwargs.items()])
        if save_result.get(args, "no_save") != "no_save" :
            print("Getting from cache")
            return save_result[args]
        elif save_result.get(key, "no_save") != "no_save" :
            print("Getting from cache")
            return save_result[key]
        elif len(args) != 0:
            save_result[args] = func(*args)
            print("Calculating new result")
            return save_result[args]
        else:
            save_result[key] = func(**kwargs)
            print("Calculating new result")
            return save_result[key]
    return wrapper
