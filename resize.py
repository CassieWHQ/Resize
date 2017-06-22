import cv2
import os
#for n in range(1,17,1):
    
 #   image = cv2.imread('./in/raw{}/image{}.png'.format(n))
  #  tst = cv2.resize(image,(128,128))
   # cv2.imwrite('./out/{}/image{}.png'.format(n,n),tst)
root_dir = 'in/'
n = 0
print os.listdir(root_dir)
for filename in os.listdir(root_dir):
    n+=1
    image = os.path.join(root_dir, filename)
    image = cv2.imread(image)
    # tst2 = cv2.resize(image, (24, 24))
    tst3 = cv2.resize(image, (450, 450))
    cv2.imwrite('out-test/tr_{}.jpg'.format(n), tst3)

# for cv2.imwrite('out-test/{}/image{}.png'.format(n,j), tst2)
#     label in os.listdir(root_dir):
#     # label_dir = os.path.join(root_dir, label)
#     # print label_dir
#     # n += 1
#     # j = 0
#     # print os.listdir(label_dir)
#     for filename in os.listdir(label_dir):
#         j += 1
#         image = os.path.join(label_dir, filename)
#         image = cv2.imread(image)
#         tst2 = cv2.resize(image, (128, 128))
#