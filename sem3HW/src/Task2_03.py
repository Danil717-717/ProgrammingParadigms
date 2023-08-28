
from abc import ABC, abstractmethod


class Sort(ABC):
    @abstractmethod
    def sort(self, nums):
        pass

class BubbleSort(Sort):
    def sort(self, nums):
        n=1
        while n < len(nums):
            for i in range(len(nums)-n):
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1],nums[i]
            n+=1
        return nums  


class SelectionSort(Sort):
    def sort(self, nums):
        for i in range(len(nums)):
            lowest_value_index = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[lowest_value_index]:
                    lowest_value_index = j
            nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]

class SortStrategy:
    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy):
        self.strategy = strategy

    def sort(self, nums):
        if self.strategy is None:
            raise ValueError("Strategy is not set")
        return self.strategy.sort(nums)


array = [1, 7, 3, 48, 35, 6, 4]
print(array)
#Создаем объекты стратегий
bubble_sort = BubbleSort()
selection_sort = SelectionSort()

#Создаем объект для работы со стратегиями сортировки
sort_strategy = SortStrategy()

#Устанавливаем стратегию сортировки и выполняем сортировку
sort_strategy.set_strategy(bubble_sort)
sorted_array = sort_strategy.sort(array)
print("Buble sort: ", sorted_array)

sort_strategy.set_strategy(selection_sort)
sorted_array = sort_strategy.sort(array)
print("Selection Sort:", sorted_array)


