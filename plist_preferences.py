#!/usr/bin/env python3
"""
Script:	plist_preferences.py
Date:	2020-04-20

Platform: macOS

Description:
Easily manage a plist file and settings
Simplifies the need to continually check that file exists, keys exists, etc
When setting keys, or editing settings directly they are saved to disk (via auto save or save())
"""
__author__ = "thedzy"
__copyright__ = "Copyright 2020, thedzy"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "thedzy"
__email__ = "thedzy@hotmail.com"
__status__ = "Developer"

import pathlib
import plistlib
import logging


class Settings(dict):
    def __init__(self, name, data_set=None, auto_save=True, verbose=False):
        """
        Initialise the class variables
        Creates a self saving dict
        :param name: (str) Name of preference (ex, com.github.thedzy)
        :param data_set: (dict) The initial values to start with, None will load existing settings, or start new
        :param auto_save: (bool) Whether to automatically load and save to file or wait for specific calls
        """
        self.name = name

        if name is not None:
            self.file = pathlib.Path.joinpath(pathlib.Path.home(), 'Library', 'Preferences', name + '.plist')
            self.auto_save = auto_save
        else:
            self.auto_save = False

        self.verbose = verbose

        if data_set is None:
            data_set = {}
            if name is not None:
                if pathlib.Path.exists(self.file):
                    if self.verbose:
                        logging.info('Working with {}'.format(self.file))
                    self.load()
                else:
                    if self.verbose:
                        logging.info('Creating with {}'.format(self.file))

        for key, value in data_set.items():
            if isinstance(value, dict):
                data_set[key] = Settings(None, value)

        super().__init__(data_set)

    def __del__(self):
        """
        Destructor
        :return: (void)
        """
        if self.name is not None:
            self.__save()

    def set_auto_save(self, auto_save):
        """
        Set/change the auto save option
        :param auto_save: (bool) Option
        :return: (bool) Setting
        """
        self.auto_save = bool(auto_save)
        return self.auto_save

    def save(self):
        """
        Save the file to disk, default automatic
        :return: (void)
        """
        if self.verbose:
            logging.info('Saving file {}'.format(self.file))

        if self.name is None:
            return

        try:
            with open(self.file, 'wb') as settings_file:
                plistlib.dump(self, settings_file, sort_keys=True)
        except Exception as err:
            logging.warning('File not saved: Reason {}'.format(err))

    def __save(self, override=False):
        """
        Save the file to disk, default automatic
        :param override: (bool) Override the auto save
        :return: (void)
        """
        try:
            if self.auto_save or override:
                with open(self.file, 'wb') as settings_file:
                    plistlib.dump(self, settings_file, sort_keys=True)
        except Exception as err:
            logging.warning('File not saved: Reason {}'.format(err))

    def load(self):
        """
        Load the file from disk, default automatic
        :return: (void)
        """
        try:
            with open(self.file, 'rb') as settings_file:
                self.set(plistlib.load(settings_file))
        except FileNotFoundError as err:
            logging.warning('{}'.format(err))

    def clear(self, save_to_disk=False):
        """
        Remove all items from data structure
        :param save_to_disk: (bool) Save to disk when done (override)
        :return: (void)
        """
        super().clear()
        self.__save(save_to_disk)

    def set(self, data_set=None, save_to_disk=False):
        """
        Set the entire preferences
        :param data_set: (dict) Preferences
        :param save_to_disk: (bool) Save to disk when done (override)
        :return: (void))
        """
        # Clear the current data from the data structure
        self.clear()

        # Initialise with new data
        if data_set is None:
            super().__init__({})
        else:
            super().__init__(data_set)

        self.__save(save_to_disk)

    def set_key(self, key, value, save_to_disk=False):
        """
        Set a key at the root level
        :param key: (str) Key name
        :param value: (any) Value for key pair
        :param save_to_disk: (bool) Save to disk when done (override)
        :return: (void)
        """
        self[key] = value

        self.__save(save_to_disk)

    def set_keys(self, save_to_disk=False, **kwargs):
        """
        Set keys at the root level
        :param save_to_disk: (bool) Save to disk when done (override)
        :return: (void)
        """
        super().__init__(kwargs)

        self.__save(save_to_disk)

    def get(self, key=None, default=None):
        """
        Get key at root or root
        :param key: (str) Key names from parent to children
        :param default: (any) Value returned if key does not exist
        :return: (any) Value
        """
        if key is None:
            return self
        else:
            return super().get(key, default)

    def get_key(self, *keys, default=None):
        """
        Get key and different depths
        :param keys: (list) Key names from parent to children
        :param default: (any) Value returned if key does not exist
        :return: (any) Value
        """
        if len(keys) == 0:
            return self

        if len(keys) == 1:
            return self.get(keys, default)

        parent_key = self
        try:
            for key in keys:
                parent_key = parent_key[key]
        except KeyError:
            return default
        except TypeError:
            return default
        return parent_key

    def pop(self, key, default=None, save_to_disk=False):
        """
        Remove specified key and return the corresponding value.
        :param key: (str) Key
        :param default: (any) Value returned if key does not exist
        :param save_to_disk: (bool) Save to disk when done (override)
        :return: (any) Value of key pair
        """
        try:
            value = super().pop(key)
            self.__save(save_to_disk)
        except Exception as err:
            value = default
        return value

    def popitem(self, default=None, save_to_disk=False):
        """
        Remove and return default if empty
        :param save_to_disk: (bool) Save to disk when done (override)
        :param default: (any) Default value if not found
        :return: (any) Value of key pair
        """
        try:
            value = super().popitem()
            self.__save(save_to_disk)
        except Exception as err:
            value = default
        return value

    def setdefault(self, key, default=None, save_to_disk=False):
        """
        Like .get() but sets if missing
        :param key: (str) Key name
        :param default: (any) Default value if none
        :param save_to_disk: (bool) Save to disk when done (override)
        :return:
        """
        try:
            value = super().setdefault(key, default)
            self.__save(save_to_disk)
        except Exception as err:
            value = default
        return value

    def update(self, dictionary=None, save_to_disk=False, **kwargs):
        """
        Update settings from dict/iterable
        :param dictionary: (dict) To update settings with
        :param save_to_disk: (bool) Save to disk when done (override)
        :param kwargs: (dict) To update settings with
        :return:
        """
        if dictionary is not None:
            super().update(dictionary)
        super().update(kwargs)
        self.__save(save_to_disk)

    def __setitem__(self, key, value):
        """
        Set self[key] to value
        Override, save on change of settings
        :param key: (str) Key name
        :param value: (any) Value of pair
        :return: (void)
        """
        if isinstance(value, dict):
            child = Settings(None, value)
        else:
            child = value
        super().__setitem__(key, child)

        self.__save()
