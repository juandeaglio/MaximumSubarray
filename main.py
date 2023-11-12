from abc import abstractmethod, ABC
from math import ceil
from typing import List, Callable, Protocol


class Sub_Array_Strategy(ABC):
    def solve_sub_array(self, nums: List[int]) -> int:
        pass

class Sliding_Window_Strategy(Sub_Array_Strategy):
    def solve_sub_array(self, nums: List[int]) -> int:
        index = 0
        window = 1
        max_sum = 0
        while index < len(nums):
            if sum(nums[index:index+window]) > max_sum:
                max_sum = sum(nums[index:index+window])
                window += 1
            else:
                index += window
        return max_sum


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return Sliding_Window_Strategy().solve_sub_array(nums)


class Test:
    def __init__(self, expected: int, input: List[int]):
        self.expected = expected
        self.input = input

class TestRunner:
    def run_tests(self, tests: List[Test], tested_function: Callable):
        failed_test_output: List[str] = []
        passed_test_output: List[str] = []
        for test in tests:
            truncated_input = str(test.input)[0:100]
            try:
                output: str = tested_function(test.input)
                assert test.expected == output
                passed_test_string = f"Test passed: For {truncated_input} received {output}"
                passed_test_output.append(passed_test_string)
            except AssertionError:
                failed_test_string = f"Test failed: For {truncated_input} received {output}, expected {test.expected}"
                failed_test_output.append(failed_test_string)

        if len(failed_test_output) > 0:
            print("Failed tests:")
            for failed_test in failed_test_output:
                print(failed_test)

            return len(failed_test_output)

        print("All tests passed")
        for passed_test in passed_test_output:
            print(passed_test)
        return 0

large_test_input: list[int] = []
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4

# generate a test case input with 10^5 elements.
# we append a number to the generate_large_test_input list, this number is either positive or negative, negatives
# become less common as we approach the center of 10**5.
# the number we append depends on how close we are to the center of 10**5 too, as we reach 10**5/2, the numbers
# become larger (positive or negative).
# as we pass 10**5, the size of the numbers returns back to 1..
# i.e. index 10**5 -1 will be equal to 1.
# index 10**5 / 2 will be equal to 10^4 or possibly -10^4
# , so we will formulate a number to append which is equal to ((i/50000) * 10^4 )
negatives = 0
largest_sum = 0
for i in range(1, ceil((10**5)/2)):
    number = (ceil(i / 50000 * 10**4))

    modulus = (negatives+1) ** 2

    if i % modulus == 0:
        number *= -1000000
        negatives += 1

    large_test_input.append(number)

for i in range(1, 50000-negatives**2):
    largest_sum += ceil((negatives**2 + i) / 50000 * 10**4)
    largest_sum += ceil((negatives**2 + i) / 50000 * 10**4)

for i in range(1, ceil((10**5)/2)):
    number = ceil((50000-i) / 50000 * 10**4)

    modulus = (negatives) ** 2

    if modulus != 0 and  (50000-i) % modulus == 0:
        number *= -1000000
        negatives -= 1

    large_test_input.append(number)



# write generate_large_test_input to a file
with open("large_test_input.txt", "w") as file:
    file.write(str(large_test_input))
    file.close()

tests = [
    Test(expected=1, input=[1]),
    Test(expected=largest_sum, input=large_test_input),
]

tested_function = Solution().maxSubArray
TestRunner().run_tests(tests, tested_function)

tested_function = Solution().maxSubArray
if __name__ == "__main__":
    # return function to stdout
    exit_code = TestRunner().run_tests(tests, tested_function)
    exit(exit_code)