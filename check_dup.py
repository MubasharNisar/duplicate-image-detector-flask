from imagededup.methods import PHash
from imagededup.utils import plot_duplicates
phasher = PHash()
encodings = phasher.encode_images(image_dir='images/')
duplicates = phasher.find_duplicates(encoding_map=encodings)
plot_duplicates(image_dir='images/',
                duplicate_map=duplicates,
                filename='Rails_1.png')

