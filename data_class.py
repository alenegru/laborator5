class Data:
    """
    This is a class for the data from the housing.csv file, that contains the constructor which initialises
    attributes of the data and get set methods for each attribute.
    """

    def __init__(self, longitude, latitude, housing_median_age, total_rooms, total_bedrooms, population, households,
                 median_income, median_house_value, ocean_proximity):
        """
        The constructor of the class Data
        :param longitude:
        :param latitude:
        :param housing_median_age:
        :param total_rooms:
        :param total_bedrooms:
        :param population:
        :param households:
        :param median_income:
        :param median_house_value:
        :param ocean_proximity:
        """
        self.longitude = longitude
        self.latitude = latitude
        self.housing_median_age = housing_median_age
        self.total_rooms = total_rooms
        self.total_bedrooms = total_bedrooms
        self.population = population
        self.households = households
        self.median_income = median_income
        self.median_house_value = median_house_value
        self.ocean_proximity = ocean_proximity

    def get_longitude(self):
        return self.longitude

    def set_longitude(self, longitude):
        self.longitude = longitude

    def get_latitude(self):
        return self.latitude

    def set_latitude(self, latitude):
        self.latitude = latitude

    def get_housing_median_age(self):
        return self.housing_median_age

    def set_housing_median_age(self, housing_median_age):
        self.housing_median_age = housing_median_age

    def get_total_rooms(self):
        return self.total_rooms

    def set_total_rooms(self, total_rooms):
        self.total_rooms = total_rooms

    def get_total_bedrooms(self):
        return self.total_bedrooms

    def set_total_bedrooms(self, total_bedrooms):
        self.total_bedrooms = total_bedrooms

    def get_population(self):
        return self.population

    def set_population(self, population):
        return self.population

    def get_households(self):
        return self.households

    def set_households(self, households):
        self.households = households

    def get_median_income(self):
        return self.median_income

    def set_median_income(self, median_income):
        self.median_income = median_income

    def get_median_house_value(self):
        return self.median_house_value

    def set_median_house_value(self, median_house_value):
        self.median_house_value = median_house_value

    def get_ocean_proximity(self):
        return self.ocean_proximity

    def set_ocean_proximity(self, ocean_proximity):
        self.ocean_proximity = ocean_proximity

    def pretty_print(self):
        try:
            print(
                "%f %f %f %f %f %f %f %f %f %s" % (
                    self.longitude, self.latitude, self.housing_median_age, self.total_rooms,
                    self.total_bedrooms, self.population, self.households,
                    self.median_income, self.median_house_value, self.ocean_proximity))
        except AttributeError:
            print("This line doesn't exist")
