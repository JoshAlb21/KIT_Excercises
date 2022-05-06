function [ d ] = eucl_dist ( x, y )
% calculate the Euclidean distance of two vectors x, y

d = sqrt(sum((x-y).^2));