from PIL import Image
import glob

#display the images characteristics
img_path = 'F:\Python\Resize_using_python\data/gubb_bNNER-01.jpg'

im = Image.open(img_path)
print('\n')
print('{}'.format(img_path))
print('SIZE : {}'.format(im.size))
print('image mode : {}'.format(im.mode))
#im.show()


#empty list
image_list = []
resized_images = []
file_name = []


#append images to a list
for filename in glob.glob('F:\Python\Resize_using_python\data\*.jpg'):
    print(filename)
    image = Image.open(filename)
    image_list.append(image)
    file_name.append(filename)

for image in image_list:
    image.resize((900,900))
    resized_images.append(image)


#save resized images to new folder
#could also probably use os to crate new folder


for (i,new) in enumerate(resized_images):
    new.save('{}{}{}'.format('F:\Python\Resize_using_python\data_resize\File_',i+1,'.jpg'))