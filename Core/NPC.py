from Core.Body import Body


class NPC:
    def __init__(self, name="", age="", body=None, behavior="", backstory=""):
        self.name = name
        self.age = age
        self.body = body if body else Body()
        self.behavior = behavior
        self.backstory = backstory

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "body": self.body.to_dict(),
            "behavior": self.behavior,
            "backstory": self.backstory
        }
