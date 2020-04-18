clear; clc; close all;

% Starter code for proving stability of switched linear system 
% under *arbitrary* switching, using Lyapunov function methods

%% Continuous-time 2x2 system with 2 modes
% =========================================================================
set(0,'defaulttextinterpreter','latex')
% two Hurwitz matrices
A1 = [-1, 0.25; -1 -1]; A2 = [-0.5, -2; 0.4, -0.5];
eig(A1) 
eig(A2)

% individual modal linear dynamics
f1 = @(t,x) A1*x; f2 = @(t,x) A2*x;

x = linspace(-4,4,20); y = linspace(-4,4,20); 
[x11,x12] = meshgrid(x,y); [x21,x22] = meshgrid(x,y);

u1 = zeros(size(x11)); v1 = zeros(size(x12)); u2 = u1; v2 = v1;

t=0;
for i = 1:numel(x11)
    x1dot = f1(t,[x11(i); x12(i)]);
    x2dot = f2(t,[x21(i); x22(i)]);
    u1(i) = x1dot(1); v1(i) = x1dot(2);
    u2(i) = x2dot(1); v2(i) = x2dot(2);
end

% Plot individual vector fields
figure(1)
subplot(2,2,1)
quiver(x11,x12,u1,v1)
figure(gcf); xlabel('$x_1$','FontSize',24); ylabel('$x_2$','FontSize',24); 
axis tight;
set(gca,'FontSize',14); 
title('$\dot{x} = A_{1}x$','FontSize',24);
subplot(2,2,2)
quiver(x21,x22,u2,v2)
figure(gcf); 
xlabel('$x_1$','FontSize',24); ylabel('$x_2$','FontSize',24); 
axis tight;
set(gca,'FontSize',14); 
title('$\dot{x} = A_{2}x$','FontSize',24);
hold on

%% Find Individual Lyapunov Functions

% For modal dynamics 1
cvx_begin sdp
variable P1(2,2) symmetric;
A1'*P1+P1*A1 <= -eye(2);
P1 >= eye(2);
cvx_end
cvx_status
cvx_optval;
% Lyapunov function for dynamics 1
syms xx; syms yy; V1 = @(xx,yy) [xx; yy]'*P1*[xx; yy];
subplot(2,2,3)
ezsurfc(V1, [-4, 4, -4, 4])
xlabel('$x_1$','FontSize',24); ylabel('$x_2$','FontSize',24); 
title('$V_1(x_1,x_2)$','FontSize',24);
set(gca,'FontSize',14)

% For modal dynamics 2
cvx_begin sdp
variable P2(2,2) symmetric;
A2'*P2+P2*A2 <= -eye(2);
P2 >= eye(2);
cvx_end
cvx_status
cvx_optval;
% Lyapunov function for dynamics 2
syms xx; syms yy; V2 = @(xx,yy) [xx; yy]'*P2*[xx; yy];
subplot(2,2,4)
ezsurfc(V2, [-4, 4, -4, 4])
xlabel('$x_1$','FontSize',24); ylabel('$x_2$','FontSize',24); 
title('$V_2(x_1,x_2)$','FontSize',24);
set(gca,'FontSize',14)


%% Find Common Quadratic Lyapunov Function (CQLF), if possible
% for the switched linear system
cvx_begin sdp
% fill in your code here
cvx_end
cvx_status
cvx_optval;
% Plot CQLF (uncomment the following after you filled in the code above) 
% syms xx; syms yy; V = @(xx,yy) [xx; yy]'*P*[xx; yy];
% figure(2)
% ezsurfc(V, [-4, 4, -4, 4])
% xlabel('$x_1$','FontSize',24); ylabel('$x_2$','FontSize',24); 
% title('CQLF $V(x_1,x_2)$','FontSize',24);
% set(gca,'FontSize',14)