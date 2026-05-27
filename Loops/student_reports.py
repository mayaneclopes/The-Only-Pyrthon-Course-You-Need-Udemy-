# You’re building a simple student report generator that combines names and scores.
# Tasks:
# Define a function generate_score_report that takes two lists — one with student names and one with their scores.
# Use the zip() function to pair each student with their score.
# Return a list of strings in the format "Name scored X marks"

def generate_score_report(names: list[str], scores: list[int]) -> list[str]:
    total = []
    for name, score in zip(names, scores):
        total.append(f"{name} scored {score} marks")
    return total