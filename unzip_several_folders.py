import os
import zipfile

# Set the path where your zipped folders are located
zip_folder_path = r"C:\Users\dhawa\Desktop\mEng Project\virtual_bidding\RT_LBMP"
output_folder = zip_folder_path
# output_folder = r"C:\Users\dhawa\Desktop\mEng Project\virtual_bidding\RT_LBMP"  

# Ensure the output directory exists
os.makedirs(output_folder, exist_ok=True)

# Loop through all ZIP files in the folder
for filename in os.listdir(zip_folder_path):
    if filename.endswith(".zip"):  # Process only ZIP files
        zip_path = os.path.join(zip_folder_path, filename)
        extract_to = os.path.join(output_folder, filename[:-4])  # Create a folder per ZIP file

        # Ensure the extraction folder exists
        os.makedirs(extract_to, exist_ok=True)

        # Extract the ZIP file
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)

        print(f"Extracted: {filename} -> {extract_to}")

print("✅ All ZIP files extracted successfully!")
