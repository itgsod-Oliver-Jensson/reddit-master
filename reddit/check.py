class Check(object):
    def __init__(self, data):
        self.data = data

    def check_if_title_is_cool(self):
        text = self.data

        cooltext = ["Le", "Autism", "Atheism", "cool", "xXx"]

        for s in text.split(" "):
            for c in cooltext:
                if s == c:
                    return True
