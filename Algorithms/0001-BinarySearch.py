# Usa la fuerza bruta
# eficient econ listas ordenadas

# Escaneo Linear
def LinearScan(arr, target):
    i = 0
    while i < len(arr):
        if arr[i] == target:
            return i
        i += i
    return None