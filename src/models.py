from dataclasses import dataclass, asdict

@dataclass
class RectangleInput:
    """Input data contract for rectangle calculations."""
    width: float
    height: float

@dataclass
class ShapeProperties:
    """Output data contract for shape properties."""
    area: float
    perimeter: float
    center: dict[str, float]

    def to_json(self):
        """Converts the dataclass instance to a dictionary."""
        return asdict(self)