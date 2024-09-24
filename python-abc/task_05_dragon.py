#!/usr/bin/python3
class SwimMixin:
    """
    Mixin class that adds swimming ability.
    The swim method prints a message indicating the creature is swimming.
    """

    def swim(self):
        print("The creature swims! ")


class FlyMixin:
    """
    Mixin class that adds flying ability.
    The fly method prints a message indicating the creature is flying.
    """

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    The Dragon class inherits from both SwimMixin and FlyMixin.
    This means a Dragon can both swim and fly.
    The roar method prints a message indicating the dragon is roaring.
    """

    def roar(self):
        print("The dragon roars!")
