
from abc import abstractmethod


class Sort():
    @abstractmethod
    def sort(self):
        pass

class BubbleSort(Sort):
    def sort(nums):
        n=1
        while n < len(nums):
            for i in range(len(nums)-n):
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1],nums[i]
            n+=1
        return(nums)  


class SelectionSort(Sort):
    def sort(nums):
    # Значение i соответствует кол-ву отсортированных значений
        for i in range(len(nums)):
             # Исходно считаем наименьшим первый элемент
            lowest_value_index = i
            # Этот цикл перебирает несортированные элементы
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[lowest_value_index]:
                    lowest_value_index = j
            # Самый маленький элемент меняем с первым в списке
            nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]

class SortStrategy:
    def strategy(self, strategy):
        self.strategy = strategy

    def sort(nums):
        return #????????
    
    #def sort(numbers):
     #   return

array = [1, 7, 3, 48, 35, 6, 4]
print(array)
strateg = SortStrategy()
strateg.strategy(BubbleSort())
strateg.sort(array)
print(array)
