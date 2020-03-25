import keras
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPool2D
from keras.layers.normalization import BatchNormalization
from PIL import Image
from apis.config import DL_MODEL

ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'bmp']
def allowed_file(filename):
	return '.' in filename and \
		   filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class SimpleModel(object):

	def __init__(self, model_weights_path=''):

		self.path = model_weights_path

	def _create_model(self):
		
		num_classes = 10
		input_shape = (28, 28, 1)
		
		model = Sequential()
		model.add(Conv2D(32, kernel_size=(3, 3),activation='relu',kernel_initializer='he_normal',input_shape=input_shape))
		model.add(Conv2D(32, kernel_size=(3, 3),activation='relu',kernel_initializer='he_normal'))
		model.add(MaxPool2D((2, 2)))
		model.add(Dropout(0.20))
		model.add(Conv2D(64, (3, 3), activation='relu',padding='same',kernel_initializer='he_normal'))
		model.add(Conv2D(64, (3, 3), activation='relu',padding='same',kernel_initializer='he_normal'))
		model.add(MaxPool2D(pool_size=(2, 2)))
		model.add(Dropout(0.25))
		model.add(Conv2D(128, (3, 3), activation='relu',padding='same',kernel_initializer='he_normal'))
		model.add(Dropout(0.25))
		model.add(Flatten())
		model.add(Dense(128, activation='relu'))
		model.add(BatchNormalization())
		model.add(Dropout(0.25))
		model.add(Dense(num_classes, activation='softmax'))
		return model

	def process_image(self, fname):
		"""
		Processing image for prediction. Cropping and scaling so that the longest side it 20. 
		Then putting it in a center of 28x28 blank image. Returning array of normalized data.
		"""

		img = Image.open(fname)
		bbox = Image.eval(img, lambda px: 255-px).getbbox()
		
		if bbox == None:
			return None

		widthlen = bbox[2] - bbox[0]
		heightlen = bbox[3] - bbox[1]

		if heightlen > widthlen:
			widthlen = int(20.0 * widthlen/heightlen)
			heightlen = 20
		else:
			heightlen = int(20.0 * widthlen/heightlen)
			widthlen = 20

		hstart = int((28 - heightlen) / 2)
		wstart = int((28 - widthlen) / 2)

		img_temp = img.crop(bbox).resize((widthlen, heightlen), Image.NEAREST)

		new_img = Image.new('L', (28,28), 255)
		new_img.paste(img_temp, (wstart, hstart))

		imgdata = list(new_img.getdata())
		img_array = np.array([(255.0 - x) / 255.0 for x in imgdata])
		return img_array

	def _predict_single(self, model, fname=''):

		img_array = self.process_image(fname=fname)
		img_array = np.reshape(img_array, (1,28,28,1))