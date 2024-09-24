#!/usr/bin/python3

class VerboseList(list):
    """
    Subclass of the built-in list that provides verbose output
    when modifying the list (adding, removing, or popping items).
    """

    def append(self, item):
        """
        Adds an item to the list and prints a message indicating the item was added.

        Parameters:
        item (any): The item to be added to the list.
        """
        print(f"Added {[item]} to the list.")
        super().append(item)

    def extend(self, item):
        """
        Extends the list with an iterable and prints a message indicating how many items were added.

        Parameters:
        item (iterable): An iterable (e.g., list, tuple) whose items will be added to the list.
        """
        x = len(item)
        print(f"Extended the list with {[x]} items.")
        super().extend(item)

    def remove(self, item):
        """
        Removes an item from the list and prints a message if the item was successfully removed.
        Raises a ValueError if the item is not in the list.

        Parameters:
        item (any): The item to remove from the list.
        """
        if item not in self:
            raise ValueError(f"{[item]} is not in the list.")
        else:
            print(f"Removed {[item]} from the list.")
            super().remove(item)

    def pop(self, index=-1):
        """
        Removes and returns the item at the given index and prints a message.
        By default, it removes the last item in the list.

        Parameters:
        index (int, optional): The index of the item to remove. Defaults to -1 (last item).

        Returns:
        any: The item that was removed from the list.
        """
        item = super().pop(index)
        print(f"Popped {[item]} from the list.")
        return item
