import os

# Define the path to the images folder and the index.html file
images_folder = 'images'
index_file = 'index.html'

# Get a list of image files in the folder, sorted by modification time in reverse order
image_files = sorted(
    [f for f in os.listdir(images_folder) if f.lower().endswith(('png', 'jpg', 'jpeg', 'gif'))],
    key=lambda x: os.path.getmtime(os.path.join(images_folder, x)),
    reverse=True
)

# Generate the HTML content for the images
image_html = ""
for image_file in image_files:
    img_src = os.path.join(images_folder, image_file)
    filename = os.path.splitext(image_file)[0].replace('-', ' ')
    image_html += f'<img src="{img_src}">\n<p>{filename}</p>\n'

# Read the existing index.html file
with open(index_file, 'r') as file:
    html_content = file.read()

# Find the start and end of the image container div
start_marker = '<div id="image-container">'
end_marker = '</div>'
start_index = html_content.find(start_marker)
end_index = html_content.find(end_marker, start_index)

# If the div is found, replace its content; otherwise, create a new div
if start_index != -1 and end_index != -1:
    new_html_content = html_content[:start_index + len(start_marker)] + '\n' + image_html + html_content[end_index:]
else:
    new_html_content = html_content.replace(
        '</body>',
        f'<div id="image-container">\n{image_html}</div>\n</body>'
    )

# Write the updated HTML content back to the index.html file
with open(index_file, 'w') as file:
    file.write(new_html_content)

print("index.html has been updated successfully.")




















# import os

# def get_image_files(directory):
#     """Return a list of image files in the given directory."""
#     supported_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp')
#     return [f for f in os.listdir(directory) if f.endswith(supported_extensions)]

# def update_index_html(image_files, index_path='index.html'):
#     """Update the index.html file with img tags for the given image files."""
#     if not image_files:
#         return

#     img_tags = ''.join([f'<img src="./images/{file}" alt="{file}">\n' for file in image_files])

#     # Read the existing content of the index.html
#     with open(index_path, 'r') as file:
#         content = file.readlines()

#     # Find the place to insert the images (e.g., after a placeholder comment)
#     for i, line in enumerate(content):
#         if '<!-- IMAGES_PLACEHOLDER -->' in line:
#             content.insert(i + 1, img_tags)
#             break
#     else:
#         # If no placeholder, add images at the end
#         content.append(img_tags)

#     # Write the updated content back to the index.html
#     with open(index_path, 'w') as file:
#         file.writelines(content)

# if __name__ == "__main__":
#     image_folder = 'images'  # The folder where images are stored
#     index_file = 'index.html'
    
#     images = get_image_files(image_folder)
#     update_index_html(images, index_file)
