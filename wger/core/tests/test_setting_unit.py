# This file is part of wger Workout Manager.
#
# wger Workout Manager is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# wger Workout Manager is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Workout Manager.  If not, see <http://www.gnu.org/licenses/>.

from wger.core.models import SettingUnit
from wger.core.tests import api_base_test

from wger.manager.tests.testcase import WorkoutManagerAccessTestCase, WorkoutManagerTestCase
from wger.manager.tests.testcase import WorkoutManagerDeleteTestCase
from wger.manager.tests.testcase import WorkoutManagerEditTestCase
from wger.manager.tests.testcase import WorkoutManagerAddTestCase


class RepresentationTestCase(WorkoutManagerTestCase):
    '''
    Test the representation of a model
    '''

    def test_representation(self):
        '''
        Test that the representation of an object is correct
        '''
        self.assertEqual("{0}".format(SettingUnit.objects.get(pk=1)), 'Repetitions')


class OverviewTest(WorkoutManagerAccessTestCase):
    '''
    Tests the settings unit overview page
    '''

    url = 'core:setting_unit:list'
    anonymous_fail = True


class AddTestCase(WorkoutManagerAddTestCase):
    '''
    Tests adding a new unit
    '''

    object_class = SettingUnit
    url = 'core:setting_unit:add'
    data = {'name': 'Furlongs'}


class DeleteTestCase(WorkoutManagerDeleteTestCase):
    '''
    Tests deleting a unit
    '''

    object_class = SettingUnit
    url = 'core:setting_unit:delete'
    pk = 1


class EditTestCase(WorkoutManagerEditTestCase):
    '''
    Tests editing a unit
    '''

    pk = 1
    object_class = SettingUnit
    url = 'core:setting_unit:edit'
    data = {'name': 'Furlongs'}


class ApiTestCase(api_base_test.ApiBaseResourceTestCase):
    '''
    Tests the unit resource
    '''
    pk = 1
    resource = SettingUnit
    private_resource = False