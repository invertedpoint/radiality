"""
radiality:examples:simple:human:core
"""

import eventer
import effectors


class Human(eventer.Human, effectors.Family, effectors.Animal):
    """
    TODO: Add docstring
    """
    _name: str

    def __init__(self, name: str) -> None:
        """
        TODO: Add docstring
        """
        super().__init__()

        self._name = name

    def intro(self) -> None:
        """
        TODO: Add docstring
        """
        core_id = self.__class__.__name__
        print(f'The {core_id} core running...')

    def outro(self) -> None:
        """
        TODO: Add docstring
        """
        core_id = self.__class__.__name__
        print(f'\nThe {core_id} core is stopped')


class Man(Human):
    """
    TODO: Add docstring
    """
    pass


class Woman(Human):
    """
    TODO: Add docstring
    """
    pass
