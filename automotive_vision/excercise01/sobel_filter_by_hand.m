
% define filter mask by hand
sobel_filter_kernel = int16([1 0 -1; 2 0 -2; 1 0 -1])
% rotate before aplying! convolution

% vertical edge
mirrored_sobel_u = rot90(rot90(sobel_filter_kernel))
% horizontal edge
mirrored_sobel_v = mirrored_sobel_u'

% Apply filter
loaded_img = imread(fullfile('images/0001.png'));
whos loaded_img
img = int16(loaded_img);
[height, width] = size(img); 
result_u = zeros(size(img)); % initialize black empty matrix aka image to populate
result_v = zeros(size(img));
for r=2:(height - 1) % iterate over each height pixel index
    for c=2:(width - 1) % iterate over width pixel index
        %img(r-1:r+1,c-1:c+1) is a Matrix!
        product_img_patch_with_filter = img(r-1:r+1,c-1:c+1) .* mirrored_sobel_u;
        result_u(r,c) = sum(product_img_patch_with_filter(:));
        
        product_img_patch_with_filter = img(r-1:r+1,c-1:c+1) .* mirrored_sobel_v;
        result_v(r,c) = sum(product_img_patch_with_filter(:));
    end 
end
montage([loaded_img,uint8(result_u), uint8(result_v)])

