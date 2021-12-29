import os
import random
import pandas as pd

adjectives = pd.read_csv(os.path.join(os.path.dirname(__file__), 'words/adjectives.txt'), sep='\n', header=None, names=['adjectives'], squeeze=True)
animals    = pd.read_csv(os.path.join(os.path.dirname(__file__), 'words/animals.txt'),    sep='\n', header=None, names=['animals'],    squeeze=True)

print((random.choice(adjectives) + random.choice(animals)).lower().replace('-', '').strip())
