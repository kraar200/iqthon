import os

ENV = bool(os.environ.get("STRING_SESSION", False))

if ENV:
    
    from config import Development as Config  # noqa
