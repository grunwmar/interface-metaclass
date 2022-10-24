""" Interface metaclass """

from typing import Callable


class InterfaceError(Exception):
    """ Base class for interface exceptions """

    def __init__(self, message: str):
        super().__init__(message)


class NotDefinedInterfaceError(InterfaceError):
    """ Raised when interface requires attributes, but they are """
    """ not present in derived class. """

    def __init__(self, undefined_items: dict):
        attr = ", ".join([f"[{k!s}:{v!r}]" for k,v in undefined_items.items()])
        super().__init__(f"Required attributes {attr} are not defined.")


class InvalidTypeInterfaceError(InterfaceError):
    """ Raised when interface requires attributes of certain types, """
    """ but the types of attributes in derived class do not agree. """

    def __init__(self, invalid_items: dict):
        attr = ", ".join([f'"attribute [{k!s}] is type {v[0]!r} not {v[1]!r}"' for k, v in invalid_items.items()])
        super().__init__(f"Invalid attributes {attr}.")


class Interface(type):
    """ Metaclass to create derived class with function of interface """
    """ which has to prevent instantiation of object """
    """ if its derived does not define required attributes. """


    def __interface_check__(mcs):
        """ Takes annotations of derived object and checks if derived object """
        """ of derived object define attributes corresponding to these """
        """ annotations. If true then creates __interface__ attribute """
        """ information about attributes required by interface and creates """
        """ instance of object. If not, throws and InterfaceError with """
        """ message containing info about invalid attributes."""

        undefined_items = {}
        invalid_items = {}
        interface_items = mcs.__annotations__

        for ann, tp in interface_items.items():
            if ann not in dir(mcs):
                undefined_items[ann] = tp
            else:
                m = getattr(mcs, ann)
                if not isinstance(m, tp):
                    invalid_items[ann] = (tp, m)

        if len(undefined_items) > 0:
            attr = ", ".join([f'"{k!s}:{v!r}"' for k,v in undefined_items.items()])
            raise NotDefinedInterfaceError(undefined_items)

        if len(invalid_items) > 0:
            raise InvalidTypeInterfaceError(invalid_items)

        mcs.__interface__ = interface_items


    def __call__(mcs, *args, **kwargs):
        called = super().__call__( *args, **kwargs)
        mcs.__interface_check__()
        return called
