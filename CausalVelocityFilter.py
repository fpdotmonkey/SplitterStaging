from DiscreteTransferFunction import DiscreteTransferFunction


class CausalVelocityFilter(DiscreteTransferFunction):


    def __init__(self, filteringAmount, timeStepLength):

        super().__init__([filteringAmount / timeStepLength,
                          -(2*filteringAmount-1) / timeStepLength,
                          (filteringAmount-1) / timeStepLength,
                          0],
                         [1])