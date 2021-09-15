from ycgcr import YCBCR
from k_means import KMEANS
import os


def join_path(imagepath, file):
    return os.path.join(imagepath, file)


def main():
    image_path = 'images'
    if os.path.exists(image_path):
        # List all files from a given directory
        filenames = [file for file in os.listdir(image_path) if os.path.isfile(join_path(image_path, file))]

        # Filter files to only have image files of type JPG, JPEG and PNG
        image_files = [img_file for img_file in filenames if img_file.split('.')[-1] in ['jpg', 'jpeg', 'png']]

        for img in image_files:
            full_image_path = os.path.join(image_path, img)
            KMEANS(full_image_path)
    else:
        print("Incorrent path")


if __name__ == "__main__":
    main()
