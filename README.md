# Image Pyramids
```
This project is trying to implement image blending by using image pyramids.
* Combining a moon background and a dog face.
```
### Image Pyramids
```
Input background image: moon.jpg
Input target image: dog.jpg
Input mask image: mask.jpg

Command line >> python Pyramid_Image_Blending.py -i moon.jpg -t dog.jpg -m mask.jpg
```

The program will show the result image as below: 

![2_1_output](https://user-images.githubusercontent.com/28382639/35773195-022b7970-0900-11e8-980d-cda0f202e59b.jpg)

The process images show as below:
![2_2_output](https://user-images.githubusercontent.com/28382639/35773202-152086ce-0900-11e8-814f-8e3ddf8f4568.jpeg)
Useful link for implementation:

- [Image Pyramids](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/tree/master/tutorials/Image_Processing/7_Image_Pyramids)
- [Image Blending](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/tree/master/tutorials/Core_Operation)

## Code
- [Image Pyramids](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/tree/master/tutorials/Image_Processing/7_Image_Pyramids)
- [Image blending using image pyramids](https://github.com/Hank-Tsou/Image-Pyramids)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Author: Hank Tsou
* Contact: hank630280888@gmail.com
* Project from California State Polytechnic University, Pomona, Computer Science, CS-519 Computer Vision



# Hough Transform - Line Detection
#### a. Generate an image showing detected lines of the pool table overlaid on the top of the original image.

>> This file include: </br>
>>* (1) Readme.md</br>
>>* (2) pool.jpg</br>
>>* (3) 1_a-1.py [ Use Hough Transform to detect lines on target edge image]</br>
>>* (4) 1_a-2.py [ Use Hough Transform to detect lines on target edge image and contour ]</br>

>>> <pre>Note: Each program can select one of the opencv function below:</br>" [1] cv2.HoughLines() " and " [2] cv2.HoughLinesP() "</br>--Therefore, there will have two output images for each program

>> #### (A) How to run the code [1_a-1.py]
>>> (a) Using the command prompt and direct to the file position. (my example)
>>> <pre> >> [C:\Users\hank\Desktop\Yueh_Lin_Tsou_lab2\1\a]

>>> (b) input >> "python 1_a-1.py" to run the code.
>>> <pre> >> [C:\Users\hank\Desktop\Yueh_Lin_Tsou_lab2\1\a>python 1_a-1.py]

>>> (c) The program will ask to slecte one of the opencv function
>>> <pre> >> [(1) cv2.HoughLines (2) cv2.HoughLinesP: ]

>>> (d) The program will show the result image

>>> ![image](https://user-images.githubusercontent.com/28382639/35773127-d6171cc4-08fd-11e8-85ec-b378d11727d3.png)

>> #### (B) How to run the code [1_a-2.py]: Same as '1_a-1.py'

>>> ![image](https://user-images.githubusercontent.com/28382639/35773134-142dff32-08fe-11e8-8581-ad74e4612a05.png)
