import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


class KMEANS:
    image_name: str

    def __init__(self, image, img_name):
        """
        Constructs all the necessary attributes for the KMEANS object.

        :param image: (str) Full path of an image file
        :param img_name: (str) Name of the image file
        """
        KMEANS.image_name = img_name.split('.')[0]
        image_path = image
        bgr_image = cv.imread(image_path)
        self.remove_background(bgr_image)

    @staticmethod
    def remove_background(leaf_image):
        """
        Removes the background of an image based on its HSV values.

        :param leaf_image: An image file to have its background extracted
        :return: None
        """
        # Gaussian blur image to remove noise
        blured = cv.GaussianBlur(leaf_image, (1, 1), 0)

        rgb_image = cv.cvtColor(leaf_image, cv.COLOR_BGR2RGB)

        # Convert blured Image from BGR to HSV
        hsv_leaf = cv.cvtColor(blured, cv.COLOR_BGR2HSV)

        SV_channel = hsv_leaf.copy()

        SV_channel[:, :, 0] = np.zeros((SV_channel.shape[0], SV_channel.shape[1]))  # Set the 'H' channel to zero

        SV_channel[:, :, 2] = np.zeros((SV_channel.shape[0], SV_channel.shape[1]))  # Set the 'V' channel to zero

        # Create a binary mask from the SV Channel
        mask = cv.inRange(SV_channel, (0, 0, 0), (0, 85, 0))

        # Invert mask, White areas represent green components and black the background
        mask = cv.bitwise_not(mask)

        # perform bitwise_and between mask and hsv image
        background_extracted = cv.bitwise_and(hsv_leaf, hsv_leaf, mask=mask)

        KMEANS.segment_diseased(background_extracted, rgb_image)

    @staticmethod
    def segment_diseased(bg_extracted_hsv, rgb_image):
        """
        Segments an image to show the segmented part as white and the rest as black

        :param bg_extracted_hsv: An image file to be segmented
        :param rgb_image: An image file to be sent to the "plot_images" function
        :return: None
        """
        bg_extracted_rgb = cv.cvtColor(bg_extracted_hsv, cv.COLOR_HSV2RGB)
        ycrcb = cv.cvtColor(bg_extracted_rgb, cv.COLOR_RGB2YCrCb)

        cr = ycrcb[:, :, 1]
        z = cr.reshape((cr.shape[0] * cr.shape[1]))

        # convert to np.float32
        z = np.float32(z)

        # define criteria, number of clusters(K) and apply kmeans()
        criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 100, 1)
        K = 2
        ret, label, center = cv.kmeans(z, K, None, criteria, 10, cv.KMEANS_RANDOM_CENTERS)

        # Now convert back into uint8, and make original image
        center = np.uint8(center)
        res = center[label.flatten()]
        res2 = res.reshape(cr.shape)

        KMEANS.plot_images(rgb_image, cr, res2)

    @staticmethod
    def plot_images(original, processed, disease_area):
        """
        Plots three images to the screen and saves them in a PNG file

        :param original: An image file to be ploted
        :param processed: An image file to be ploted
        :param disease_area: An image file to be ploted
        :return: None
        """
        fig, axs = plt.subplots(1, 3)
        axs[0].set_title('Original Image')
        axs[0].set_xticks([])
        axs[0].set_yticks([])
        axs[0].imshow(original, cmap="gray")

        axs[1].set_title('Processed Image')
        axs[1].set_xticks([])
        axs[1].set_yticks([])
        axs[1].imshow(processed, cmap="gray")

        axs[2].set_title('Diseased Area')
        axs[2].set_xticks([])
        axs[2].set_yticks([])
        axs[2].imshow(disease_area, cmap="gray")

        plt.savefig(f'Plots/{KMEANS.image_name}.png')
        print('Image saved in "Plots" folder.\n')

        plt.show()
