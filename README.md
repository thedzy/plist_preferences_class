
# Plist Preference Management Class
## _class_ plist_preference
### An easy way to access, store and save preference files
------
JamfClassic interacts with the classic API of Jamf

Usage:
```python
settings = plist_preferences.Settings('com.github.thedzy.example', data_set=None, auto_save=True, verbose=False)

settings.set_key('key_name', value)

key_value = settings.get_key('key_name', value)
# or
key_value = settings['key_name']
```
_See: example.py_

```python
class Settings(dict):
    def __init__(self, name, data_set=None, auto_save=True, verbose=False):
        """
        Initialise the class variables
        Creates a self saving dict
        :param name: (str) Name of preference (ex, com.github.thedzy)
        :param data_set: (dict) The initial values to start with, None will load existing settings, or start new
        :param auto_save: (bool) Whether to automatically load and save to file or wait for specific calls
        """

    def __del__(self):
        """
        Destructor
        :return: (void)
        """

    def set_auto_save(self, auto_save):
        """
        Set/change the auto save option
        :param auto_save: (bool) Option
        :return: (bool) Setting
        """

    def save(self):
        """
        Save the file to disk, default automatic
        :return: (void)
        """

    def __save(self, override=False):
        """
        Save the file to disk, default automatic
        :param override: (bool) Override the auto save
        :return: (void)
        """

    def load(self):
        """
        Load the file from disk, default automatic
        :return: (void)
        """

    def clear(self, save_to_disk=False):
        """
        Remove all items from data structure
        :param save_to_disk: (bool) Save to disk when done (override)
        :return: (void)
        """

    def set(self, data_set=None, save_to_disk=False):
        """
        Set the entire preferences
        :param data_set: (dict) Preferences
        :param save_to_disk: (bool) Save to disk when done (override)
        :return: (void))
        """

    def set_key(self, key, value, save_to_disk=False):
        """
        Set a key at the root level
        :param key: (str) Key name
        :param value: (any) Value for key pair
        :param save_to_disk: (bool) Save to disk when done (override)
        :return: (void)
        """

    def set_keys(self, save_to_disk=False, **kwargs):
        """
        Set keys at the root level
        :param save_to_disk: (bool) Save to disk when done (override)
        :return: (void)
        """

    def get(self, key=None, value=None):
        """
        Get key at root or root
        :param key: (str) Key names from parent to children
        :param default: (any) Value returned if key does not exist
        :return: (any) Value
        """

    def get_key(self, *keys, default=None):
        """
        Get key and different depths
        :param keys: (list) Key names from parent to children
        :param default: (any) Value returned if key does not exist
        :return: (DataObj) Contains data, err, success
        """

    def pop(self, key, default=None, save_to_disk=False):
        """
        Remove specified key and return the corresponding value.
        :param key: (str) Key
        :param default: (any) Value returned if key does not exist
        :param save_to_disk: (bool) Save to disk when done (override)
        :return: (any) Value of key pair
        """

    def popitem(self, default=None, save_to_disk=False):
        """
        Remove and return default if empty
        :param save_to_disk: (bool) Save to disk when done (override)
        :param default: (any) Default value if not found
        :return: (any) Value of key pair
        """

    def setdefault(self, key, default=None, save_to_disk=False):
        """
        Like .get() but sets if missing
        :param key: (str) Key name
        :param default: (any) Default value if none
        :param save_to_disk: (bool) Save to disk when done (override)
        :return:
        """

    def update(self, dictionary=None, save_to_disk=False, **kwargs):
        """
        Update settings from dict/iterable
        :param dictionary: (dict) To update settings with
        :param save_to_disk: (bool) Save to disk when done (override)
        :param kwargs: (dict) To update settings with
        :return:
        """

    def __setitem__(self, key, value):
        """
        Set self[key] to value
        Override, save on change of settings
        :param key: (str) Key name
        :param value: (any) Value of pair
        :return: (void)
        """
```
