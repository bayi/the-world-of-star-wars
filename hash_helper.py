from werkzeug.security import generate_password_hash, check_password_hash


def set_password_hash(password):
    return generate_password_hash(password)


def check_password(self, password):
        return check_password_hash(self.pw_hash, password)