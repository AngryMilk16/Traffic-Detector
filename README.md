This is a simple program that detects vehicles as they drive down the highway. 

It does this by first opening the video (.mp4) and removing the still background with Opencv. It then detects the movement of the pixels and if there are more than 800 pixels in one area (that are moving together), it will highlight them and put a box around the object. 

This code is not overly complex and that makes it so there can be some errors within it (ie. detecting multiple cars in one car and other similar problems)

Feel free to make your own copy and mess around with it with your own videos too!
