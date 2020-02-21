token = ""

try:
    from local_config import token
except ImportError:
    print("token doesn't exist")
