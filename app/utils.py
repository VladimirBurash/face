from skimage import io

from app import DETECTOR, SP, FACEREC


def get_descriptor(path):
    shape = None
    desc = None
    img = io.imread(path)
    dets = DETECTOR(img, 1)
    for k, d in enumerate(dets):
        print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
            k, d.left(), d.top(), d.right(), d.bottom()))
        shape = SP(img, d)
    if shape:
        desc = FACEREC.compute_face_descriptor(img, shape)
    return desc
