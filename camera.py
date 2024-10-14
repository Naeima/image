# https://stackoverflow.com/questions/21697645/how-to-extract-metadata-from-a-image-using-python
# https://medium.com/vacatronics/how-to-extract-metadata-from-images-using-python-cd8de8ab48c5
# https://www.codegrepper.com/code-examples/python/iterate+over+list+of+images+in+folder+python
# https://realpython.com/storing-images-in-python/
# IPv4 Address. . . . . . . . . . . : 192.168.0.78 (windows)
# IPv4 Address. . . . . . . . . . . : 192.168.0.87 (mac)
# https://stackoverflow.com/questions/48845368/how-can-generate-a-image-url-from-image
import cv2
from PIL import Image, ExifTags
from PIL.ExifTags import TAGS, GPSTAGS
import PIL.Image
import piexif 
import piexif
import os
import glob
import requests
from io import BytesIO
import cv2
import json

# iterate through images folder and load images.
images = glob.glob("Images16/*.jpg")

for image in images:
    exif_dict = piexif.load(image)


# Extract thumbnail and save it, if exists
    thumbnail = exif_dict.pop('thumbnail')
    if thumbnail is not None:
        with open('thumbnail.jpg', 'wb') as f:
            f.write(thumbnail)

# Iterate through all the other ifd names and print them
    print(f'Metadata for {image}:')
    for ifd in exif_dict:
        print(f'{ifd}:')
        for tag in exif_dict[ifd]:
            tag_name = piexif.TAGS[ifd][tag]["name"]
            tag_value = exif_dict[ifd][tag]

        # Avoid print a large value, just to be pretty
            if isinstance(tag_value, bytes):
                tag_value = tag_value[:10]
            print(f'\t{tag_name:25}: {tag_value}')
    # print()

    # mydata = [i for i in tag_name]
    
    with open('camera.csv', 'w') as outfile:
       outfile.write(str(exif_dict))
  










# def store_many_disk(images, labels) :
#     """ Stores an array of images to disk
#         Parameters:
#         ---------------
#         images       images array, (N, 32, 32, 3) to be stored
#         labels       labels array, (N, 1) to be stored
#     """
#     images = glob.glob("Images16/*.jpg")
#     num_images = len(images)

#     # Save all the images one by one
#     for i, image in enumerate(images):
#         Image.fromarray(image).save("DGFC" / f"{i}.png")

#     # Save all the labels to the csv file
#     with open("DGFC"/ f"{num_images}.csv", "w") as csvfile:
#         writer = csv.writer(
#             csvfile, delimiter=" ", quotechar="|", quoting=csv.QUOTE_MINIMAL
#         )
#         for label in labels:
#             # This typically would be more than just one value per row
#             writer.writerow([label])

# def store_many_lmdb(images, labels):
#     """ Stores an array of images to LMDB.
#         Parameters:
#         ---------------
#         images       images array, (N, 32, 32, 3) to be stored
#         labels       labels array, (N, 1) to be stored
#     """
#     num_images = len(images)

#     map_size = num_images * images[0].nbytes * 10

#     # Create a new LMDB DB for all the images
#     env = lmdb.open(str(lmdb_dir / f"{num_images}_lmdb"), map_size=map_size)

#     # Same as before — but let's write all the images in a single transaction
#     with env.begin(write=True) as txn:
#         for i in range(num_images):
#             # All key-value pairs need to be Strings
#             value = CIFAR_Image(images[i], labels[i])
#             key = f"{i:08}"
#             txn.put(key.encode("ascii"), pickle.dumps(value))
#     env.close()

# def store_many_hdf5(images, labels):
#     """ Stores an array of images to HDF5.
#         Parameters:
#         ---------------
#         images       images array, (N, 32, 32, 3) to be stored
#         labels       labels array, (N, 1) to be stored
#     """
#     num_images = len(images)

#     # Create a new HDF5 file
#     file = h5py.File(hdf5_dir / f"{num_images}_many.h5", "w")

#     # Create a dataset in the file
#     dataset = file.create_dataset(
#         "images", np.shape(images), h5py.h5t.STD_U8BE, data=images
#     )
#     meta_set = file.create_dataset(
#         "meta", np.shape(labels), h5py.h5t.STD_U8BE, data=labels
#     )
#     print()
#     file.close()


# content ='image01'
# response = requests.get(url)
# img = Image.open(BytesIO(response.content)
# 

# filenames = glob.glob("images16/*.jpg")
# filenames.sort()
# images = [cv2.imread(img) for img in filenames]

# for img in images:
    
# images = Image.open('Images16/*.jpg')
# image = Image.open('image01.jpg')
# # for image in images:
# # summarize some details about the image
# print(image.format)
# print(image.mode)
# print(image.size)
# # show the image
# image.show()