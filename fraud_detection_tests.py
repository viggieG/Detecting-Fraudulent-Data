import fraud_detection as fd
import math
import csv


def test_ones_and_tens_digit_histogram():
    # example from spec
    actual = fd.ones_and_tens_digit_histogram([127, 426, 28, 9, 90])
    expected = [0.2, 0.0, 0.3, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.2]
    for i in range(len(actual)):
        assert math.isclose(actual[i], expected[i])
    # example from spec
    real = fd.ones_and_tens_digit_histogram([0, 1, 1, 2, 3, 5, 8,
                                            13, 21, 34, 55, 89,
                                            144, 233, 377, 610,
                                            987, 1597, 2584,
                                            181, 6765])
    expect = [0.21428571428571427, 0.14285714285714285, 0.047619047619047616,
              0.11904761904761904, 0.09523809523809523, 0.09523809523809523,
              0.023809523809523808, 0.09523809523809523, 0.11904761904761904,
              0.047619047619047616]
    for i in range(len(real)):
        assert math.isclose(real[i], expect[i])


def test_extract_election_vote_counts():
    # example from spec
    input = open("election-iran-2009.csv")
    file = csv.DictReader(input)
    expect = []
    for col in file:
        col["Ahmadinejad"] = col["Ahmadinejad"].replace('"', "")
        col["Ahmadinejad"] = col["Ahmadinejad"].replace(',', "")
        # specific expected values
        expect.append(int(col["Ahmadinejad"]))
    input.close()
    list = ["Ahmadinejad"]
    assert fd.extract_election_vote_counts("election-iran-2009.csv", list) \
           == expect


def test_mean_squared_error():
    # example from spec
    assert fd.mean_squared_error([1, 4, 9], [6, 5, 4]) == 17.0


def main():
    test_ones_and_tens_digit_histogram()
    test_extract_election_vote_counts()
    test_mean_squared_error()


if __name__ == "__main__":
    main()
