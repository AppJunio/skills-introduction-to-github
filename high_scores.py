def display_high_scores(scores):
  """Displays the high scores."""
  print("🏆 High Scores 🏆")
  for i, score in enumerate(scores):
    print(f"{i + 1}. {score}")

def add_new_score(scores, new_score):
  """Adds a new score to the list and keeps it sorted."""
  scores.append(new_score)
  scores.sort(reverse=True) # Sort in descending order
  return scores[:5] # Keep only the top 5 scores

# Initial high scores
high_scores = [1200, 1050, 900, 850, 700]

display_high_scores(high_scores)

# Add a new score
new_score = 1100
high_scores = add_new_score(high_scores, new_score)

print("\nAfter adding a new score:")
display_high_scores(high_scores)
