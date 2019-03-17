
it_is_not_variable = 123456

function res = f1_solution(x, c)
  res = log(0.5*(x+sqrt(c+x.*x)));
endfunction

function res = f1(x, yx)
  res = 1 / (2*e^yx - x);
endfunction

function res = RungeKutta_4(f, y0, a, b, step)
  res = [y0];
  len = 1;
  
  for i=a+step:step:b
    last_res = res(len);
    
    k1 = f(i-step, last_res);
    k2 = f(i-0.5*step, last_res + 0.5*step*k1);
    k3 = f(i-0.5*step, last_res + 0.5*step*k2);
    k4 = f(i, last_res + step*k3);
    
    dx = (step/6)*(k1+2*k2+2*k3+k4);
    new_res = last_res + dx;
    
    res = [res new_res];
    len += 1;
  end   
  
endfunction

function [res, h] = KuttaMersena_helper(f, x, y, h, eps)
    k1 = f(x, y);
    k2 = f(x + h/3, y + 1.5*k1);
    k3 = f(x + h/3, y + (h/6)*k1 + (h/6)*k2);
    k4 = f(x + 0.5*h, y + (h/8)*k1 + 1.5*h*k2);
    k5 = f(x + h, y + 0.5*h*k1 - 1.5*h*k3 + 2*h*k4);
    
    new_x_1 = x + 0.5*h*(k1-3*k3+4*k4);
    new_x_2 = x + (h/6) * (k1 + 4*k3 + k5);
    
    r = 0.2*abs(new_x_1-new_x_2);
    
    if (r>=eps)
      % recalculate because of low accuracy
      [res, h] = KuttaMersena_helper(@f, x, y, 0.5*h, eps);
    else
      if (r<(eps/64))
        h = h*2;
      endif
      
      res = new_x_2;
    endif
endfunction

function res = KuttaMersena(f, y0, a, b, step)
  res = [y0];
  len = 1;
  
  eps = 0.0001
  h = step
  
  for i=a+step:step:b
    last_res = res(len);
    
    [new_res, h] = KuttaMersena_helper(@f, i-step, last_res, step, eps);
    
    res = [res new_res];
    len += 1;
  end   
endfunction

function void = MyMethodsCalls()
  
C = 4*(e^2)
a = 0
b = 1
step = 0.001
x = a:step:b;

plot(x, RungeKutta_4(@f1, 1, a, b, step), x, KuttaMersena(@f1, 1, a, b, step), x, f1_solution(x, C))
legend("Runge-Kutta", "Kutta-Mersena", "Analytic solution")
title("lines overlap, solution is too accurate")

endfunction

MyMethodsCalls()

function void = BuiltInMethodsCalls()
  [x1, y1] = ode23(@f1, [0, 1], 1);
  [x2, y2] = ode45(@f1, [0, 1], 1);
  
  x = 0:0.001:1
  C = 4*(e^2)
  
  plot(x, f1_solution(x, C), x1, y1, x2, y2)
  legend("Analytic", "ode23", "ode45")
endfunction

%BuiltInMethodsCalls()