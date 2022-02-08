% Importing data
data = importdata("input.txt");
% Seperating the x and y from input file.
x = data(:,1); 
y = data(:,2);

% Obtaining n value from the lenght of x array.
n=length(x)-1;

% Most of the values in A and b matrixes are 0.
% It is safe to initially define these matrixes as 0 matrixes.
A=zeros(4*n,4*n);
b=zeros(4*n,1);

k=2; % k is a counter. 

% Equations of every 4 row are similar. Only values differ.
% This for loop iterates through the line of A and b.
for i=1:4:4*n
    % h is calculated at each iteration.
    h = x(k) - x(k-1);

    % This for loop iterates through the columns of A and rows of b.
    % In this loop, corresponding values in every row and column is
    % assigned.
    for j=1:1:4
        % i instead of j is used intentionally, indexing with j was more complex.
        A(i,i) = 1;
        b(i) = y(k-1);

        A(i+1,i) = 1; 
        A(i+1,i+1) = h;
        A(i+1,i+2) = h*h;
        A(i+1,i+3) = h*h*h;
        b(i+1) = y(k);

        A(i+2,i+1) = 1;
        A(i+2,i+2) = 2*h;
        A(i+2,i+3) = 3*h*h;


        A(i+3,i+2) = 2;
        A(i+3,i+3) = 6*h;

        if i<4*n-4 % values in the last two row is different from the others.
            A(i+2,i+5) = -1;
            A(i+3,i+6) = -2;
        end
    end
    k = k+1; % counting k
end

A = inv(A); % inverse of A
C = A*b; % Finding C with multiplying A and b

% Shape of C was 20x1 matrix. It transformed into nx4 matrix by the following lines. 
C = reshape(C, [4,n]); 
C = transpose(C)

%--------------------------------------------------------------------%
 
% Corresponding y values can be found by putting the 
% x values in the interval (x(1),x(end))
% to S function given in the problem. 

% More x values are obtained from the following for loop.
j = 1;
for i=x(1):0.05:x(end)
    x_plot(j) = i;
    j = j+1;
end


j = 1;
k = 1;
for i = x_plot
    % Below line is the S function given in the project.
    y_plot(j) = C(k,1) + C(k,2)*(i - x(k)) + C(k,3)*(i - x(k)).^2 + C(k,4)*(i - x(k)).^3;
    j = j+1;
    if i == x(k+1) % k values are incremented when i is equal to the next x value given in the input file.
    k = k+1;
    end
end


% Plotting
figure
plot(x_plot, y_plot,'LineWidth', 3, 'Color', 'r');
title('x vs y');
xlabel('x');
ylabel('y');
