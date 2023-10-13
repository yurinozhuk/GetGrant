"""Method that contains Custom Assertion class and methods"""


class AssertionUtils:
    @staticmethod
    def contains_any(container, elements):
        """
        Check if the container contains any of the given elements.

        :param container: The container to check.
        :param elements: List of elements to look for.
        :return: True if any element is found, False otherwise.
        """
        return any(element in container for element in elements)

    @staticmethod
    def not_empty(data):
        """
        Check if the data is not empty.

        :param data: The data to check.
        :return: True if the data is not empty, False otherwise.
        """
        return bool(data)

    @staticmethod
    def is_empty(data):
        """
        Check if the data is empty.

        :param data: The data to check.
        :return: True if the data is empty, False otherwise.
        """
        return not bool(data)

    @staticmethod
    def is_false(expression):
        """
        Check if the expression evaluates to False.

        :param expression: The expression to check.
        :return: True if the expression is False, False otherwise.
        """
        return expression is False

    @staticmethod
    def is_true(expression):
        """
        Check if the expression evaluates to True.

        :param expression: The expression to check.
        :return: True if the expression is True, False otherwise.
        """
        return expression is True

    @staticmethod
    def less_equal(value1, value2):
        """
        Check if value1 is less than or equal to value2.

        :param value1: The first value.
        :param value2: The second value.
        :return: True if value1 is less than or equal to value2, False otherwise.
        """
        return value1 <= value2

    @staticmethod
    def greater_equal(value1, value2):
        """
        Check if value1 is greater than or equal to value2.

        :param value1: The first value.
        :param value2: The second value.
        :return: True if value1 is greater than or equal to value2, False otherwise.
        """
        return value1 >= value2

    @staticmethod
    def less_than(value1, value2):
        """
        Check if value1 is less than value2.

        :param value1: The first value.
        :param value2: The second value.
        :return: True if value1 is less than value2, False otherwise.
        """
        return value1 < value2

    @staticmethod
    def greater_than(value1, value2):
        """
        Check if value1 is greater than value2.

        :param value1: The first value.
        :param value2: The second value.
        :return: True if value1 is greater than value2, False otherwise.
        """
        return value1 > value2

    @staticmethod
    def not_equals(value1, value2):
        """
        Check if value1 is not equal to value2.

        :param value1: The first value.
        :param value2: The second value.
        :return: True if value1 is not equal to value2, False otherwise.
        """
        return value1 != value2

    @staticmethod
    def equals(value1, value2):
        """
        Check if value1 is equal to value2.

        :param value1: The first value.
        :param value2: The second value.
        :return: True if value1 is equal to value2, False otherwise.
        """
        return value1 == value2
