import random
import matplotlib.pyplot as plt


def simulate_dice_rolls(num_rolls):
    sums = {}

    for _ in range(num_rolls):
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        sum = dice_1 + dice_2
        sums[sum] = sums.get(sum, 0) + 1

    probabilities = {key: value/num_rolls for (key, value) in sums.items()}

    return probabilities

def plot_probabilities(probabilities: dict):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())

    # Create the gragh
    plt.bar(sums, probs, tick_label=sums)
    plt.xlabel("Sum of the number on the dice")
    plt.ylabel("Probability")
    plt.title("Probability of the number's sum on two dice")

    for i, prob in enumerate(probs):
        plt.text(sums[i], prob, f"{prob*100:.2f}%", ha="center")

    plt.show()


if __name__ == "__main__":
    for accuracy in [100, 1000, 100000]:
        probabilities = simulate_dice_rolls(accuracy)

        plot_probabilities(probabilities)