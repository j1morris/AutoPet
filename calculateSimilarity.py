import numpy as np
import cv2
from matplotlib import pyplot as plt
from datetime import datetime

# Paths to the images
NEG_PATH = "./data/negSamples/"
POS_PATH = "./data/posSamples/"
NEG_REF  = "./data/negSamples/sample0.jpg"


def cosine(img1, img2):
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

def segmenting(img1, img2, num_seg):

    # Get the image dimensions and calcualte segment length
    x_len, y_len, _ = img1.shape
    seg_len = y_len // num_seg

    # Used to hold the segments
    img1s = []
    img2s = []

    # print("img_dim: ({}, {}) -> seg_len: {}".format(x_len, y_len, seg_len))

    # Create the segments
    for i in range(num_seg):
        start = seg_len * i
        end   = start + seg_len
        img1s.append(img1[:,start:end])
        img2s.append(img2[:,start:end])

    # print("num_seg: {}, seg_dim: {}".format(len(img1s), img1s[0].shape))
    # print("num_seg: {}, seg_dim: {}".format(len(img2s), img1s[0].shape))

    # for i in range(num_seg):
    #     cv2.imwrite('./data/debug/img1_{}.jpg'.format(i), img1s[i])
    #     cv2.imwrite('./data/debug/img2_{}.jpg'.format(i), img2s[i])

    # For each segment, calculate the cosine similarity
    similarities = [cosine(img1s[i], img2s[i]) for i in range(num_seg)]

    # print("{} -> {}".format(similarities, min(similarities)))

    # Return the minimum similarity
    return min(similarities)
      

if __name__ == "__main__":

    neg_sim = []
    pos_sim = []

    # Open and crop
    neg_ref = cv2.imread(NEG_REF)
    neg_ref = neg_ref[300:600,100:1000]

    num_seg = 4
    # segmenting(neg_ref, neg_ref, num_seg)

    for i in range(25):

        # Open and crop
        img2 = cv2.imread(NEG_PATH + "sample" + str(i) + ".jpg")
        img2 = img2[300:600,100:1000]

        # neg_sim.append(cosine(neg_ref, img2))
        neg_sim.append(segmenting(neg_ref, img2, num_seg))

    for i in range(25):

        # Open and crop
        img2 = cv2.imread(POS_PATH + "sample" + str(i) + ".jpg")
        img2 = img2[300:600,100:1000]

        # pos_sim.append(cosine(neg_ref, img2))
        pos_sim.append(segmenting(neg_ref, img2, num_seg))

    # Graph distribution of similarity values
    bins = np.linspace(0.8, 1.1, 300)

    plt.hist(neg_sim, bins, alpha=0.5, label='negative similarities')
    plt.hist(pos_sim, bins, alpha=0.5, label='positive similarities')
    plt.legend(loc="upper right")
    # plt.savefig("./data/distributions/distribution_cosine.png")
    plt.savefig("./data/distributions/distribution_{}_segments.png".format(num_seg))
