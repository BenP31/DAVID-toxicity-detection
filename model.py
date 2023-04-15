from detoxify import Detoxify
from datetime import datetime
import math
import sys

checkpoint_path = "models/original-albert-0e1d6498.ckpt"

class ToxicModel:
    def __init__(self) -> None:
        self.model = Detoxify('original-small', checkpoint=checkpoint_path)

    def predict(self, text:str) -> dict:
        return self.model.predict(text)
        

if __name__ == "__main__":
    model = ToxicModel()
    print(f"Model size: {sys.getsizeof(model.model.model)}")
    _times = []
    for i in range(50):
        _s = datetime.now()
        model.predict(text = "Test " * i)
        _f = datetime.now()
        _t = _f-_s
        _times.append(_t)
    _avg = sum([_x.microseconds for _x in _times])/len(_times)
    print(f"Takes \n\t{_avg} microseconds \n\t{_avg*(10**-6):2.5f} seconds (converted) \nper message on average")