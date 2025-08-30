import json
import csv

# Load the annotations file
with open("data/annotations.json", "r") as f:
    data = json.load(f)

# Open CSV file to write
with open("taco_annotations.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["image_id", "category_id", "supercategory"])

    # Loop through annotations
    for ann in data["annotations"]:
        image_id = ann["image_id"]
        category_id = ann["category_id"]

        # Get supercategory from categories list
        supercategory = ""
        for cat in data["categories"]:
            if cat["id"] == category_id:
                supercategory = cat["supercategory"]
                break

        writer.writerow([image_id, category_id, supercategory])

print("CSV file taco_annotations.csv created successfully!")
