%might use matrix solutions
clear all;
clc;
syms x;

% Let's first define the function;
f = @(x) a_0*x + a_1*x^2 + a_2; 
a_0 = 1.23;
a_1 = 2.46;
a_2 = 3.57;
eps_s = 0.0000001;

i_m = 50;
% Obtain the first guesses from the text file;
% input = load('YourFile.txt') ;

% Obtain first guesses
x_1 = 1;
x_2 = 3;
x_3 = (x_1 + x_2)/2;

eps_a = (x_2-x_1)/x_2;
% function we are trying to find
g = @(x) 3.^x;

% Choose the method as matrix solving, first define matrix [A] & [B]
for i = 0:1:i_m ; 
    A = [1, x_1, x_1^2; 1, x_2, x_2^2; 1, x_3, x_3^2];    
    b = [g(x_1); g(x_2); g(x_3)];
    C = inv(A)*b;
    a_0 = C(1);
    a_1 = C(2);
    a_2 = C(3);
    
    der = @(x) a_1 + a_2*x*2;

    x_n = x_3 - ((g(x_3)/der(x_3)));

    x_1 = x_2 ;
    x_2 = x_3 ;
    x_3 = x_n ; 


       fprintf('%d\t\t%.8f\t\t%.8f\t\t%.8f\t\t%.8f\n',i,x_n,x_2,x_1,eps_a);
    if abs(eps_a)<eps_s
        break;
    end                                                
end


    


%Finding the solution by matrix solving

