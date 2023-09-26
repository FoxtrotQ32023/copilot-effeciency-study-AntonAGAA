from solution import find_airport_hubs  

def test_find_airport_hubs():
    content = """
        3
        3.2 -15.0
        20.1 -175
        -30.2 10
        3
        52.31 4.76
        51.96 4.44
        51.45 5.37
        """
    result = find_airport_hubs(content)
    assert result == [(3.2, -15.0), (52.31, 4.76)], f"Expected [(3.2, -15.0), (52.31, 4.76)] but got {result}"

def test_single_airport():
    content = """
        1
        40.71 -74.01
        """
    result = find_airport_hubs(content)
    assert result == [(40.71, -74.01)], f"Expected [(40.71, -74.01)] but got {result}"
