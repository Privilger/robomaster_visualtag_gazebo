#!/usr/bin/python
import os
import cv2


class Generator:
	def __init__(self):
		with open('template/model.sdf', 'r') as f:
			self.sdf_template = f.read()

		with open('template/model.config', 'r') as f:
			self.config_template = f.read()

		with open('template/materials/scripts/visualtag.material', 'r') as f:
			self.material_template = f.read()

	def generate(self, tag_directory, tag_name, tag_size):
		img = cv2.imread('%s/%s.png' % (tag_directory, tag_name), cv2.IMREAD_COLOR)
		img = cv2.resize(img, (tag_size, tag_size), interpolation=cv2.INTER_NEAREST)

		if not os.path.exists('models/%s/materials/scripts' % tag_name):
			os.makedirs('models/%s/materials/scripts' % tag_name)

		if not os.path.exists('models/%s/materials/textures' % tag_name):
			os.makedirs('models/%s/materials/textures' % tag_name)

		with open('models/%s/model.sdf' % tag_name, 'w') as f:
			f.write(self.sdf_template.replace('visualtag_01', tag_name))

		with open('models/%s/model.config' % tag_name, 'w') as f:
			f.write(self.config_template.replace('visualtag_01', tag_name))

		with open('models/%s/materials/scripts/visualtag.material' % tag_name, 'w') as f:
			f.write(self.material_template.replace('visualtag_01', tag_name))

		cv2.imwrite('models/%s/materials/textures/%s.png' % (tag_name, tag_name), img)


def main():
	# Texture size must be power of two
	# With the default tag image size (10pix), tags will not be clearly rendered due to rescaling and interpolation
	tag_size = 1024

	generator = Generator()
	for i in range(1,45):
		generator.generate('imgs/', 'visualtag_%02d' % i, tag_size)


if __name__ == '__main__':
	main()
