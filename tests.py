import pytest
import task


def test_find_maximum_distance_1():
    assert task.find_maximum_distance(
        number_of_cities=9087, cities_with_train_station=[1, 2, 18, 67, 13, 501, 975, 25, 9000]
    ) == 4012


def test_find_maximum_distance_2():
    assert task.find_maximum_distance(
        number_of_cities=223, cities_with_train_station=[90, 17, 87, 175, 15, 1, 29]
    ) == 47


def test_find_maximum_distance_3():
    assert task.find_maximum_distance(
        number_of_cities=2300, cities_with_train_station=[20, 79, 150, 790, 524, 13, 1502, 2000]
    ) == 356


def test_find_maximum_distance_4():
    assert task.find_maximum_distance(
        number_of_cities=5, cities_with_train_station=[2, 3, 4]
    ) == 2


def test_find_maximum_distance_4():
    assert task.find_maximum_distance(
        number_of_cities=13, cities_with_train_station=[4, 11]
    ) == 4


def test_city_negative_number():
    with pytest.raises(task.ValidationError) as exc:
        task.find_maximum_distance(number_of_cities=-1, cities_with_train_station=[0, 4, 7])
    assert "The city input values are out of bounds." in str(exc.value)


def test_city_number_too_big():
    with pytest.raises(task.ValidationError) as exc:
        task.find_maximum_distance(number_of_cities=20900, cities_with_train_station=[7, 2, 8764])
    assert "The city input values are out of bounds." in str(exc.value)


def test_station_list_empty():
    with pytest.raises(task.ValidationError) as exc:
        task.find_maximum_distance(number_of_cities=1765, cities_with_train_station=[])
    assert "The city with train stations list cannot be empty." in str(exc.value)


def test_station_list_too_long():
    with pytest.raises(task.ValidationError) as exc:
        task.find_maximum_distance(number_of_cities=3, cities_with_train_station=[0, 1, 2, 3])
    assert "The number of cities with train stations cannot be longer than number of cities" in str(exc.value)


def test_negative_city_index():
    with pytest.raises(task.ValidationError) as exc:
        task.find_maximum_distance(number_of_cities=90, cities_with_train_station=[9, 78, -9])
    assert "Invalid city index." in str(exc.value)


def test_station_index_out_of_bounds():
    with pytest.raises(task.ValidationError) as exc:
        task.find_maximum_distance(number_of_cities=567, cities_with_train_station=[1, 47, 908])
    assert "Invalid city index." in str(exc.value)


def test_contains_duplicates():
    with pytest.raises(task.ValidationError) as exc:
        task.find_maximum_distance(number_of_cities=7509, cities_with_train_station=[5, 5, 87, 908])
    assert "Each city can only have one train station." in str(exc.value)


