import os
import pickle
import numpy as np

from art import art
from pe import extract
from scanner import find_hash, search_vt, get_stats

os.system('clear')

print(art)

file = input('Enter file name with appropriate directory : ')
print()

hash = find_hash(file)
resp = search_vt(hash)

if(resp=="NoHistory"):
    print("This appears to be an undiscovered file\n")
    print("Proceeding to analyze the file locally\n")
    model = pickle.load(open('model','rb'))
    attributes = extract(file)
    prediction = model.predict(attributes)
    x = np.argmax(prediction.round(), axis=0)
    if(x==0):
        print("File appears to be legitimate")
    else:
        print("File appears to be malicious")
else:
    get_stats(resp)
