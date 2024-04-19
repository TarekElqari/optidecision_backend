import numpy as np


class TOPSIS:
    def __init__(self, criteria_names, criteria_weights, criteria_preferences):
        self.criteria_names = criteria_names
        self.criteria_weights = criteria_weights
        self.criteria_preferences = criteria_preferences

    def calculate_topsis_scores(self):
        num_alternatives = int(input("Enter the number of alternatives: "))
        alternatives_data = []

        for i in range(num_alternatives):
            alternative_name = input(f"Enter the name of alternative {i + 1}: ")
            alternative_values = []

            for criterion_name, preference in zip(self.criteria_names, self.criteria_preferences):
                value = float(input(f"Enter the value of {criterion_name} for {alternative_name}: "))
                # Adjust the value based on preference
                if preference == 'max':
                    alternative_values.append(value)
                elif preference == 'min':
                    alternative_values.append(1 / value)  # Invert for minimization
                else:
                    raise ValueError("Invalid preference. Please specify 'max' or 'min'.")

            alternatives_data.append({'name': alternative_name, 'values': alternative_values})

        alternative_values = np.array([alternative['values'] for alternative in alternatives_data])
        root_sum_squares = np.sqrt(np.sum(alternative_values ** 2, axis=0))
        normalized_data = alternative_values / root_sum_squares
        weighted_normalized_matrix = normalized_data * self.criteria_weights

        ideal_solution = np.max(weighted_normalized_matrix, axis=0)
        negative_ideal_solution = np.min(weighted_normalized_matrix, axis=0)
        distances_to_ideal = np.linalg.norm(weighted_normalized_matrix - ideal_solution, axis=1)
        distances_to_negative_ideal = np.linalg.norm(weighted_normalized_matrix - negative_ideal_solution, axis=1)
        topsis_scores = distances_to_negative_ideal / (distances_to_ideal + distances_to_negative_ideal)

        sorted_indices = np.argsort(topsis_scores)[::-1]
        sorted_alternatives = [alternatives_data[i] for i in sorted_indices]

        print("Alternatives sorted by TOPSIS scores:")
        for alternative, score in zip(sorted_alternatives, topsis_scores):
            print(f"{alternative['name']}: {score}")
        return topsis_scores
