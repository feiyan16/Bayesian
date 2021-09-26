from JointDistributionTable import JointDistributionTable


class Test:
    def __init__(self, name, filepath, bayes):
        self.name = name
        self.bayes = bayes
        self.table = JointDistributionTable(filepath)
        self.bayes_classification = []

    def run_test(self):
        for row in range(self.table.row_size()):
            p_a_0 = 1
            p_a_1 = 1
            for col in range(self.table.col_size()):
                attribute = self.table.get_key_at(row, col)
                value = self.table.get_value_at(row, attribute)
                if value == 0:
                    p_a_0 *= self.bayes.p_a0_0[attribute]
                    p_a_1 *= self.bayes.p_a0_1[attribute]
                elif value == 1:
                    p_a_0 *= self.bayes.p_a1_0[attribute]
                    p_a_1 *= self.bayes.p_a1_1[attribute]
            p_0_a = p_a_0 * self.bayes.p_0
            p_1_a = p_a_1 * self.bayes.p_1
            if p_0_a >= p_1_a:
                self.bayes_classification.append(0)
            else:
                self.bayes_classification.append(1)
        print("Accuracy on {} set ({} instances): {:.2f}%".format(self.name, self.table.row_size(),
                                                                 self.calculate_accuracy()))

    def calculate_accuracy(self):
        similar = 0
        for i in range(self.table.row_size()):
            if self.bayes_classification[i] == self.table.get_class_val(i):
                similar += 1
        return similar / self.table.row_size() * 100
