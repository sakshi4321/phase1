import pickle
with open("temp.dat","rb") as f:
    obj = pickle.load(f)
    print(obj)
