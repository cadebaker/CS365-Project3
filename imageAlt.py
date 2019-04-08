from PIL import Image, ImageFilter
import os


count = 0

car_manipulated = "Traverse"

for filename in os.listdir("/Users/brendannahed/Documents/Work/Current_Classes/CIS_365/Project_3/training_images/"+car_manipulated):
	try:
		im = Image.open(os.path.join('/Users/brendannahed/Documents/Work/Current_Classes/CIS_365/Project_3/training_images/'+car_manipulated,filename))
		im_sharp = im.filter(ImageFilter.DETAIL)
		im_sharp.save('training_images/'+car_manipulated+'/___altdetail'+str(count)+'.jpg', 'JPEG')
		count = count + 1
	except:
		print filename

for filename in os.listdir("/Users/brendannahed/Documents/Work/Current_Classes/CIS_365/Project_3/training_images/"+car_manipulated):
	try:
		im = Image.open(os.path.join('/Users/brendannahed/Documents/Work/Current_Classes/CIS_365/Project_3/training_images/'+car_manipulated,filename))
		im_sharp = im.filter(ImageFilter.SMOOTH)
		im_sharp.save('training_images/'+car_manipulated+'/___altsmooth'+str(count)+'.jpg', 'JPEG')
		count = count + 1
	except:
		print filename
