clear
clc
close all

% Importing the ODEs
f

% Read the inputs from a file
file_read = fopen('input.txt','r');
formatSpec = '%f';
input_file = fscanf(file_read,formatSpec);
equation_number = input_file(1);
corrector_step = input_file(2);
x_i = input_file(3);
x_f = input_file(4);
h = input_file(5);
initConditions = input_file(6:end);
fclose(file_read);

headerfile = fopen('output1.txt', 'w'); 
headerfile2 = fopen('output2.txt', 'w'); 

% Setting the x values
x = x_i:h:x_f;

fprintf(headerfile, "x:\t");
fprintf(headerfile2, "x:\t");
fprintf(headerfile, '%f\t', x);
fprintf(headerfile, "\n");
fprintf(headerfile2, '%f\t', x);
fprintf(headerfile2, "\n");

% Iterating through ODEs
for j=1:(equation_number)

    % Setting the initial conditions
    runge_kutta_y = [initConditions(j)];
    heun_y = [initConditions(j)];

    % 4th Order Runge-Kutta Method
    % Eqautions from slides
    for i=1:(length(x)-1)                             
        k1 = f_ode{j}(x(i),runge_kutta_y(i));
        k2 = f_ode{j}(x(i)+h/2,runge_kutta_y(i)+h/2*k1);
        k3 = f_ode{j}((x(i)+h/2),(runge_kutta_y(i)+h/2*k2));
        k4 = f_ode{j}((x(i)+h),(runge_kutta_y(i)+k3*h));
        runge_kutta_y(i+1) = runge_kutta_y(i) + (k1+2*k2+2*k3+k4)*h/6;
    end    

    fprintf(headerfile, "y"+j+":\t");
    fprintf(headerfile, '%f\t', runge_kutta_y);
    fprintf(headerfile, "\n");

    % Heun Method
    % Eqautions from slides
    for i = 1:(length(x)-1)
        
        % y_0 is set
        y_corrected = heun_y(i)+h*f_ode{j}(x(i),heun_y(i));

        % Corrector steps
        for k = 1:corrector_step
            y_corrected = heun_y(i)+(f_ode{j}(x(i),heun_y(i))+f_ode{j}(x(i+1),y_corrected))/2*h;

        end
        heun_y(i+1) = y_corrected;
        
    end

    fprintf(headerfile2, "y"+j+":\t");
    fprintf(headerfile2, '%f\t', heun_y);
    fprintf(headerfile2, "\n");
    
    % Plotting the graphs for each ODE
    figure
    plot(x,heun_y,x,runge_kutta_y)
    xlabel("x")
    ylabel("y")
    title("ODE " + j)
    legend("Heun","Runge-Kutta")
end



