from Core.Body import Body


class Player:
    def __init__(self, name="Player", level=1, health=100, energy=100, body=None):
        self.name = name
        self.level = level
        self.health = health
        self.energy = energy
        self.body = body if body else Body()

    def to_dict(self):
        return {
            "name": self.name,
            "level": self.level,
            "health": self.health,
            "energy": self.energy,
            "body": self.body.to_dict()
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data.get("name", "Player"),
            level=data.get("level", 1),
            health=data.get("health", 100),
            energy=data.get("energy", 100),
            body=Body.from_dict(data.get("body", {}))
        )
