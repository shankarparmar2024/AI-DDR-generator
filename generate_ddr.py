"""
generate_ddr.py

This version generates a DDR report locally
without using any external API.
"""


def generate_ddr(inspection_text, thermal_text, images):

    report = f"""
# Detailed Diagnostic Report (DDR)

## 1. Property Issue Summary
Based on the inspection and thermal reports, several structural and thermal
observations were identified within the property. The findings indicate
potential maintenance issues that may require further professional review.

---

## 2. Area-wise Observations

### Inspection Findings
{inspection_text[:800]}

### Thermal Findings
{thermal_text[:800]}

---

## 3. Probable Root Cause
The issues may be related to structural wear, moisture penetration,
or insulation inefficiencies observed during the inspection.

---

## 4. Severity Assessment
Severity is assessed as **Moderate**, because the issues could
impact structural integrity or energy efficiency if left unresolved.

---

## 5. Recommended Actions

- Conduct a detailed structural inspection
- Repair any visible cracks or damage
- Improve insulation in affected areas
- Monitor thermal anomalies over time

---

## 6. Additional Notes

Extracted images from the reports:

"""

    if images:
        for img in images:
            report += f"\nImage: {img}"
    else:
        report += "\nImage Not Available"

    report += """

---

## 7. Missing or Unclear Information

Some detailed measurements or diagnostic data were not clearly
available in the provided documents. Additional inspection may be required.

"""

    return report