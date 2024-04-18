import numpy as np

class AHP:
    def __init__(self):
        pass

    def pairwise_comparison(self, names):
        n = len(names)
        comparisons = np.zeros((n, n))

        for i in range(n):
            for j in range(i + 1, n):
                comparisons[i, j] = float(input(f"Enter the comparison value between {names[i]} and {names[j]}: "))
                comparisons[j, i] = 1 / comparisons[i, j]

        return comparisons

    def calculate_priority_weights(self, comparisons):
        normalized_matrix = comparisons / comparisons.sum(axis=0)
        priority_weights = normalized_matrix.mean(axis=1)
        return priority_weights

    def check_consistency(self, comparisons):
        row_sums = comparisons.sum(axis=1)
        n = len(row_sums)
        lambda_max = (row_sums / n).sum() / n
        random_index = {1: 0, 2: 0, 3: 0.58, 4: 0.9, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45, 10: 1.49}
        consistency_index = (lambda_max - n) / (n - 1)

        if n in random_index:
            consistency_ratio = consistency_index / random_index[n]
            return consistency_ratio
        else:
            return None

    def evaluate_hierarchy(self):
        num_criteria = int(input("Enter the number of criteria: "))
        criteria_data = []
        criteria_names = []
        for i in range(num_criteria):
            criterion_name = input(f"Enter the name of criterion {i + 1}: ")
            criteria_names.append(criterion_name)

        criteria_comparisons = self.pairwise_comparison(criteria_names)
        criteria_weights = self.calculate_priority_weights(criteria_comparisons)

        for i, criterion_name in enumerate(criteria_names):
            criterion_weight = criteria_weights[i]
            criteria_data.append({
                'name': criterion_name,
                'weight': criterion_weight,
                'subcriteria': []
            })
            num_subcriteria = int(input(f"Enter the number of subcriteria for criterion {criterion_name}: "))
            subcriteria_names = []

            for j in range(num_subcriteria):
                subcriterion_name = input(
                    f"Enter the name of subcriterion {j + 1} for criterion {criterion_name}: ")
                subcriteria_names.append(subcriterion_name)

            subcriteria_comparisons = self.pairwise_comparison(subcriteria_names)
            if num_subcriteria == 2:  # Adjust weights directly for only two subcriteria
                total_comparison = subcriteria_comparisons[0, 1] + subcriteria_comparisons[1, 0]
                subcriteria_weights = [subcriteria_comparisons[0, 1] / total_comparison,
                                       subcriteria_comparisons[1, 0] / total_comparison]
            else:
                subcriteria_weights = self.calculate_priority_weights(subcriteria_comparisons / subcriteria_comparisons.sum(axis=1))

            for j, subcriterion_name in enumerate(subcriteria_names):
                subcriterion_weight = subcriteria_weights[j]
                criteria_data[i]['subcriteria'].append({
                    'name': subcriterion_name,
                    'weight': subcriterion_weight
                })
        total_weights = sum(criterion['weight'] for criterion in criteria_data)
        for criterion in criteria_data:
            criterion['global_weight'] = criterion['weight'] / total_weights
        print("Hierarchy evaluation results:")
        for criterion in sorted(criteria_data, key=lambda x: x['global_weight'], reverse=True):
            print(f"Criterion: {criterion['name']}")
            print(f"Global Weight: {criterion['global_weight']}")
            print("Subcriteria:")
            for subcriterion in criterion['subcriteria']:
                print(f"  - {subcriterion['name']}: {subcriterion['weight']}")
            print()


ahp = AHP()
ahp.evaluate_hierarchy()
