def calculate_score(best_score, bonus=0):
    total = best_score + bonus
    return total


try:

    score = int(input("enter best_score:"))
    extra = input("enter bonus:")
    if extra == "":
        final = calculate_score(score)
    else:
        final = calculate_score(score, int(extra))
    print(f"result: {final}")
except ValueError:
    print("try again")
