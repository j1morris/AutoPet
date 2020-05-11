import numpy as np
import cv2
from matplotlib import pyplot as plt

# Paths to the images
NEG_PATH = "./data/negSamples/"
POS_PATH = "./data/posSamples/"
NEG_REF  = "./data/negSamples/sample0.jpg"


def calculate (img1, img2):
    # Convert to gray
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # Flatten the 2-D arrays
    img1 = img1.flatten()
    img2 = img2.flatten()

    img1 = np.array(img1, dtype=np.int64)
    img2 = np.array(img2, dtype=np.int64)

    # Calculate cosine similarity
    numerator = np.dot(img1, img2)
    norm1 = np.linalg.norm(img1)
    norm2 = np.linalg.norm(img2)
    denominator = norm1 * norm2

    return (numerator / denominator)


if __name__ == "__main__":

    neg_sim = []
    pos_sim = []

    # Open and crop
    neg_ref = cv2.imread(NEG_REF)
    neg_ref = neg_ref[300:600,100:1000]

    for i in range(25):

        # Open and crop
        img2 = cv2.imread(NEG_PATH + "sample" + str(i) + ".jpg")
        img2 = img2[300:600,100:1000]

        neg_sim.append(calculate(neg_ref, img2))

    for i in range(25):

        # Open and crop
        img2 = cv2.imread(POS_PATH + "sample" + str(i) + ".jpg")
        img2 = img2[300:600,100:1000]

        pos_sim.append(calculate(neg_ref, img2))

    # Graph distribution of similarity values
    bins = np.linspace(0.8, 1.1, 300)

    plt.hist(neg_sim, bins, alpha=0.5, label='negative similarities')
    plt.hist(pos_sim, bins, alpha=0.5, label='positive similarities')
    plt.legend(loc="upper right")
    plt.savefig("distribution.png")
