from random import sample
import string

def get_random_password(n) -> str:

    m = string.ascii_lowercase + string.ascii_uppercase + string.digits
    password = "".join(sample(m, n))
    return password

print(get_random_password(8))