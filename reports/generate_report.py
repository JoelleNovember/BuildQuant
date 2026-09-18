from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table
)
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(
    filename,
    project_name,
    project_number,
    location,
    floor_area,
    net_wall_area,
    tile_quantity,
    paint_area,
    tile_cost,
    paint_cost,
    total_cost
):

    document = SimpleDocTemplate(
        filename,
        pagesize=A4
    )

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "BUILDQUANT",
            styles["Title"]
        )
    )

    content.append(
        Paragraph(
            "Residential Quantity Estimate",
            styles["Heading2"]
        )
    )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            f"<b>Project:</b> {project_name}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"<b>Project Number:</b> {project_number}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"<b>Location:</b> {location}",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            "Quantities",
            styles["Heading2"]
        )
    )

    quantity_data = [
        ["Item", "Quantity"],
        ["Floor Area", f"{floor_area:.2f} m²"],
        ["Net Wall Area", f"{net_wall_area:.2f} m²"],
        ["Floor Tiles", f"{tile_quantity:.2f} m²"],
        ["Paint Area", f"{paint_area:.2f} m²"]
    ]

    content.append(
        Table(quantity_data)
    )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            "Cost Estimate",
            styles["Heading2"]
        )
    )

    cost_data = [
        ["Item", "Cost"],
        ["Floor Tiles", f"R{tile_cost:,.2f}"],
        ["Paint", f"R{paint_cost:,.2f}"],
        ["TOTAL", f"R{total_cost:,.2f}"]
    ]

    content.append(
        Table(cost_data)
    )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            "BuildQuant is an educational prototype and "
            "does not replace professional quantity surveying.",
            styles["Normal"]
        )
    )

    document.build(content)