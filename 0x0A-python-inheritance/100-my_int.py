#!/usr/bin/python3
""" 12. My integer """


class MyInt(int):
    """ a class MyInt that inherits from int """
    def __eq__(self, other):
        """Overides and inverts == operator"""
        return int(self) != int(other)

    def __ne__(self, other):
        """Overides and inverts != operator"""
        return int(self) == int(other)
