# Data export module

class Point():
    def __init__(self, x = None, y = None):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"


class DataSerie():
    def __init__(self, X_label = "X", Y_label = "Y"):
        self.__points = []
        self.__X_label = X_label
        self.__Y_label = Y_label

    def __repr__(self):
        return f"[{','.join(map(str, self.__points))}]"

    def __iter__(self):
        for point in self.__points: yield point
    
    def __len__(self):
        return len(self.__points)
    
    def __getitem__(self, key):
        return self.__points[key] if key <= len(self) else None
    
    def append(self, point:Point) -> None:
        self.__points.append(point)

    def set_labels(self, X:str = None, Y:str = None) -> None:
        if X: self.__X_label = X
        if Y: self.__Y_label = Y

    def get_X_label(self) -> str:
        return self.__X_label

    def get_Y_label(self) -> str:
        return self.__Y_label


def export_csv(data, filename):
    """Save data as CSV"""

    pass

def export_xlsx(data, filename):
    """Save data as XLSX"""

    pass