import numpy as np

new = np.array([[2,5,6,7,7],[1,2,4,5,7]])
new2 = np.array([9,9,9,9,9])

print(new)
print(new2.any() == new.any())