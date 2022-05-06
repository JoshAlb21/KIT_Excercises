% Sobel filter
%***************
gray_img = imread(fullfile('images/0001.png'));
img = int16(gray_img);

sobel_hor = fspecial('sobel');
sobel_ver = sobel_h';
filtered = imfilter(img, sobel_hor);
imshow(filtered, [])
title('Sobel in horizontal direction')

% Gradient Length
%***************
sobel_u = double(imfilter(gray_img, sobel_h));
sobel_v = double(imfilter(gray_img, sobel_v));
derivative_img=sqrt(sobel_u.^2+sobel_v.^2);
imshow((derivative_img), [])
title('Gradient Length') %edges in both directions

% Gaussian Blur
I = double(imread(fullfile('images/0001.png')));
f_2 = fspecial('gaussian',11,2);
out_2 = imfilter(I,f_2);
f_10 = fspecial('gaussian',11,10);
out_10 = imfilter(I,f_10);

montage([uint8(out_2), uint8(out_10)])
title('Gaussian Blur')
%the higher sigma is, the more blurred the image will be 

% Canny filter
I = imread(fullfile('images/2176.png'));
BW = edge(I,'canny',[0.1 0.17]);
imshow(BW)
title('Canny Edge Detection')
