#!/usr/bin/env python3
class CountedIterator:
    """
    A custom iterator class that counts how many items have been iterated over.
    """

    def __init__(self, iterable):
        """
        Initializes the CountedIterator with an iterable and a counter.

        Parameters:
        - iterable: An iterable object (e.g., list, tuple) that will be iterated over.
        """
        self.iterator = iter(iterable)
        self.compteur = 0

    def get_count(self):
        """
        Returns the number of items that have been iterated over so far.
        """
        return self.compteur

    def __next__(self):
        """
        Returns the next item from the iterator and increments the counter.
        If the iterator is exhausted, it raises the StopIteration exception.
        """
        try:
            item = next(self.iterator)
            self.compteur += 1
            return item

        except StopIteration:
            raise StopIteration
