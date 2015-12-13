import time

from django.contrib.auth import get_user_model
from django.test.client import RequestFactory
from django.db import connection

from mezzanine.utils.tests import TestCase

from logbook import Logger

log = Logger('Inmate tests')

User = get_user_model()

import numpy as np
import datetime

from inmates.models import (
    PrisonFacility,
    CellBlock,
    PrisonCell,
    Gang,
    Inmate,
)

DEBUG = True
INITIAL_BUILD = True

BLOCKS_PER_PRISON = 10
CELLS_PER_BLOCK = 50

PRISONS = [
    ("San Diego Central Jail", "(619) 610-1647"),
    ("Las Colinas Detention & Reentry Facility", "(619) 402-1312"),
    ("Vista Detention Facility", "(760) 936-0014"),
    ("George Bailey Detention Facility", "(619) 210-0385"),
    ("South Bay Detention Facility", "(619) 213-1433"),
    ("East Mesa Reentry Facility", "(619) 210-0334"),
    ("Facility 8 Detention Facility", "(619) 210-0327")
]

MAX_SECONDS_PER_INSERTION = 0.1

first_names = ["John_" + str(i) for i in xrange(50)]
last_names = ["Doe_" + str(i) for i in xrange(50)]
GANGS = [None] + ["Gang_" + str(i) for i in xrange(50)]




class InmateTest(TestCase):
    def setUp(self):
        """
        Creates an admin user, sets up the debug cursor, so that we can
        track the number of queries used in various places, and creates
        a request factory for views testing.
        """
        self._username = "test"
        self._password = "test"
        self._emailaddress = "example@example.com"
        args = (self._username, self._emailaddress, self._password)
        self._user = User.objects.create_superuser(*args)
        self._request_factory = RequestFactory()
        self._debug_cursor = connection.force_debug_cursor
        connection.force_debug_cursor = True
        self._build_prison_components()

    def tearDown(self):
        """
        Clean up the admin user created and debug cursor.
        """
        self._user.delete()
        connection.force_debug_cursor = self._debug_cursor

    def _build_prison_components(self):
        t0 = time.time()
        facilities = [PrisonFacility.objects.create(name=name, phone_number=phone_number)
                      for name, phone_number in PRISONS]
        for facility in facilities:
            facility.save()
        cell_blocks = [CellBlock.objects.create(facility=facility, block_number=block_number)
                       for block_number in xrange(BLOCKS_PER_PRISON)
                       for facility in facilities]
        for block in cell_blocks:
            block.save()
        cells = [PrisonCell(cell_block=cell_block, cell_number=cell_number)
                 for cell_number in xrange(CELLS_PER_BLOCK)
                 for cell_block in cell_blocks]
        for cell in cells:
            cell.save()
        gangs = [Gang(name=name) for name in GANGS]
        for gang in gangs:
            gang.save()
        self._elapsed_time = round(time.time() - t0, 5)
        self._txn_count = len(facilities) + len(cell_blocks) * (1 + CELLS_PER_BLOCK) + len(GANGS)
        self._prison_cells = cells
        self._gangs = gangs

    def test_build_time(self):
        print "\nPrison model build time:\n  {} seconds/insertion\n  {} insertions".format(
            self._elapsed_time / self._txn_count, self._txn_count)
        self.assertLess(self._elapsed_time / self._txn_count, MAX_SECONDS_PER_INSERTION,
                        "Insertions take too long")

    def test_inmate_insertions(self):
        cells = self._prison_cells
        gangs = self._gangs
        t0 = time.time()
        for cell in cells:
            Inmate.objects.create(
                first_name=np.random.choice(first_names),
                last_name=np.random.choice(last_names),
                social_secutity_number=social(),
                release_date=datetime.datetime.now() + datetime.timedelta(days=np.random.randint(1, 10000)),
                birth_date=random_bday(),
                gang=np.random.choice(gangs),
                prison_cell=cell
            )
        elapsed_time = round(time.time() - t0, 5)
        print "\nInmate creation time:\n  {} seconds/insertion\n  {} insertions".format(
            elapsed_time / len(cells), len(cells))
        self.assertLess(elapsed_time / len(cells), MAX_SECONDS_PER_INSERTION, "Insertions take too long")

    def test_this_meant_to_fail(self):
        raise ExampleException("This is what happens when a test fails")

    def test_some_other_test(self):
        pass


def random_bday(min_age=18, max_age=60):
    low = min_age * 365
    high = max_age * 365
    age = np.random.randint(low, high)
    today = datetime.datetime.today().date()
    return today - datetime.timedelta(days=age)


def social():
    return np.random.randint(100000000, 999999999)


class ExampleException(Exception):
    pass
