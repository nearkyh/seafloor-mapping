import itertools


class SmoothingGraph:

    def __init__(self):
        pass

    def smoothing_point(self, smoothRange):
        smoothRangeList = []
        if smoothRange:
            for i in range(-smoothRange, smoothRange + 1):
                smoothRangeList.append(i)

        # Combinations with replacement
        list_cwr = list(itertools.combinations_with_replacement(smoothRangeList, 2))
        # Permutations
        list_p = list(itertools.permutations(smoothRangeList, 2))
        sum_list = list_cwr + list_p
        # Remove duplicate elements
        duplicate_list = list(set(sum_list))
        # Remove center point(0, 0)
        duplicate_list.remove((0, 0))

        smoothing_points = duplicate_list

        return smoothing_points

    def partial_smoothing_point(self, smoothRange):
        if smoothRange == 1:
            range = self.smoothing_point(1)

            return range

        elif smoothRange == 2:
            range = self.smoothing_point(1)
            range2 = self.smoothing_point(2)
            for i in range:
                range2.remove(i)

            return range, range2

        elif smoothRange == 3:
            range = self.smoothing_point(1)
            range2 = self.smoothing_point(2)
            range3 = self.smoothing_point(3)
            for i in range2:
                range3.remove(i)
            for i in range:
                range2.remove(i)

            return range, range2, range3

        elif smoothRange == 4:
            range = self.smoothing_point(1)
            range2 = self.smoothing_point(2)
            range3 = self.smoothing_point(3)
            range4 = self.smoothing_point(4)
            for i in range3:
                range4.remove(i)
            for i in range2:
                range3.remove(i)
            for i in range:
                range2.remove(i)

            return range, range2, range3, range4
