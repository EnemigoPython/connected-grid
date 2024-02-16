import numpy as np

def random_binary_array(x: int, y: int):
    return np.random.randint(2, size=(x, y))

def grid_is_connected(arr: np.array):
    # initialise with all vals that are 1 in the first row
    connected_above = set(e for e, el in enumerate(arr[0]) if el == 1)
    for row in arr[1:]:
        new_connected = set()
        for e in connected_above:
            # check each val connected to 1s in prev row
            # that hasn't already been marked as connected
            if row[e] == 0 or e in new_connected:
                continue
            new_connected.add(e)
            # if there is a connection, check left and right
            for d in (-1, 1):
                curr = e + d
                while curr >= 0 and curr < len(row):
                    # in each direction stop when no direct path
                    # or val already marked as connected
                    if row[curr] == 0 or curr in new_connected:
                        break
                    new_connected.add(curr)
                    curr += d
        if not new_connected:
            return False
        connected_above = new_connected
    return True



def main():
    connected_arrs = {}
    for size in range(3, 10):
        connected_arrs[size] = []
        for _ in range(20):
            arr = random_binary_array(size, size)
            if grid_is_connected(arr):
                connected_arrs[size].append(arr)

    for k, v in connected_arrs.items():
        print(f"\nConnected arrays of size {k}:")
        for i in v:
            print(f"\n{i}")



if __name__ == '__main__':
    main()
