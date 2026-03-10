def get_float_in_range(prompt, min_value, max_value):
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if value < min_value or value > max_value:
            print(f"Out of range. Enter a number between {min_value} and {max_value}.")
            continue

        return value


def get_weights():
    while True:
        print("\nEnter category weights (percent). They must sum to 100.\n")

        w_quiz = get_float_in_range("Quizzes weight (%): ", 0, 100)
        w_part = get_float_in_range("Participation weight (%): ", 0, 100)
        w_mid = get_float_in_range("Midterm weight (%): ", 0, 100)
        w_final = get_float_in_range("Final exam weight (%): ", 0, 100)

        total = w_quiz + w_part + w_mid + w_final

        if abs(total - 100.0) <= 0.01:
            return {
                "quizzes": w_quiz,
                "participation": w_part,
                "midterm": w_mid,
                "final": w_final,
            }

        print(f"\nWeights sum to {total:.2f}, not 100. Please try again.\n")


def compute_current_contribution(scores, weights):
    return (
        scores["quizzes"] * weights["quizzes"] / 100.0
        + scores["participation"] * weights["participation"] / 100.0
        + scores["midterm"] * weights["midterm"] / 100.0
    )


def required_final_score(target_grade, current_contrib, final_weight_percent):
    if final_weight_percent <= 0:
        return float("inf") if current_contrib < target_grade else 0.0

    final_weight = final_weight_percent / 100.0
    return (target_grade - current_contrib) / final_weight


def main():
    print("=== Final Exam Score Needed Calculator ===")
    print("Categories: Quizzes, Participation, Midterm, Final Exam\n")

    weights = get_weights()

    print("\nEnter your current scores (0–100) for completed categories.\n")
    scores = {
        "quizzes": get_float_in_range("Quizzes current score (%): ", 0, 100),
        "participation": get_float_in_range("Participation current score (%): ", 0, 100),
        "midterm": get_float_in_range("Midterm score (%): ", 0, 100),
    }

    current_contrib = compute_current_contribution(scores, weights)
    w_final = weights["final"]

    print("\n--- Summary ---")
    print(f"Current weighted contribution (non-final): {current_contrib:.2f} / 100")
    print(f"Final exam weight: {w_final:.2f}%\n")

    thresholds = {
        "A": 93,
        "A-": 90,
        "B+": 87,
        "B": 83,
        "B-": 80,
        "C+": 77,
        "C": 73,
        "C-": 70,
        "D": 60,
    }

    print("Required Final Exam Scores:")
    for letter, target in thresholds.items():
        needed = required_final_score(target, current_contrib, w_final)

        if needed == float("inf"):
            msg = "N/A (final weight is 0%)"
        elif needed <= 0:
            msg = "0.00% (already secured)"
        elif needed > 100:
            msg = f"{needed:.2f}% (not possible)"
        else:
            msg = f"{needed:.2f}%"

        print(f"  {letter:>2} (>= {target}): {msg}")


if __name__ == "__main__":
    main()