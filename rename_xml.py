from PIL import Image
import os
import shutil

input_folder = "/home/nvidia/Finalproject/test_xml" # Folder with your original pictures
output_folder = "test_xml_renamed"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

ext= '.xml'

counter = 10000


for filename in os.listdir(input_folder):

    if filename.lower().endswith(ext):
        try:

            input_path = os.path.join(input_folder, filename)
            new_filename = f"{counter:03d}{ext}"
            output_path = os.path.join(output_folder, new_filename)

            shutil.copy(input_path,output_path)



            print(f"✓ Renamed: {filename} ➝ {new_filename}")


            counter += 1

        except Exception as e:
            print(f"✗ Error with {filename}: {e}")

print("\nAll done! Check the 'resized_images' folder for your 512x512 pictures.")
