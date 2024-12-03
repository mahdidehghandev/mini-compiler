from lexer import Lexer
from parser import Parser
from evaluate import Evaluate
import matplotlib.pyplot as plt
import numpy as np


def read_file(entry):
    try:
        with open(entry, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{entry}' not found.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def main(file_name):
    text = read_file(file_name)
    if not text:
        return

    lexer = Lexer(text)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    parser.parse()

    print("Parsed postfix expression:")
    for i in parser.postfix:
        print(i.value, end=" ")
    print("\n")

    while True:
        print("1- without visual")
        print("2- with visual")
        print("3- find root")
        print("4- Exit")
        choice = input("--> ")

        if choice == "1":
            evaluate = Evaluate(parser.postfix)
            evaluate.evaluate()

        elif choice == "2":
            start_of_the_interval = float(input("Enter start of the interval: "))
            end_of_the_interval = float(input("Enter end of the interval: "))
            step = 0.2
            points = []

            for i in np.arange(start_of_the_interval, end_of_the_interval, step):
                evaluate = Evaluate(parser.postfix)
                y = evaluate.evaluate_with_value(i)
                points.append((i, y))

            x, y = zip(*points)
            plt.figure(figsize=(10, 6))
            plt.plot(x, y, marker='o', markersize=8, linestyle='-', linewidth=2, color='blue', label='Curve')
            plt.scatter(0, 0, color='red', s=150, label='(0, 0)', zorder=5)
            plt.axhline(0, color='gray', linewidth=3, linestyle='dashdot')
            plt.axvline(0, color='gray', linewidth=3, linestyle='dashdot')
            plt.xlabel('X', fontsize=14, weight='bold')
            plt.ylabel('Y', fontsize=14, weight='bold')
            plt.title('Visualization of (x, y) Points', fontsize=16, weight='bold')
            plt.grid(True, linewidth=1.2)
            plt.legend(fontsize=12)
            plt.show()

        elif choice == "3":
            start_of_the_interval = float(input("Enter start of the interval: "))
            end_of_the_interval = float(input("Enter end of the interval: "))
            accuracy = float(input("Enter desired accuracy: "))
            max_iterations = 1000

            evaluate = Evaluate(parser.postfix)
            y1 = evaluate.evaluate_with_value(start_of_the_interval)
            evaluate = Evaluate(parser.postfix)
            y2 = evaluate.evaluate_with_value(end_of_the_interval)

            if y1 * y2 > 0:
                print("No root found in the given interval.")
            else:
                iteration = 0
                while abs(end_of_the_interval - start_of_the_interval) > accuracy and iteration < max_iterations:
                    mid_point = (start_of_the_interval + end_of_the_interval) / 2
                    evaluate = Evaluate(parser.postfix)
                    y_mid = evaluate.evaluate_with_value(mid_point)

                    if abs(y_mid) < accuracy:
                        print(f"Root found at x = {mid_point} with y ≈ {y_mid}")
                        break

                    if y1 * y_mid < 0:
                        end_of_the_interval = mid_point
                        y2 = y_mid
                    else:
                        start_of_the_interval = mid_point
                        y1 = y_mid

                    iteration += 1

                if iteration >= max_iterations:
                    print("Maximum iterations reached. Approximation may not be accurate.")
                else:
                    print(f"Root approximated at x = {(start_of_the_interval + end_of_the_interval) / 2}")

        elif choice == "4":
            break

        else:
            print("NOT VALID INPUT")


if __name__ == "__main__":
    main('test.txt')
