from typing import List


def find_maximum_distance(
    number_of_cities: int, cities_with_train_station: List[int]
) -> int:
    validate_inputs(number_of_cities, cities_with_train_station)
    cities_with_train_station.sort()
    max_diff = cities_with_train_station[0]
    for i in range(1, len(cities_with_train_station)):
        diff = (cities_with_train_station[i] - cities_with_train_station[i - 1]) // 2
        if diff > max_diff:
            max_diff = diff
    last_city_distance = number_of_cities - cities_with_train_station[-1] - 1
    max_distance = max(last_city_distance, max_diff)
    return max_distance


class ValidationError(Exception):
    def __init__(self, message):
        super().__init__(message)


def validate_inputs(
        number_of_cities: int, cities_with_train_station: List[int]
):
    city_number_out_of_bounds = number_of_cities <= 0 or number_of_cities > 10000

    if city_number_out_of_bounds:
        raise ValidationError(message="The city input values are out of bounds.")
    elif len(cities_with_train_station) == 0:
        raise ValidationError(message="The city with train stations list cannot be empty.")
    elif len(cities_with_train_station) > number_of_cities:
        raise ValidationError(
            message="The number of cities with train stations cannot be longer than number of cities"
        )

    for index in cities_with_train_station:
        if index < 0 or index >= number_of_cities:
            raise ValidationError(message="Invalid city index.")
        elif cities_with_train_station.count(index) > 1:
            raise ValidationError(message="Each city can only have one train station.")


if __name__ == "__main__":
    # These are some of test cases. When evaluating the task, more will be added:
    assert find_maximum_distance(number_of_cities=3, cities_with_train_station=[1]) == 1
    assert find_maximum_distance(number_of_cities=4, cities_with_train_station=[3]) == 3
    assert (
        find_maximum_distance(number_of_cities=5, cities_with_train_station=[0, 4]) == 2
    )

    print("ALL TESTS PASSED")

