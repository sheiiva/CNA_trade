#  B4 - COMPUTER NUMERICAL ANALYSIS
#      -----------------------
#           TRADE PROJECT
#
# Repository:
# https://github.com/sheiiva/CNA_trade
#
# (05/19/2020)
# Authors:  Corentin COUTRET-ROZET  <corentin.rozet@epitech.eu>
#           Patricia Monfa-Matas    <patricia.monfa-matas@epitech.eu>
#


class Compute():
    """
    Provide computing tools or specific trading computations.
    """

    def isInt(self, value) -> bool:
        """
        Check for value's type.

        Args:
            value ([type]): Value to be tested.

        Returns:
            bool: Return True if 'value' is an int. Return False otherwise.
        """

        try:
            int(value)
        except ValueError:
            return False
        else:
            return True

    def isFloat(self, value) -> bool:
        """
        Check for value's type.

        Args:
            value ([type]): Value to be tested.

        Returns:
            bool: Return True if 'value' is a float. Return False otherwise.
        """

        try:
            float(value)
        except ValueError:
            return False
        else:
            return True
