close all;
imagename = '0000.png';
I1 = imread(['images/left_img/' imagename]);
I2 = imread(['images/right_img/' imagename]);
search_size = [31 31];   %%% set reasonable values here
window_size = [11 11];   %%% set reasonable values here

matches = feature_matching(I1, I2, search_size, window_size);
visualize_feature_matching(I1, I2, double(matches), imagename);
disp(matches)
plot_patches(I1, I2, double(matches), window_size);
