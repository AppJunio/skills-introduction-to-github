A common use case for an array is to store and manage a high score leaderboard in a game. Let's say we want to keep track of the top 5 scores. An array is a suitable choice for this because we have a fixed number of scores to store.

In Python, the built-in list type is often used as a dynamic array, meaning it can grow and shrink in size. While Python doesn't have a strict, fixed-size array in its core language, you can enforce a fixed size in your logic. For a more traditional, typed array, you can use the array module or the popular NumPy library. For simplicity, we'll use a standard Python list here.

Explanation:

1. We start with an initial list of high scores.
2. The "display_high_scores" function iterates through the list and prints each score.
3. The "add_new_score" function appends a new score, sorts the list in descending order, and then returns a new list containing only the top 5 scores.
