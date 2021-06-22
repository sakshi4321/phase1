import pickle
with open("edc.dat","rb") as f:
    obj = pickle.load(f)
    print(obj)
