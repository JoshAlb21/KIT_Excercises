close all;
image_point_locations = [161, 297;  980, 350; ...
                         600,  26;  597,  87; ...
                         680, 109;  356, 121; ...
                         840, 101;  603, 262; ...
                        1046, 320; 1086,  86];

imagename = '0000.png';
I1 = imread([fullfile('images/left_img/', imagename)]);
I2 = imread([fullfile('images/right_img/', imagename)]);
search_size = [31 31]; %area where to search in right image
window_size = [11 11]; %apply comparison function on

for i = 1:size(image_point_locations,1)
    p = image_point_locations(i,:);
    matches = match_point(I1, I2, p, search_size, window_size);
    %visualize_matched_points(I1, I2, p, matches, ['Point_', int2str(i)]);
    
end

feature_points = detect_features(I1, 10)
imshow(I1)
hold on
plot(feature_points)

