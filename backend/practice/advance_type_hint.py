from typing import List, Union, Optional


# .............................
from typing import Callable

def smart_divide(func: Callable[[int, int], float]):
    def inner(a, b):
        if b == 0:
            print("Whoops! Division by 0")
            return None
        return func(a, b)
    return inner

@smart_divide
def divide(a, b):
    print(a/b)

divide(6, 0)
    


# .........................

# class Job:
#     def __init__(self, title: str, description: Optional[str]) -> None:
#         self.title = title
#         self.description = description

#     def __repr__(self):
#         return self.title
    
# job1 = Job(title="Team Lead", description=" Leads the team from technical aspect")
# job2 = Job(title="Senior Manager", description="Manager")

# jobs: List[Job] = [job1, job2]
# print(jobs)



# ....................

# Image= List[List[int]]

# def flatten(pic: Image) -> List:
#     flat_list = []
#     for sublist in pic:
#         flat_list.extend(sublist)
#     return flat_list

# curr_list = flatten([[1, 2, 3], [4, 5, 6]])
# print(curr_list)



# .................
# x: List[Union[int, float]] = [1.2, 4, 3.55]

# ................

# def inr_to_usd(value: float) -> Union[float, None]:
#     try:
#         conversion_factor = 75
#         value = value / conversion_factor
#         return value
#     except Exception as e:
#         print(e)
#         return None
    
# converted_currency = inr_to_usd(80)
# print(converted_currency)
