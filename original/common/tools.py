import uuid


def generate_acode(length=8):
    return uuid.uuid4().hex[:length]
