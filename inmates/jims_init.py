

# from jail_system.local_settings import PRISONS, BLOCKS_PER_PRISON, CELLS_PER_BLOCK


from inmates.models import (
    PrisonFacility,
    CellBlock,
    PrisonCell
)

DEBUG = True
INITIAL_BUILD = True


BLOCKS_PER_PRISON= 10
CELLS_PER_BLOCK = 100

PRISONS = [
    ("San Diego Central Jail", "(619) 610-1647"),
    ("Las Colinas Detention & Reentry Facility", "(619) 402-1312"),
    ("Vista Detention Facility", "(760) 936-0014"),
    ("George Bailey Detention Facility", "(619) 210-0385"),
    ("South Bay Detention Facility", "(619) 213-1433"),
    ("East Mesa Reentry Facility", "(619) 210-0334"),
    ("Facility 8 Detention Facility", "(619) 210-0327")
]
#
# if INITIAL_BUILD:
#     init_jims(PRISONS, BLOCKS_PER_PRISON, CELLS_PER_BLOCK)
#

first_names = ['Jean', 'Erica', 'Clayton', 'Grace', 'Iris', 'Barry', 'Ebony', 'Laurie', 'Aubrey', 'Sylvester',
               'Miriam', 'Tim', 'Stewart', 'Levi', 'Leon', 'Dexter', 'Eva', 'Lola', 'Shannon', 'Benjamin',
               'Hugh', 'Rita', 'Olivia', 'Laura', 'Bernice', 'Annette', 'Lamar', 'Dominick', 'Katherine',
               'David', 'Marie', 'Clara', 'Erik', 'Fred', 'Walter', 'Emanuel', 'Marilyn', 'Estelle', 'Thomas',
               'Alonzo', 'Arlene', 'Ernestine', 'Lela', 'Juan', 'Elmer', 'Bryant', 'Anita', 'Chad', 'Sophia',
               'Terence', 'Oliver', 'Jeanne', 'Ken', 'Reginald', 'Devin', 'Teresa', 'Guadalupe', 'Tiffany',
               'Vanessa', 'Beverly', 'Nina', 'Margarita', 'Brent', 'Dennis', 'Abel', 'Stacey', 'Caroline',
               'Wanda', 'Nicholas', 'Annie', 'Kerry', 'Rachael', 'Alison', 'Lindsey', 'Jerome', 'Earl', 'Whitney',
               'Emma', 'Aaron', 'Roger', 'Deborah', 'Meredith', 'Jamie', 'Ernest', 'Gwendolyn', 'Sonya', 'Calvin',
               'Marguerite', 'Rochelle', 'Katrina', 'Jaime', 'Dawn', 'Pam', 'Paula', 'Elsie', 'Max', 'Loretta',
               'Nora', 'Tonya', 'Natalie']

last_names = [['Austin', 'Mckinney', 'Maldonado', 'Ramirez', 'Hines', 'Becker', 'Duncan', 'Riley', 'Garza', 'Cortez',
               'Allison', 'Stevens', 'Howard', 'Douglas', 'Curtis', 'Daniels', 'Hammond', 'Turner', 'Harper', 'Lee',
               'Robertson', 'Hughes', 'Patterson', 'Cook', 'Bell', 'Bryant', 'Long', 'Alexander', 'Thomas', 'Bowers',
               'Edwards', 'Alvarado', 'Stephens', 'Boone', 'Webster', 'White', 'Dawson', 'Goodman', 'Bowen', 'Malone',
               'Ortiz', 'Carlson', 'Garrett', 'Cunningham', 'Dean', 'Hayes', 'Hogan', 'Frazier', 'Baker', 'Potter',
               'Flores', 'Figueroa', 'Mccoy', 'Bates', 'Mills', 'Patrick', 'Woods', 'Higgins', 'Adams', 'Walters',
               'Casey', 'Reid', 'Castro', 'Hicks', 'Quinn', 'Watts', 'Beck', 'Oliver', 'Gonzalez', 'Evans', 'Hale',
               'Saunders', 'Mccarthy', 'Russell', 'Walsh', 'Holloway', 'Carpenter', 'Little', 'Johnston', 'Pratt',
               'Conner', 'Fernandez', 'Lambert', 'Sims', 'Patton', 'Rios', 'Hardy', 'Warren', 'Rowe', 'Shelton',
               'Mitchell', 'Thornton', 'Harrington', 'Underwood', 'George', 'Elliott', 'Farmer', 'Cole', 'Mcguire', 'Medina']]


def init_jims(prison_tuples, blocks_per_prison, cells_per_block):
    facilities = [PrisonFacility(name=name, phone_number=phone_number)
                  for name, phone_number in prison_tuples]
    for obj in facilities:
        obj.save()
    cell_blocks = [CellBlock(facility=facility, block_number=block_number)
                   for block_number in xrange(blocks_per_prison)
                   for facility in facilities]
    for obj in cell_blocks:
        obj.save()
    cells = [PrisonCell(cell_block=cell_block, cell_number=cell_number)
             for cell_number in xrange(cells_per_block)
             for cell_block in cell_blocks]
    for cell in cells:
        cell.save()


def random_names(n):pass



