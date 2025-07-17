from PIL import Image
import os

input_folder = "/home/nvidia/Finalproject/test_img" # Folder with your original pictures
output_folder = "test_img_renamed"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.jfif']

counter = 10000


for filename in os.listdir(input_folder):

    if any(filename.lower().endswith(ext) for ext in image_extensions):
        try:

            input_path = os.path.join(input_folder, filename)
            img = Image.open(input_path)
            img = img.convert('RGB')


            #resized_img = img.resize((512, 512))


            _, ext = os.path.splitext(filename)
            new_filename = f"{counter:03d}{ext}"


            output_path = os.path.join(output_folder, new_filename)
            img.save(output_path)

            print(f"✓ Renamed: {filename} ➝ {new_filename}")


            counter += 1

        except Exception as e:
            print(f"✗ Error with {filename}: {e}")

print("\nAll done! Check the 'resized_images' folder for your 512x512 pictures.")
