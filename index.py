from data_class import Data
import functools
import collections


class Main:
    """
    This is a class for the menu at the start of the app.
    """

    def __init__(self):
        self.data_list = []

    def initialise_data(self):
        """
        Method for initialising the data from the housing.cvs file, creating a list with each line of the file, starting
        with the second, as elements and then creating a list of Data objects.
        """
        lista = [line.rstrip('\n') for line in open('housing.csv')]
        lista = lista[1:]
        self.data_list = list(map(self.create_object, lista))
        self.data_list = list(filter(lambda element: element is not None, self.data_list))

    @staticmethod
    def create_object(item):
        new_list = item.split(",")
        if new_list[9] == "":
            return None
        try:
            line = Data(
                float(new_list[0]),
                float(new_list[1]),
                float(new_list[2]),
                float(new_list[3]),
                float(new_list[4]),
                float(new_list[5]),
                float(new_list[6]),
                float(new_list[7]),
                float(new_list[8]),
                new_list[9]
            )
            return line
        except ValueError:
            return None

    def main_controller(self):
        run = True
        while run:
            print("Please choose one:")
            print("1.Show the district with the biggest population")
            print("2.Show the district with the smallest population")
            print("3.The district with the biggest number of inhabitants per dorm + average value")
            print("4.The district with the smallest number of inhabitants per dorm")
            print("5.Average income and average age")
            print("6.Show the number of districts for each category of ocean_proximity")
            print("7.Raise the price of all the houses near the ocean by 10%")
            print("8.Report")
            print("9.Quit")
            self.initialise_data()
            try:
                choice = int(input("Please make a choice: "))
                if choice == 1:
                    self.biggest_district_by_population().pretty_print()
                elif choice == 2:
                    self.smallest_district_by_population().pretty_print()
                elif choice == 3:
                    self.district_with_max_number_inhabitants().pretty_print()
                    print("Average value: %f" % (self.average_value_inhabitants()))
                elif choice == 4:
                    self.district_with_min_number_inhabitants().pretty_print()
                elif choice == 5:
                    print("Average income: %f\nAverage age: %f" % (self.average_income(), self.average_age()))
                elif choice == 6:
                    print(self.number_of_districts_for_each_ocean_proximity())
                elif choice == 7:
                    [data_object.pretty_print() for data_object in self.increase_house_price()]
                elif choice == 8:
                    min_latitude = float(input("Please insert a minimum value for latitude:"))
                    max_latitude = float(input("Please insert a maximum value for latitude:"))

                    min_longitude = float(input("Please insert a minimum value for longitude:"))
                    max_longitude = float(input("Please insert a maximum value for longitude:"))

                    min_median_house_value = float(input("Please insert a minimum value for the price of the house:"))
                    max_median_house_value = float(input("Please insert a maximum value for the price of the house:"))
                    self.report(max_latitude, min_latitude, max_longitude, min_longitude, max_median_house_value,
                                min_median_house_value)
                elif choice == 9:
                    run = False
                elif choice > 9:
                    print("This option doesn't exist!")
            except ValueError:
                print("Oops!  That was not a valid input.  Try again...")

    def biggest_district_by_population(self):
        return functools.reduce(lambda accumulator, data_object: accumulator if
        accumulator.get_population() > data_object.get_population() else data_object, self.data_list)

    def smallest_district_by_population(self):
        return functools.reduce(lambda accumulator, data_object: accumulator if
        accumulator.get_population() < data_object.get_population() else data_object, self.data_list)

    def district_with_max_number_inhabitants(self):
        return functools.reduce(lambda accumulator, data_object: accumulator if
        accumulator.get_population() / accumulator.get_total_bedrooms() >
        data_object.get_population() / data_object.get_total_bedrooms()
        else data_object, self.data_list)

    def district_with_min_number_inhabitants(self):
        return functools.reduce(lambda accumulator, data_object: accumulator if
        accumulator.get_population() / accumulator.get_total_bedrooms() <
        data_object.get_population() / data_object.get_total_bedrooms()
        else data_object, self.data_list)

    def average_value_inhabitants(self):
        max_value = self.district_with_max_number_inhabitants().get_population() / self.district_with_max_number_inhabitants().get_total_bedrooms()
        min_value = self.district_with_min_number_inhabitants().get_population() / self.district_with_min_number_inhabitants().get_total_bedrooms()
        return (max_value + min_value) / 2

    def average_income(self):
        """sum_income = self.data_list[0].get_median_income()
        return functools.reduce(lambda accumulator, data_object: sum_income + data_object.get_median_income(),
        self.data_list)"""
        list_of_incomes = [data_object.get_median_income() for data_object in self.data_list]
        return (sum(list_of_incomes)) / len(self.data_list)

    def average_age(self):
        list_of_age = [data_object.get_housing_median_age() for data_object in self.data_list]
        return (sum(list_of_age)) / len(self.data_list)

    def number_of_districts_for_each_ocean_proximity(self):
        list_of_ocean_proximities = [data_object.get_ocean_proximity() for data_object in self.data_list]
        counter = collections.Counter(list_of_ocean_proximities)
        values = list(counter.values())
        keys = list(counter.keys())
        result = [str(keys[index]) + ": " + str(values[index]) for index in range(0, len(keys))]
        return result

    def increase_house_price(self):
        list_price_raise = [data_object for data_object in self.data_list if
                            data_object.get_ocean_proximity() == "NEAR OCEAN"]
        return list(map(self.increase_price, list_price_raise))

    @staticmethod
    def increase_price(item):
        new_price = item.get_median_house_value() * 1.1
        item.set_median_house_value(new_price)
        return item

    def report(self, max_latitude, min_latitude, max_longitude, min_longitude, max_median_house_value,
               min_median_house_value):
        data_string_list = [self.create_line(data_object) for data_object in self.data_list if
                            max_latitude > data_object.get_latitude() > min_latitude and
                            max_longitude > data_object.get_longitude() > min_longitude and
                            max_median_house_value > data_object.get_median_house_value() > min_median_house_value]
        with open('report.csv', 'w') as file:
            [file.write(data_line)for data_line in data_string_list]
        file.close()

    @staticmethod
    def create_line(data_object):
        data_line = "%f,%f,%f,%f,%f,%f,%f,%f,%f,%s\n" % (
            data_object.get_longitude(), data_object.get_latitude(), data_object.get_housing_median_age(),
            data_object.get_total_rooms(),
            data_object.get_total_bedrooms(), data_object.get_population(), data_object.get_households(),
            data_object.get_median_income(), data_object.get_median_house_value(),
            data_object.get_ocean_proximity())
        return data_line


Main().main_controller()
