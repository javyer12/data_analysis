# grades = [88, 92, 79, 93, 85,60]
# # sortGrades = grades.sort();

# for i in range(len(grades)):    
#     if grades[i] > 60 and grades[i] < 70:
#         print("The  grade is Novice (", grades[i], ")")
#     elif grades[i] >= 70 and grades[i] < 80:
#         print("The grade is Competent (", grades[i], ")")
#     elif grades[i] >= 80 and grades[i] < 90: 
#         print("The grade is Proficient (", grades[i], ")")
#     elif grades[i] >= 90 and grades[i] <= 100:
#         print("The grade is Expert (", grades[i], ")")
#     else:
#         print("The grade is Fail (", grades[i], ")")


# def greeting(name):
#     print("Hello, " + name + "!")

# greeting("Alice")

# # area = base * height / 2
# def calculate_triangle_area(base,height):
#     area = base * height / 2
#     return area

# print(calculate_triangle_area(5,10))

# return the largest number in a list
# def find_largest_number(numbers):
#     largest = numbers[0]
#     print("Initial largest:", largest)
#     for number in numbers:
#         if number > largest:
#             largest = number
#     return largest  

# print(find_largest_number([3, 5, 2, 8, 1]))  # Output: 8


#List   
# numbers = [1,2,3,4,5,6,]

# numbers.append(7) # add element at the end
# print(numbers) 
# numbers.remove(2) # remove element by value
# print(numbers)
# numbers.insert(2,10) # insert element at index
# print(numbers)
# numbers.pop() # remove last element
# print(numbers)

# Dictionary List
# students = [
#     {"name": "Alice", "age": 20, "grade": 88},
#     {"name": "Bob", "age": 22, "grade": 92},
#     {"name": "Charlie", "age": 19, "grade": 79}
# ]
# student = {
#     "name": "Bradly",
#     "age":21,
#     "grade":85
# }
# iterate through dictionary
# for key, value in student.items():
#     print(key, ":", value)
# iterate through dictionary= first one[0]
# for  key, value in students[0].items():
#     print(key, ":", value)

#  iterate through list of dictionaries
# for student  in students:
#     print(student["name"], "is", student["age"], "years old and scored", student["grade"])

# product ={
#     "name": "Laptop",
#     "brand": "Dell",
#     "price": 1200,
#     "specs": {
#         "processor": "Intel i7",
#         "ram": "16GB",
#         "storage": "512GB SSD"
#     },
#     "in_stock": True
# }
# product["in_stock"] = False  # update value

# for key, value in product.items():
#     print(key)

# SET= Conjuntos  List=[], set={}, dict={key,value}, tupla=()
# fruit = {"apple", "banana", "cherry"}
# fruit.add("orange")
# fruit.remove("banana")
# print(fruit)

# List comprehension
# squares = [x**2 for x in range(11)]
# print(squares)  

def practice(number_list):
    # return a even list
    even_numbers = [x for x in number_list if x % 2 == 0]
    print("Even number with List: ", even_numbers)
    # return a set of unique numbers
    unique_numbers = {x for x in [2,3,2,3,2,5,6,6,3,8,7]}
    print("Unique numbers with Set: ", unique_numbers)

    # return a dic with a square of each number
    square_dic = {x: x**2 for x in number_list}
    print("Square of each number with Dict: ", square_dic)

practice([1,2,3,4,5,6,7,8,9,10])