from models import RectangleInput, ShapeProperties

def calculate_properties(data: RectangleInput, center: dict) -> ShapeProperties:
    """
    Calculates the area and perimeter of a rectangle.

    Args:
        data: A RectangleInput object containing the width and height.
        center: A dict containing the x,y coordinates of the center.

    Returns:
        A ShapeProperties object with the calculated area and perimeter.
    """
    area = data.width * data.height
    perimeter = 2 * (data.width + data.height)

    return ShapeProperties(
        area=round(area, 2),
        perimeter=round(perimeter, 2),
        center=center
    )