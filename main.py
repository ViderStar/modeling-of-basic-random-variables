from labwork1 import LabWork1
from labwork2 import LabWork2
from labwork3 import LabWork3
from labwork4 import LabWork4
from labwork5 import LabWork5

if __name__ == "__main__":
    print(f"Please, input numer of labwork:")
    lab_num = input()
    if lab_num == "1":
        LabWork1()
    elif lab_num == "2":
        LabWork2()
    elif lab_num == "3":
        LabWork3()
    elif lab_num == "4":
        LabWork4()
    elif lab_num == "5":
        LabWork5()
