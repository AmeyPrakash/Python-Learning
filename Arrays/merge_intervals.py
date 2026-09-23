from typing import list

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()

        result = []

        for start, end in intervals:
            # No overlap
            if not result or result[-1][1] < start:
                result.append([start, end])

            # Overlap
            else:
                result[-1][1] = max(result[-1][1], end)

        return result    