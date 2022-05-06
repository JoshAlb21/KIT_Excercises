matrix = [1 2 3; 4 5 6]
vector = [1 2 3]
transpose_vector = [-2 1 -4]'

%get element
matrix(2,3)
%get complete row
matrix(2,:)
%get complete column
matrix(:,2)
%convert matrix to vector
matrix(:)
%check type
whos matrix

%FUNCTIONS
ZeroMatrix = zeros(2,3)
length(ZeroMatrix)
size(ZeroMatrix)

%SEQUENCE

%generate sequence/vector
[1:2:10]
100:-1:1 %counting backwards
% apply method on all entries
format short e %% format the output to be more readable
10.^[-3:5] % Point means element-wise
format default

%PLOTTING
x=-10:0.1:10;
y = sinc(x)
%plot (x,y,'-r')
hold on
%plot (x,1/pi*x.^-1,'k:')
axis ([-10 10 -1.5 1.5])
%legend ('sinc(x)','x,1/pi*x.^-1');
hold off

% LOOPS
s=0
for i=1:length(x)
    s=s+x(i)*x(i);
end

%Use of functions
eucl_dist([1, 2], [3, 4])
%own file or by the end of life script
%Use script
%plot_script


% IMAGES
g = imread (fullfile('images/0001.png'));
imshow(g);
size(g);
max(max(g))
% adjust range
imshow(I, [20, 40]);
% adjust range autom. with min and max
imshow(I, []);

rgb = imread (fullfile('images/0002.png'));
gray = rgb2gray(rgb);
imshow(gray);
% Show multiple pictures in 1 window
montage({g,gray})
