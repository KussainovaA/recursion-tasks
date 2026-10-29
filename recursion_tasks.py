
# 1. Factorial

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


print("1. Factorial:", factorial(5))


# 2. Sum of Numbers

def sum_numbers(n):
    if n == 0:
        return 0
    return n + sum_numbers(n - 1)


print("2. Sum of Numbers:", sum_numbers(5))


# 3. Power of a Number

def power(a, n):
    if n == 0:
        return 1
    return a * power(a, n - 1)


print("3. Power:", power(2, 5))


# 4. Count Digits

def count_digits(n):
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)


print("4. Count Digits:", count_digits(58321))


# 5. Sum of Digits

def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)


print("5. Sum of Digits:", sum_digits(58321))


# 6. Reverse a Number

def reverse_number(n):
    if n < 10:
        return n
    return int(str(n % 10) + str(reverse_number(n // 10)))


print("6. Reverse Number:", reverse_number(12345))


# 7. Fibonacci Number

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print("7. Fibonacci:", fibonacci(7))


# 8. Greatest Common Divisor

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


print("8. GCD:", gcd(48, 18))


# 9. Recursive Array Sum

def array_sum(arr, n):
    if n == 0:
        return 0
    return arr[n - 1] + array_sum(arr, n - 1)


arr = [2, 4, 6, 8]
print("9. Array Sum:", array_sum(arr, len(arr)))


# 10. Find the Maximum Element

def find_max(arr, n):
    if n == 1:
        return arr[0]

    maximum = find_max(arr, n - 1)

    if arr[n - 1] > maximum:
        return arr[n - 1]

    return maximum


arr = [4, 8, 2, 15, 7]
print("10. Maximum:", find_max(arr, len(arr)))


# 11. Count Occurrences

def count_occurrences(arr, x, n):
    if n == 0:
        return 0

    if arr[n - 1] == x:
        return 1 + count_occurrences(arr, x, n - 1)

    return count_occurrences(arr, x, n - 1)


arr = [2, 5, 2, 8, 2, 9]
print("11. Occurrences:", count_occurrences(arr, 2, len(arr)))


# 12. Check for Palindrome

def is_palindrome(s):
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return is_palindrome(s[1:-1])


print("12. Palindrome:", is_palindrome("level"))


# 13. Reverse a String

def reverse_string(s):
    if len(s) == 0:
        return ""

    return reverse_string(s[1:]) + s[0]


print("13. Reverse String:", reverse_string("algorithm"))


# 14. Recursive Binary Search

def binary_search(arr, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid

    if target < arr[mid]:
        return binary_search(arr, target, left, mid - 1)

    return binary_search(arr, target, mid + 1, right)


arr = [2, 4, 7, 10, 15, 21]
result = binary_search(arr, 15, 0, len(arr) - 1)

print("14. Binary Search Index:", result)


# 15. Tower of Hanoi

def hanoi(n, source, auxiliary, destination):
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return

    hanoi(n - 1, source, destination, auxiliary)

    print("Move disk", n, "from", source, "to", destination)

    hanoi(n - 1, auxiliary, source, destination)


print("15. Tower of Hanoi:")
hanoi(3, "A", "B", "C")

print("Number of moves:", 2 ** 3 - 1)


# 16. Generate All Subsets

def subsets(arr, index, current):
    if index == len(arr):
        print(current)
        return

    subsets(arr, index + 1, current)

    subsets(arr, index + 1, current + [arr[index]])


print("16. All Subsets:")
subsets([1, 2, 3], 0, [])


# 17. Generate All Permutations

def permutations(s, current):
    if len(s) == 0:
        print(current)
        return

    for i in range(len(s)):
        permutations(s[:i] + s[i+1:], current + s[i])


print("17. All Permutations:")
permutations("ABC", "")


# 18. Maze Solver

def solve_maze(maze, row, col, path):
    n = len(maze)

    if row < 0 or col < 0 or row >= n or col >= n:
        return False

    if maze[row][col] == 1:
        return False

    if (row, col) in path:
        return False

    path.append((row, col))

    if row == n - 1 and col == n - 1:
        return True

    if solve_maze(maze, row + 1, col, path):
        return True

    if solve_maze(maze, row, col + 1, path):
        return True

    if solve_maze(maze, row - 1, col, path):
        return True

    if solve_maze(maze, row, col - 1, path):
        return True

    path.pop()
    return False


maze = [
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 0, 0, 0]
]

path = []

print("18. Maze Solver:")

if solve_maze(maze, 0, 0, path):
    print("Path:", path)
else:
    print("No path found")


# 19. N-Queens Problem

def solve_queens(board, row, n):
    if row == n:
        for i in range(n):
            print(board[i])
        print()
        return

    for col in range(n):
        safe = True

        for i in range(row):
            if board[i] == col:
                safe = False

            if abs(board[i] - col) == abs(i - row):
                safe = False

        if safe:
            board[row] = col
            solve_queens(board, row + 1, n)
            board[row] = -1


print("19. N-Queens:")

n = 4
board = [-1] * n

solve_queens(board, 0, n)


# 20. Recursive Binary Tree Traversal

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def preorder(root):
    if root is None:
        return

    print(root.value, end=" ")
    preorder(root.left)
    preorder(root.right)


def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.value, end=" ")
    inorder(root.right)


def postorder(root):
    if root is None:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.value, end=" ")


root = Node(10)

root.left = Node(5)
root.right = Node(15)

root.left.left = Node(2)
root.left.right = Node(7)

root.right.right = Node(20)


print("20. Preorder:")
preorder(root)

print("\nInorder:")
inorder(root)

print("\nPostorder:")
postorder(root)

