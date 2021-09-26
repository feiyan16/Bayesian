class JointDistributionTable:
    def __init__(self, filepath):
        self.attributes = []
        self.table = []
        self.class_data = []
        file = open(filepath, "r")
        att_str = file.readline()
        self.attributes = att_str.split("\t")
        lines = file.readlines()
        for i in range(len(lines)):
            line = lines[i]
            if line.isspace() or len(line) == 0:
                continue
            data_ln = line.split("\t")
            class_val = int(data_ln[len(data_ln) - 1])
            self.class_data.append(class_val)
            att_to_value = {}
            for n in range(0, len(data_ln) - 1):
                att = self.attributes[n]
                val = int(data_ln[n])
                att_to_value[att] = val
            self.table.append(att_to_value)
        file.close()

    def get_row(self, row):
        return self.table[row]

    def add_row(self, att_to_value):
        self.table.append(att_to_value)

    def put_in_row(self, row, attribute, value):
        att_to_value = self.table[row]
        att_to_value.update({attribute, value})

    def get_value_at(self, row, attribute):
        att_to_value = self.table[row]
        return att_to_value[attribute]

    def get_key_at(self, row, col):
        att_to_value = self.table[row]
        attributes = att_to_value.keys()
        return list(attributes)[col]

    def add_class_val(self, value):
        self.class_data.append(value)

    def get_class_val(self, row):
        return self.class_data[row]

    def row_size(self):
        return len(self.class_data)

    def col_size(self):
        return len(self.attributes) - 1
