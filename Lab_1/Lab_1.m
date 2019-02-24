
C = -3

function res = analytic_solution(x,c)
  res = c*cos(x) + 2
endfunction
  
function [ans]=f(x, yx)
  % yx = y(x)
  ans = (2.-yx) * tan(x)
endfunction

function yx=euler(a, b, y0, step)
  % initilize array of integral curve points with y0
  yx = [y0]
  yx_length = 1 % remember the length of array
  
  for i = a+step:step:b
    last_yx = yx(yx_length) % get the last element to calculate new
    
    % calculate new y point of integral curve using Euler's method
    new_yx = last_yx + step * f(i-step, last_yx)
    
    % add new point to array and increment the length 
    yx = [yx new_yx]
    yx_length+=1
  end
endfunction

function yx=euler_modified(a, b, y0, step) 
  % calculate h/2 just one time. instead of doing it in the loop
  half_step = step/2
  
  % initilize array of calculated integral curve points. and the length of this array
  yx = [y0]
  yx_length = 1
  
  for i = a+step:step:b
    last_yx = yx(yx_length)
    
    % pre-calculate x and y(x) to use Modified Euler's method
    yx_p = last_yx + half_step * f(i-step, last_yx)
    x_p = (i-step) + half_step
    
    % calculate new point of integral curve
    new_yx = last_yx + step * f(x_p, yx_p)
    
    yx = [yx new_yx]
    yx_length+=1
  end
endfunction

function yx=Hoin(a, b, y0, step) 
  % calculate h/2 just one time. instead of doing it in the loop
  half_step = step/2
  
  % initilize array of calculated integral curve points. and the length of this array
  yx = [y0]
  yx_length = 1
  
  for i = a:step:b-step
    last_yx = yx(yx_length)
   
    % calculate new point of integral curve using Hoin's method
    new_yx = last_yx + half_step * (
        f(i, last_yx) + f(i+step, last_yx + step * f(i, last_yx))
      )
    
    yx = [yx new_yx]
    yx_length+=1
  end
endfunction

a = 0
b = 1
step = 0.1
n = round((b-a)/step)
x = a:step:b

%plot(x, euler(a,b,-1,step), x, analytic_solution(x,C))
%title("Euler's method. h = 0.04")

%mx = a:0.01:b
%plot(x, euler_modified(a,b,-1,step), mx, analytic_solution(mx,C))
%title("Modified Euler's method. h = 0.1")

mx = a:0.01:b
plot(x, Hoin(a, b, -1, step), mx, analytic_solution(mx,C))
title("Hoin's method. h = 0.1")