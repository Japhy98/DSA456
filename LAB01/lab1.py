# =========================
# Part A: Required Functions
# =========================

# Function 1
def wins_rock_scissors_paper(player, opponent):
    # Normalize case
    player = player.lower()
    opponent = opponent.lower()

    # Check winning conditions
    if player == "rock" and opponent == "scissors":
        return True
    if player == "paper" and opponent == "rock":
        return True
    if player == "scissors" and opponent == "paper":
        return True

    return False


# Function 2
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Function 3
def Fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    a = 0
    b = 1

    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c

    return b


# Function 4
def sum_to_goal(numbers, goal):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == goal:
                return numbers[i] * numbers[j]
    return 0


# =========================
# Part A: Required Classes
# =========================

class UpCounter:
    def __init__(self, stepsize=1):
        self.stepsize = stepsize
        self.value = 0

    def count(self):
        return self.value

    def update(self):
        self.value += self.stepsize


class DownCounter(UpCounter):
    def update(self):
        self.value -= self.stepsize
