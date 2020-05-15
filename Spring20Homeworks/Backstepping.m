close all; clear; clc;

t_initial = 0; t_final = 5; nSample = 10; nx = 3;

init_min = -1; init_max = 1;
% randomly generate initial condition within init_min and init_max
initial_state = init_min + (init_max-init_min)*rand(nSample,nx);

set(0,'defaulttextinterpreter','latex')
% controlled phase portrait
figure(1)

tic;

for i=1:nSample
    
    % solve the ODE initial value problem
    [t,x] = ode45(@BacksteppingClosedLoop,[t_initial t_final], initial_state(i,:));
    
    % plot initial condition
    plot3(initial_state(i,1),initial_state(i,2),initial_state(i,3),'-ro')
    hold on
    % plot controlled state trajectory
    plot3(x(:,1),x(:,2),x(:,3),'-b','LineWidth',1.2)
    xlabel('$x_{1}$','FontSize',24)
    ylabel('$x_{2}$','FontSize',24)
    zlabel('$x_{3}$','FontSize',24)
    grid on
    hold on
end
plot3(0,0,0,'go','MarkerFaceColor','g') % plot origin
hold off
toc;

% plot one representative time-series
figure(2)
plot(t,x(:,1),'-o',t,x(:,2),'-o',t,x(:,3),'-o','LineWidth',1.5)
xlabel('$t$','FontSize',24)
legend('$x_{1}$', '$x_{2}$','$x_{3}$','FontSize',24,'Location','best','Interpreter','latex')
