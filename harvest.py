############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []
        self.name = name 
        self.code = code 
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType(
    "musk",
    "Muskmelon",
    1998,
    "green",
    True,
    True)
    musk.add_pairing("mint")

    cas = MelonType(
    "cas",
    "Casaba",
    2003,
    "orange",
    False,
    False)
    cas.add_pairing("mint")
    cas.add_pairing("strawberries")

    cren = MelonType(
    "cren",
    "Crenshaw",
    1996,
    "green",
    True,
    False)
    cren.add_pairing("prosciutto")

    yw = MelonType(
    "yw",
    "Yellow Watermelon",
    2013,
    "yellow",
    True,
    True)
    yw.add_pairing("ice cream")

    all_melon_types = [musk, cas, cren, yw]

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types: 
        print(melon.pairing)

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    melon_dict = {}
    for melon in melon_types: 
        melon_dict[melon.code] = melon
  
    return melon_dict

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""
    def __init__(self, melon_type, shape_rating, color_rating, harvested_from_field, harvester):
        """Initialize a melon."""

        self.melon_type = melon_type 
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvested_from_field = harvested_from_field
        self.harvester = harvest

    def is_sellable(self):
        if self.shape_rating >5 and self.color_rating > 5 and self.field != 3:
            return True
        else: 
            return False 


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melons_by_id = make_melon_type_lookup(melon_types)
    melons = [] 

    melon_1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    melon_2 = Melon(melons_by_id["yw"], 3, 4, 2, 'Shelia')
    melon_3 = Melon(melons_by_id["yw"], 9, 8, 3, 'Shelia')
    melon_4 = Melon(melons_by_id["cas"], 10, 6, 35, 'Shelia')
    melon_5 = Melon(melons_by_id["cren"], 8, 9, 35, 'Michael')
    melon_6 = Melon(melons_by_id["cren"], 8, 2, 35, 'Michael')
    melon_7 = Melon(melons_by_id["cren"], 2, 3, 4, 'Michael')
    melon_8 = Melon(melons_by_id["musk"], 6, 7, 4, 'Michael')
    melon_9 = Melon(melons_by_id["yw"], 7, 10, 3, 'Sheila')

    melons = [melon_1, melon_2, melon_3, melon_4, melon_5, melon_6, melon_7, melon_8, melon_9]

    return melons 


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons: 
        if melon.is_sellable():
           print((f'Harvest by {melon.harvester} from {melon.harvested_from_field} (CAN BE SOLD'))
        else: 
            print((f'Harvest by {melon.harvester} from {melon.harvested_from_field} (NOT SELLABLE'))

get_sellability_report(melons)

