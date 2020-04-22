#!/usr/bin/env python3

"""
Script:	example.py
Date:	2020-04-20

Platform: macOS

Description:
Demonstration of plist_class
"""
__author__ = "thedzy"
__copyright__ = "Copyright 2020, thedzy"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "thedzy"
__email__ = "thedzy@hotmail.com"
__status__ = "Developer"

import plist_preferences
import logging


def main():

    logging.basicConfig(format='[%(asctime)s] [%(levelname)-7s] %(message)s', level=logging.INFO)

    # Create a settings object, a derived class of dict
    settings = plist_preferences.Settings('com.github.thedzy.example')

    print('\nStarting settings:')
    print(settings.get())

    # Set the the entire data set
    print('\nAfter replacing entire preferences:')
    settings.set({'test': 123})
    print(settings.get())

    # Set some keys
    settings.set_key('history', 3)
    settings.set_key('history_items', ['thedzy', 'walterkovacs', 'jamiefraser'])

    settings.set_key('thedzy',
                     {'first': 'the',
                      'last': 'dzy',
                      'age': 30,
                      'children': {'susy': {'age': 3}, 'billy': {'age': 5}},
                      'mistresses': ['jill', 'sally', 'sarah', 'jennifer']})

    # Get all the settings
    print('\nAfter adding to preferences:')
    print(settings.get())

    # Get a key
    print('\nGet specific keys:')
    pref_data = settings.get('history')
    print('{} : {}'.format('history', pref_data))
    pref_data = settings.get('thedzy')
    print('{}[children] : {}'.format('thedzy', pref_data['children']))

    # Get a sub object
    print('\nGet specific key a few keys deep:')
    pref_data = settings.get_key('thedzy', 'children', 'susy')
    print('{} : {}'.format(['thedzy', 'children', 'susy'], pref_data))
    # Works with arrays the same as keys
    pref_data = settings.get_key('thedzy', 'mistresses', 3)
    print('{} : {}'.format(['thedzy', 'mistresses', 3], pref_data))

    # Check a value was found before using
    print('\nTest for keys:')
    pref_data = settings.get_key('thedzy', 'wives')
    if pref_data is not None:
        print('{} : {}'.format(['thedzy', 'wives'], pref_data))
    else:
        print('Cannot find key {}'.format(['thedzy', 'wives']))

    pref_data = settings.get_key('thedzy', 'children')
    if pref_data is not None:
        print('{} : {}'.format(['thedzy', 'children'], pref_data))
    else:
        print('Cannot find key {}'.format(['thedzy', 'children']))

    # Manual manipulation and extraction of data is still possible
    # while still retaining auto save
    print('\nChange keys by accessing data directly:')
    settings['history'] = 5
    print('History:', settings.get_key('history'))

    # Normal dict methods
    print('\nRegular dict methods still exist:')

    print('\nget(...)\n\tD.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.')
    pref_get = settings.get('history', 5)
    print('\t{} : {} = {}'.format('Get', 'history', pref_get))

    print('\nitems(...)\n\tD.items() -> a set-like object providing a view on D\'s items')
    pref_items = settings.items()
    print('\t{} : {}'.format('Items', pref_items))

    print('\nkeys(...)\n\tD.keys() -> a set-like object providing a view on D\'s keys')
    pref_keys = settings.keys()
    print('\t{} : {}'.format('Keys', pref_keys))

    print('\npop(...)\n\tD.pop(k[,d]) -> v, remove specified key and return the corresponding value.')
    pref_pop = settings.pop('thedzy')
    print('\t{} : {} = {}'.format('Pop', 'thedzy', pref_pop))

    print('\npopitem(...)\n\tD.popitem() -> (k, v), '
          'remove and return some (key, value) pair as a 2-tuple; but raise KeyError if D is empty.')
    pref_pop = settings.popitem()
    print('\t{} : {} = {}'.format('Popitem', pref_pop[0], pref_pop[1]))

    print('\nsetdefault(...)\n\tD.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D')
    prep_default = settings.setdefault('new_key', 8)
    print('\t{} : {} = {}'.format('Setdefault', 'new_key', prep_default))

    print('\nupdate(...)\n\tD.update([E, ]**F) -> None.  Update D from dict/iterable E and F.')
    settings.update({'new_key': 12})
    print('\t{} : {}'.format('Update', settings.get()))

    print('\nvalues(...)\n\tD.values() -> an object providing a view on D\'s values')
    pref_values = settings.values()
    print('\t{} : {}'.format('Values', pref_values))

    # Clear settings for the next run
    print('\nClear at set:')
    settings.clear()
    settings.set_keys(bool_example=True, integer_example=0, string_example='string')
    print(settings.get())

    # Only necessary if auto save is off
    settings.save()


if __name__ == '__main__':
    main()
