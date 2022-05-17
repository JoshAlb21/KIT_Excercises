function matches = feature_matching(I1, I2, search_size, window_size)

left_points = int16(detect_features(I1, 10));

matching_results = ones(1,4);
for i= 1:length(left_points)
    
    matches = int16(match_point(I1, I2, left_points(i,:), search_size, window_size));
    new_match = cat(2, left_points(i,:), matches);
    matching_results = [matching_results new_match];
end

matches = int16(matching_results);

