class TableMultiplication:

    def __init__(self, nb):
        self.nb = nb

    def prochain(self):
        for i in range(0, 10):
            nouvell_term_table = self.nb* i
            print(nouvell_term_table)

tab = TableMultiplication(3)
tab.prochain()
