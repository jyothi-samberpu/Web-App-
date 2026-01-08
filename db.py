import json


class Database:
    def insert(self, name, age, phone, education, email, password):
        # Safely load existing users; if file missing or empty, start with empty dict
        try:
            with open('users.json', 'r') as rf:
                users = json.load(rf)
                if not isinstance(users, dict):
                    users = {}
        except (FileNotFoundError, json.JSONDecodeError):
            users = {}


        # Check for existing email
        if email in users:
            return 0


        # Add new user
        users[email] = {
            'name': name,
            'age': age,
            'phone': phone,
            'education': education,
            'email': email,
            'password': password
        }


        # Persist changes
        with open('users.json', 'w') as wf:
            json.dump(users, wf, indent=2)


        return 1


    def get_user(self, email):
        """Return the user dict for `email`, or None if not found."""
        try:
            with open('users.json', 'r') as rf:
                users = json.load(rf)
                if not isinstance(users, dict):
                    return None
        except (FileNotFoundError, json.JSONDecodeError):
            return None


        return users.get(email)


    def validate(self, email, password):
        """Return True if credentials are valid."""
        user = self.get_user(email)
        return bool(user and user.get('password') == password)
