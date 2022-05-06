x=-10:0.1:10;
y = sinc(x)
plot (x,y,'-r')
hold on
plot (x,1/pi*x.^-1,'k:')
axis ([-10 10 -1.5 1.5])
legend ('sinc(x)','x,1/pi*x.^-1');
hold off