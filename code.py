import cv2
img=cv2.imread("PRO-104-Project-Image-main/solar-system.jpg")
text1="sun"
text2="mercury"
text3="venus"
text4="earth"
text5="mars"
text6="jupiter"
text7="saturn"
text8="uranus"
text9="neptune"
cv2.putText(img,text1,(20,225),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=0.75,color=(255,255,255))
cv2.putText(img,text2,(100,225),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,text3,(200,225),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,text4,(300,225),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,text5,(400,225),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,text6,(600,225),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,text7,(800,225),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,text8,(1000,225),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,text9,(1200,225),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=0.5,color=(255,255,255))
cv2.imshow("frame",img)
cv2.waitKey(0)

