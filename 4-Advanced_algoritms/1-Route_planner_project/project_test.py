from typing import Callable
import student_code
import helpers

MAP_40_ANSWERS: list[tuple[int, int, list[int]]] = [
    (5, 34, [5, 16, 37, 12, 34]),
    (5, 5, [5]),
    (8, 24, [8, 14, 16, 37, 12, 17, 10, 24]),
]


def test(shortest_path_function: Callable[[helpers.Map, int, int], list[int]]) -> None:
    """
    Test the shortest_path_function with predefined test cases.

    Args:
        shortest_path_function (Callable[[Map, int, int], list[int]]):
            A function that takes a Map object, a start node, and a goal node,
            and returns a list of nodes representing the shortest path.

    Returns:
        None
    """
    map_40 = helpers.load_map("map-40.pickle")
    correct = 0
    for start, goal, answer_path in MAP_40_ANSWERS:
        path = shortest_path_function(map_40, start, goal)
        if path == answer_path:
            correct += 1
        else:
            print(
                "For start:",
                start,
                "Goal:     ",
                goal,
                "Your path:",
                path,
                "Correct:  ",
                answer_path,
            )
    if correct == len(MAP_40_ANSWERS):
        print("All tests pass! Congratulations!")
    else:
        print("You passed", correct, "/", len(MAP_40_ANSWERS), "test cases")


# map_40 is a bigger map than map_10
map_40 = helpers.load_map('map-40.pickle')
helpers.show_map(map_40)
path = student_code.shortest_path(map_40, 5, 34)
if path == [5, 16, 37, 12, 34]:
    print("great! Your code works for these inputs!")
else:
    print("something is off, your code produced the following:")
    print(path)