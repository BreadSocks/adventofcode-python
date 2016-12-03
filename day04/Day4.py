import hashlib


class AdventCoin:
    def __init__(self):
        self.secretKey = "yzbqklnj"
        self.counter = -1

    def new_hash(self):
        self.counter += 1
        new_string = self.secretKey + str(self.counter)
        md5_hash = hashlib.md5(new_string).hexdigest()
        return str(md5_hash)
