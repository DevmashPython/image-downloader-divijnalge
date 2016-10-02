import re
import urllib
i=0
count=0
print"enter any url"
url=raw_input()
fp = urllib.urlopen(url)
data = fp.read()
matches = re.findall(r'(https?:/)?(/?[\w_\-&%?./]*?)\.(jpg|png|gif|jpeg)',data, re.M)
print 'Enter name of the image file that you want to create\n'
a=raw_input()
print "There a total of %d images"%len(matches)
while i<len(matches):
	b=list(matches[i])
	b.insert(2,'.')
	c=''.join(b)
	try:
		if b[3]=="jpg":
			urllib.urlretrieve(c,a+".jpg")
		if b[3]=="jpeg":
			urllib.urlretrieve(c,a+".jpg")
		if b[3]=="png":
			urllib.urlretrieve(c,a+".png")
		if b[3]=="gif":
			urllib,urlretrieve(c,a+".gif")

	except:
		count=count+1
		print "  ",
	a=a+" "
	i=i+1
if count!=0:
	n=i-count
	print "\nDue to some reason only %d got images downloaded "%n
if count==0:
	print "\nThe images have been downloaded"
