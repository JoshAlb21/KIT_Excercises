function match = match_point(I1, I2, p, search_size, window_size)
%MATCH_POINT Matches a point f from I1 to a point
% in image I2. The search_size as [height, width] specifies the size of the
% window to search in I2 for p. The window_size as [height, width] specifies 
% the window size for applying the comparison function. The best corresponding 
% point [u1, v1; ... uN, vN] is returned. If no point is found, zeroes(0,2) is
% returned.

if (mod(search_size(1),2) == 0 || mod(search_size(2),2) == 0)
    error('The search size must contain odd numbers');
end

all_compare_vals = zeros(search_size);
p = int16(p)
img_patch_l = extract_image_patch(I1, p, window_size);
lowest_val = 10000;
match_point = zeros(1,2);
for col = -search_size(1)/2:search_size(1)/2
    for row = -search_size(2)/2: search_size(2)/2
        search_point = int16(p+int16([col, row]));
        img_patch_r = extract_image_patch(I2, search_point, window_size);
        abs_grey_val = sum(sum(img_patch_r-img_patch_l));
        all_compare_vals(search_point(1), search_point(2)) = abs_grey_val;
        if abs_grey_val<lowest_val
            lowest_val = abs_grey_val;
            match_point = double(search_point);
        end
    end
end
match = match_point;

