function features = detect_features(I, number)
%DETECT_FEATURES This function computes image features given the specified
%method. The list of features is returned as [u1 v1; u2 v2; ...; uN vN]
    
points = detectHarrisFeatures(I);
[all_features,valid_points] = extractFeatures(I,points);

strongest = selectStrongest(valid_points,number);
features = strongest.Location;

end

