
from helpers import load_map

def shortest_path(M,start,goal):
    print("shortest path called")


    return


def test_shortest_path():
    map_40 = load_map('map-40.pickle')
    assert shortest_path(map_40, 5, 34) == [5, 16, 37, 12, 34]



if __name__ == "__main__":
    test_shortest_path()