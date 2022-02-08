clear
clc
close all

f  % might cause problem if there is a f.py in the same folder.

% read inputs from a file
fileID = fopen('input.txt','r');
formatSpec = '%f';
input = fscanf(fileID,formatSpec);
equations = input(1);
correctorStep = input(2);
x_i = input(3);
x_f = input(4);
h = input(5);
initConditions = zeros(1, equations);
for i=1:equations
    initConditions(i) = input(i+5);
end
fclose(fileID);
x = x_i:h:x_f;



for j=1:(length(ODEs))

    rk4y = [initConditions(1) zeros(1,length(x)-1)];
    heun = [initConditions(1) zeros(1,length(x)-1)];

    % Begins the RK4 Method
    for i=1:(length(x)-1)                              % calculation loop
        k_1 = ODEs{j}(x(i),rk4y(i));
        k_2 = ODEs{j}(x(i)+0.5*h,rk4y(i)+0.5*h*k_1);
        k_3 = ODEs{j}((x(i)+0.5*h),(rk4y(i)+0.5*h*k_2));
        k_4 = ODEs{j}((x(i)+h),(rk4y(i)+k_3*h));
        rk4y(i+1) = rk4y(i) + (1/6)*(k_1+2*k_2+2*k_3+k_4)*h;  % main equation
      
    end
    
    for i = 1:(length(x)-1)
        heunPrime = heun(i)+(h/3)*ODEs{j}(x(i),heun(i));
        heun(i+1)=heun(i)+(h/4)*(ODEs{j}(x(i),heun(i))+3*ODEs{j}(x(i)+(2*h/3), heun(i)+(2*h/3)*ODEs{j}(x(i)+h/3, heunPrime)));
    end
    
    % Compare our programs using a standart ODE integrator
    tspan = [0,100]; y0 = -0.5;
    [actx, acty] = ode45(ODEs{j}, tspan, y0);
    
    figure
    % Confirmation plot for RK4 on top of the actual plot
    plot(x,rk4y,'o-', actx, acty, '--')
    
    figure
    % Confirmation plot for Heun on top of the actual plot
    plot(x,heun,'o-', actx, acty, '--')
    
    figure
    plot(x,heun,x,rk4y,'--')
end

