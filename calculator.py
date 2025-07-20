import re


class Calc:
    def __init__(self, string):
        self.string = string
        self.result()

    def preprocess_percentage(self, percent):
        return re.sub(r"(\d+(\.\d+)?)%", r"(\1/100)", percent)

    def result(self):
        match = re.fullmatch(r"^[0-9+\-*/%.]+$", self.string)
        if match:
            try:
                mod_per = self.preprocess_percentage(self.string)
                total = eval(mod_per)
                return total
            except:
                return "Error"
        else:
            return "Error"


if __name__ == "__main__":
    Calc()
