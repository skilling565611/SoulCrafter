class Body:
    def __init__(self, race="", species="", variant="", sex=""):
        self.race = race
        self.species = species
        self.variant = variant
        self.sex = sex

    def to_dict(self):
        return {
            "race": self.race,
            "species": self.species,
            "variant": self.variant,
            "sex": self.sex
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            race=data.get("race", ""),
            species=data.get("species", ""),
            variant=data.get("variant", ""),
            sex=data.get("sex", "")
        )
