import os

ENV = bool(os.environ.get("STRING_SESSION", False))
    
    from config import Development as Config  # noqa
