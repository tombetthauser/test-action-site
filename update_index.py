import os

def get_image_files(directory):
    """Return a list of image files in the given directory."""
    supported_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp')
    return [f for f in os.listdir(directory) if f.endswith(supported_extensions)]

def update_index_html(image_files, index_path='index.html'):
    """Update the index.html file with img tags for the given image files."""
    if not image_files:
        return

    img_tags = ''.join([f'<img src="{file}" alt="{file}">\n' for file in image_files])

    # Read the existing content of the index.html
    with open(index_path, 'r') as file:
        content = file.readlines()

    # Find the place to insert the images (e.g., after a placeholder comment)
    for i, line in enumerate(content):
        if '<!-- IMAGES_PLACEHOLDER -->' in line:
            content.insert(i + 1, img_tags)
            break
    else:
        # If no placeholder, add images at the end
        content.append(img_tags)

    # Write the updated content back to the index.html
    with open(index_path, 'w') as file:
        file.writelines(content)

if __name__ == "__main__":
    image_folder = 'images'  # The folder where images are stored
    index_file = 'index.html'
    
    images = get_image_files(image_folder)
    update_index_html(images, index_file)
