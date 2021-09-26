from JointDistributionTable import JointDistributionTable


class NaiveBayes:
    def __init__(self, filepath):
        self.u = 0
        self.n0 = 0
        self.n1 = 0
        self.p_0 = 0
        self.p_1 = 0
        self.p_a0_0 = {}
        self.p_a1_0 = {}
        self.p_a0_1 = {}
        self.p_a1_1 = {}
        self.table = JointDistributionTable(filepath)
        self.get_sizes()
        self.get_probabilities()
        self.print_probabilities()

    def get_sizes(self):
        self.u = self.table.row_size()
        sorted_arr = self.table.class_data.copy()
        sorted_arr.sort()
        for i in range(0, self.u - 1):
            if sorted_arr[i] != sorted_arr[i + 1]:
                self.n0 = i + 1
                self.n1 = self.u - self.n0

    def get_probabilities(self):
        self.p_0 = self.n0 / self.u
        self.p_1 = self.n1 / self.u
        zeroes = []
        ones = []
        for i in range(self.table.row_size()):
            c = self.table.get_class_val(i)
            if c == 0:
                zeroes.append(i)
            elif c == 1:
                ones.append(i)
        for i in range(self.table.col_size()):
            attribute = self.table.attributes[i]
            ct_1 = 0
            ct_0 = 0
            for z in zeroes:
                v = self.table.get_value_at(z, attribute)
                if v == 0:
                    ct_0 += 1
                elif v == 1:
                    ct_1 += 1
            self.p_a0_0[attribute] = ct_0 / self.n0
            self.p_a1_0[attribute] = ct_1 / self.n0
            ct_0 = 0
            ct_1 = 0
            for o in ones:
                v = self.table.get_value_at(o, attribute)
                if v == 0:
                    ct_0 += 1
                elif v == 1:
                    ct_1 += 1
            self.p_a0_1[attribute] = ct_0 / self.n1
            self.p_a1_1[attribute] = ct_1 / self.n1

    def print_probabilities(self):
        class_ = "P(class={value})={prob:.2f}"
        attribute_ = "P({att}={val}|{clss})={prob:.2f}"
        print(class_.format(value=0, prob=self.p_0), end=" ")
        for i in range(self.table.col_size()):
            attribute = self.table.attributes[i]
            print(attribute_.format(att=attribute, val=0, clss=0, prob=self.p_a0_0[attribute]), end=" ")
            print(attribute_.format(att=attribute, val=1, clss=0, prob=self.p_a1_0[attribute]), end=" ")
        print()
        print(class_.format(value=1, prob=self.p_1), end=" ")
        for i in range(self.table.col_size()):
            attribute = self.table.attributes[i]
            print(attribute_.format(att=attribute, val=0, clss=1, prob=self.p_a0_1[attribute]), end=" ")
            print(attribute_.format(att=attribute, val=1, clss=1, prob=self.p_a1_1[attribute]), end=" ")
        print("\n")
