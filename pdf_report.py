from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.platypus import Paragraph
from reportlab.platypus import Spacer

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

from datetime import datetime


def generate_pdf(filename, prediction_df):

    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate(filename)

    story = []

    # Title
    story.append(
        Paragraph(
            "<b>EduAI Copilot - Student Performance Report</b>",
            styles["Title"]
        )
    )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            f"Generated On : {datetime.now()}",
            styles["Normal"]
        )
    )

    story.append(Spacer(1, 20))

    total = len(prediction_df)

    high = (prediction_df["Prediction"] == "High").sum()
    medium = (prediction_df["Prediction"] == "Medium").sum()
    low = (prediction_df["Prediction"] == "Low").sum()

    story.append(
        Paragraph(f"<b>Total Students :</b> {total}", styles["Normal"])
    )

    story.append(
        Paragraph(f"<b>High :</b> {high}", styles["Normal"])
    )

    story.append(
        Paragraph(f"<b>Medium :</b> {medium}", styles["Normal"])
    )

    story.append(
        Paragraph(f"<b>Low :</b> {low}", styles["Normal"])
    )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph("<b>Prediction Table</b>", styles["Heading2"])
    )

    data = [prediction_df.columns.tolist()]

    data.extend(prediction_df.values.tolist())

    table = Table(data)

    table.setStyle(

        TableStyle([

            ("BACKGROUND", (0,0), (-1,0), colors.darkblue),

            ("TEXTCOLOR", (0,0), (-1,0), colors.white),

            ("GRID", (0,0), (-1,-1), 1, colors.black),

            ("BACKGROUND", (0,1), (-1,-1), colors.beige),

            ("ALIGN",(0,0),(-1,-1),"CENTER"),

            ("BOTTOMPADDING",(0,0),(-1,0),10)

        ])

    )

    story.append(table)

    story.append(Spacer(1,20))

    story.append(
        Paragraph(
            "<b>AI Recommendation</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            "Students predicted as Low performers should improve attendance, increase study hours, maintain healthy sleep, and reduce gaming/social media usage.",
            styles["BodyText"]
        )
    )

    doc.build(story)