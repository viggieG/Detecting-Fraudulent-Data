import utils  # noqa: F401, do not remove if using a Mac
# add your imports BELOW this line
import csv
import matplotlib.pyplot as plt
import random


def extract_election_vote_counts(filename, column_names):
    """Extract given columns' values in a given file.

    Arguments:
        filename: a given data file name containing given columns
        column_names: a list of given columns' names

    Returns: a list of integers that contains the values in those
             columns from every row without specific order

    Example:
        Code:
            extract_election_vote_counts("election-iran-2009.csv",
                        ["Ahmadinejad", "Rezai", "Karrubi", "Mousavi"])
        Output:
            [1131111, 16920, 7246, 837858, 623946, 12199, ...]
    """
    values = []
    input = open(filename)
    file = csv.DictReader(input)
    for row in file:
        for name in column_names:
            row[name] = row[name].replace(',', "")
            if row[name] != '':
                values.append(int(row[name]))
    input.close()
    return values


def ones_and_tens_digit_histogram(numbers):
    """Find the frequency of numbers from 0 to 9 appeared
        in the ones place or the tens place in the input list.

    Arguments:
        numbers: a list of numbers

    Returns: a list with 10 numbers in which the value at index i is
             the frequency with which digit i appeared in the ones
             place or the tens place in the input list.

    Example:
        Code:
            ones_and_tens_digit_histogram([127, 426, 28, 9, 90])
        Output:
            [0.2, 0.0, 0.3, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.2]
    """
    fre = [0] * 10
    for num in numbers:
        if num < 10:
            fre[0] += 1
            fre[num] += 1
        else:
            num = num % 100
            fre[num % 10] += 1
            fre[num // 10] += 1
    sums = sum(fre)
    for i in range(10):
        fre[i] = float(fre[i] / sums)
    return fre


def plot_iran_least_digits_histogram(histogram):
    """Graphs the frequencies of the ones and tens digits
       for the Iranian election data.

    Arguments:
        histogram: a list of numbers that represent each
                   digit's frequency appeared in the ones
                   and tens digits in Iranian election data

    Returns: Nothing

    Example:
        Code:
            plot_iran_least_digits_histogram(histogram)
            (histogram generated by the 2009 Iranian election data)
        Output:
            nothing
    """
    ideal = [0.1] * 10
    plt.plot(range(10), histogram, label="iran")
    plt.plot(range(10), ideal, label="ideal")
    plt.xlabel("Digit")
    plt.ylabel("Frequency")
    plt.title("Distribution of the last two digits in \
              Iranian dataset")
    plt.legend(loc='upper left')
    plt.savefig("iran-digits.png")
    # plt.show()
    plt.clf()


def random_numbers_produced(size):
    """Generate different number of random numbers between
       0 and 99 according to the input size

    Arguments:
        size: a number representing the wanted size of randoms

    Returns: a list of random numbers with input size

    Example:
        Code:
            random_numbers_produced(2)
        Output:
            [5, 81]
    """
    randoms = []
    for i in range(size):
        randoms.append(random.randint(0, 99))
    return randoms


def plot_distribution_by_sample_size():
    """Graphs the digit frequency for five different random datasets
       (one of size 10, another of size 50, then 100, 1000,
        and 10,000) of random numbers where every element in
        the collection is a different random number x such
        that 0 <= x < 100)

    Arguments:
        Nothing

    Returns: Nothing

    Example:
        Code:
            plot_distribution_by_sample_size()
        Output:
            nothing
    """
    ideal = [0.1] * 10
    num = [10, 50, 100, 1000, 10000]
    list = [[]] * 5
    for i in range(5):
        list[i] = random_numbers_produced(num[i])
        list[i] = ones_and_tens_digit_histogram(list[i])
    plt.plot(range(10), ideal, label="ideal")
    plt.plot(range(10), list[0], label="10 random numbers")
    plt.plot(range(10), list[1], label="50 random numbers")
    plt.plot(range(10), list[2], label="100 random numbers")
    plt.plot(range(10), list[3], label="1000 random numbers")
    plt.plot(range(10), list[4], label="10000 random numbers")
    plt.xlabel("Digit")
    plt.ylabel("Frequency")
    plt.title("Distribution of last two digits in randomly generated samples")
    plt.legend(loc='upper left')
    plt.savefig("random-digits.png")
    # 0plt.show()
    plt.clf()


def mean_squared_error(numbers1, numbers2):
    """Calculate the mean squared error between the input
       lists numbers1 and numbers2

    Arguments:
        numbers1: a list of numbers
        numbers2: a list of numbers

    Returns: a number represents the mean squared error
             between the lists number1 and number2.

    Example:
        Code:
            mean_squared_error([1, 4, 9], [6, 5, 4])
        Output:
            17.0
    """
    sum = 0
    for i in range(len(numbers1)):
        sum += (numbers1[i] - numbers2[i]) ** 2
    return float(sum / len(numbers1))


def calculate_mse_with_uniform(histogram):
    """Calculate the mean squared error between the input
       list histogram and the uniform distribution

    Arguments:
        histogram: a list of numbers that represent each
                   digit's frequency appeared in the ones
                   and tens digits in data set

    Returns: a number represents the mean squared error
             between the input list histogram and uniform
             distribution

    Example:
        Code:
            calculate_mse_with_uniform(histogram)
            (histogram generated by the 2009 Iranian election data)
        output:
            0.000739583333333
    """
    ideal = [0.1] * 10
    return mean_squared_error(histogram, ideal)


def compare_simulation(mse, number_of_datapoints):
    """Calculate the mean squared error between the 10000 random
       numbers and the uniform distribution. Then compare the
       random mean squared error to the input mse and count the
       quantity of random mean squared errors that are larger or
       equal to the input mse and also quantity of those smaller ones

    Arguments:
        mse: a mean squared error number used to compare
        number_of_datapoints: a number used to decide the
                              size of random numbers

    Returns: a list containing the quantities of larger or equal and
             those smaller ones

    Example:
        Code:
            compare_simulation(0.007, 120)
        output:
            [455, 9545]
    """
    larger = 0
    smaller = 0
    list = []
    for i in range(10000):
        ram = random_numbers_produced(number_of_datapoints)
        hist = ones_and_tens_digit_histogram(ram)
        ram_mse = calculate_mse_with_uniform(hist)
        if ram_mse >= mse:
            larger += 1
        elif ram_mse < mse:
            smaller += 1
    list.append(larger)
    list.append(smaller)
    return list


def compare_iran_mse_to_samples(iran_mse, number_of_iran_datapoints):
    """Get the quantity of random mean squared errors that are larger or
       equal to the input iran_mse and also quantity of those smaller ones.
       Then print out the iran_mse, those quantities and p-value for
       iran_mse.

    Arguments:
        iran_mse: a mean squared error number between 2009 Iranian
                  election data and the uniform distribution
        number_of_iran_datapoints: a number of data points in
                                   Iranian election data

    Returns: nothing

    Example:
        Code:
            compare_iran_mse_to_samples(0.000739583333333, 120)
        Output:
            2009 Iranian election MSE: 0.0007395833333333335
            Quantity of MSEs larger than or equal to the 2009 \
                Iranianelection MSE: 387
            Quantity of MSEs smaller than the 2009 Iranian \
                electionMSE: 9613
            2009 Iranian election null hypothesis rejection level p: 0.0387
    """
    result = compare_simulation(iran_mse, number_of_iran_datapoints)
    print("2009 Iranian election MSE: " + str(iran_mse))
    print("Quantity of MSEs larger than or equal to the 2009 Iranian"
          " election MSE: " + str(result[0]))
    print("Quantity of MSEs smaller than the 2009 Iranian election"
          " MSE: " + str(result[1]))
    print("2009 Iranian election null hypothesis rejection level p: "
          + str(float(result[0] / 10000)))


def compare_us_mse_to_samples(us_mse, number_of_us_datapoints):
    """Get the quantity of random mean squared errors that are larger or
       equal to the input us_mse and also quantity of those smaller ones.
       Then print out the us_mse, those quantities and p-value for
       us_mse.

    Arguments:
        us_mse: a mean squared error number between 2008 US
                  election data and the uniform distribution
        number_of_us_datapoints: a number of data points in
                                   US election data

    Returns: nothing

    Example:
        Code:
            compare_us_mse_to_samples(0.0001410025876058068, 302)
        Output:
            2008 United States election MSE: 0.0001410025876058068
            Quantity of MSEs larger than or equal to the 2008 United \
                Stateselection MSE: 4766
            Quantity of MSEs smaller than the 2008 United States \
                electionMSE: 5234
            2008 United States election null hypothesis rejection \
                level p: 0.4766
    """
    result = compare_simulation(us_mse, number_of_us_datapoints)
    print("2008 United States election MSE: " + str(us_mse))
    print("Quantity of MSEs larger than or equal to the 2008 United States"
          " election MSE: " + str(result[0]))
    print("Quantity of MSEs smaller than the 2008 United States election"
          " MSE: " + str(result[1]))
    print("2008 United States election null hypothesis rejection level p: "
          + str(float(result[0] / 10000)))


# The code in this function is executed when this
# file is run as a Python program
def main():
    # Code that calls functions you have written above
    # e.g. extract_election_vote_counts() etc.
    # This code should produce the output expected from your program.
    numbers = extract_election_vote_counts("election-iran-2009.csv",
                                           ["Ahmadinejad", "Rezai",
                                            "Karrubi", "Mousavi"])
    histogram = ones_and_tens_digit_histogram(numbers)
    plot_iran_least_digits_histogram(histogram)
    plot_distribution_by_sample_size()
    iran_mse = calculate_mse_with_uniform(histogram)
    compare_iran_mse_to_samples(iran_mse, len(numbers))
    print()
    numbers2 = extract_election_vote_counts("election-us-2008.csv",
                                            ["Obama", "McCain",
                                             "Nader", "Barr",
                                             "Baldwin", "McKinney"])
    histogram2 = ones_and_tens_digit_histogram(numbers2)
    us_mse = calculate_mse_with_uniform(histogram2)
    compare_us_mse_to_samples(us_mse, len(numbers2))


if __name__ == "__main__":
    main()
