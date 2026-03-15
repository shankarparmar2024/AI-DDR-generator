"""
main.py

Complete pipeline:

1. Extract text + images from Inspection Report
2. Extract text + images from Thermal Report
3. Send both to AI
4. Generate DDR report
5. Save final report
"""

import os
from extract_data import extract_text_and_images
from generate_ddr import generate_ddr


def main():

    # create folders if they don't exist
    os.makedirs("extracted_images", exist_ok=True)
    os.makedirs("output", exist_ok=True)

    print("Reading Inspection Report...")

    inspection_text, inspection_images = extract_text_and_images(
        "input_docs/inspection_report.pdf.pdf",
        "extracted_images"
    )

    print("Reading Thermal Report...")

    thermal_text, thermal_images = extract_text_and_images(
        "input_docs/thermal_report.pdf",
        "extracted_images"
    )

    # combine images
    all_images = inspection_images + thermal_images

    print("Generating DDR Report with AI...")

    ddr_report = generate_ddr(
        inspection_text,
        thermal_text,
        all_images
    )

    # save report
    with open("output/ddr_report.md", "w", encoding="utf-8") as f:
        f.write(ddr_report)

    print("\nDDR Report Generated Successfully!")
    print("Check the output/ddr_report.md file")


if __name__ == "__main__":
    main()