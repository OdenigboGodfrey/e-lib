POSITIVE = 1
NEUTRAL = 0
NEGATIVE = -1
PASSWORD_SALT = '$.2@7!29^Bc;a)f2:144f6$@_)5196b01.%6.FdD04dA0%'
USER = 'U'
STAFF = 'S'
POST = 'POST'
GET = 'GET'
ALL = 'all'
SINGLE = 'single'


class AppStrings:
    def get_all(self):
        return strings

    def get_single(self, key, return_type="default"):
        if not key in self.strings:
            return "Key not found."
        if (return_type == 'dict'):
            return { key: self.strings[key]}
        return self.strings[key]

    def get_multiple(self, keys):
        to_be_returned = {}
        for key in keys:
            to_be_returned.update({key: self.get_single(key)})
        return to_be_returned

    # String constants
    strings = {
        "email_taken": "Email address has been taken.",
        'error_occured': "An error occured.",
        'registration_ok': "Registration successful.",
        'password_not_same': "Passwords do not match.",
        'wrong_password': "Password is incorrect.",
        'wrong_email': "Email address not found.",
        'new_user_failed': "User creation failed.",
        'get_item_types_failed': "Failed to get item types.",
        'no_item_types': "No item types",
        'no_categories': "No categories.",
        'failed_to_add_item': "Failed to add item.",
        'item_saved': "Item saved.",
        'item_id_needed': "Item id is needed.",
        'failed_to_get_item': "Failed to get item(s).",
        'borrow_failed': "Failed to borrow item."
    }

