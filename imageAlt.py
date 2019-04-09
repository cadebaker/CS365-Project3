from PIL import Image, ImageFilter
import os


count = 0

car_manipulated = "Traverse"


##Iterates over the directory listed
for filename in os.listdir("/Users/brendannahed/Documents/Work/Current_Classes/CIS_365/Project_3/training_images/"+car_manipulated):
	try:
		##Opens the Image
		im = Image.open(os.path.join('/Users/brendannahed/Documents/Work/Current_Classes/CIS_365/Project_3/training_images/'+car_manipulated,filename))
		##Adds a filter to the image
		im_sharp = im.filter(ImageFilter.DETAIL)
		##Saves the new image
		im_sharp.save('training_images/'+car_manipulated+'/___altdetail'+str(count)+'.jpg', 'JPEG')
		count = count + 1
	except:
		##If the file is corrupted it will throw an error
		##On corrupted files it prints the name so I can delete them.
		print filename
count = 0
##Iterates over the directory listed
for filename in os.listdir("/Users/brendannahed/Documents/Work/Current_Classes/CIS_365/Project_3/training_images/"+car_manipulated):
	try:
		##Opens the Image
		im = Image.open(os.path.join('/Users/brendannahed/Documents/Work/Current_Classes/CIS_365/Project_3/training_images/'+car_manipulated,filename))
		##Adds a filter to the image
		im_sharp = im.filter(ImageFilter.SMOOTH)
		##Saves the new image
		im_sharp.save('training_images/'+car_manipulated+'/___altsmooth'+str(count)+'.jpg', 'JPEG')
		count = count + 1
	except:
		##If the file is corrupted it will throw an error
		##On corrupted files it prints the name so I can delete them.
		print filename
