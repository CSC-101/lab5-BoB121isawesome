import data, math

# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.


# Part 2
   # The function for Part 2 should be within the class in data.py.


# Part 3
# Adds two time objects and returns the resulting time, adjusting for seconds and minutes overflow.
# Parameters: time1 and time 2 (data.Time): objects with hour, minute, and second attributes.
# Returns: data.Time: A new time object representing the sum of the two input times.
def time_add(time1,time2):
    sum_time = data.Time(0,0,0)
    sum_time.second = time1.second+time2.second
    sum_time.minute = time1.minute+time2.minute
    sum_time.hour = time1.hour+time2.hour
    while sum_time.second>=60:
        sum_time.second=sum_time.second-60
        sum_time.minute=sum_time.minute+1
    while sum_time.minute>=60:
        sum_time.minute=sum_time.minute-60
        sum_time.hour=sum_time.hour+1
    return sum_time

# Part 4
# Checks if a list of numbers is in strictly descending order.
# Parameters: num_list (list[float]): A list of floating-point numbers to check.
# Returns: bool: True if the list is in strictly descending order, otherwise False.
def is_descending(num_list:list[float]):
    for i in range(len(num_list)-1):
        if num_list[i] <= num_list[i+1]:
            return False
    return True

# Part 5
# Finds the index of the largest element within a specified range in a list.
# Parameters: num_list (list[float]): A list of floating-point numbers,
#     lower (int): The starting index of the range to search within,
#     upper (int): The ending index of the range to search within.
# Returns: int: The index of the largest element between the specified indices.
def largest_between(num_list,lower:int,upper:int):
    largest_index=lower
    for i in range(lower,upper):
        if num_list[largest_index]<num_list[i+1]:
            largest_index=i+1
    return largest_index

# Part 6
# Calculates the Euclidean distance between two points.
def distance(point1, point2):
    return math.sqrt((point1.x-point2.x)**2+(point1.y-point2.y)**2)
#Finds the point furthest from the origin in a list of points.
# Parameters: list_points (list[data.Point]): A list of Point objects, each with x and y coordinates.
# Returns: data.Point or None: The point furthest from the origin or None if the list is empty.
def furthest_from_origin(list_points:list[data.Point]):
    furthest_point = data.Point(0,0)
    if len(list_points)==0:
        return None
    else:
        for i in range(len(list_points)):
            if distance(list_points[i],data.Point(0,0))>distance(furthest_point,data.Point(0,0)):
                furthest_point=list_points[i]
        return furthest_point