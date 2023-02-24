
function x = MergeSort_app(x,low,high,app,event)

n = length(x);
if app.isWorking==1
    if n == 1

        app.randomArray = x;
    else
        if app.isWorking==1
            q= floor((low+high)/2);
        else
            app.randomArray=x;
        end
        if app.isWorking==1
        x = MergeSort_app( x,low,q,app,event);    
        x = MergeSort_app( x,q+1,high,app,event);
        else 
            app.randomArray=x;
        end
        if app.isWorking==1
            x = Merge_app( x,low,q,high,app,event); 
        else 
            app.randomArray=x;
        end
        bar(app.UIAxes, x)
       drawnow update
    end
else 
    app.randomArray=x;
    bar(app.UIAxes, array)
       drawnow update
end
end
function M = Merge_app(M,length(L),middle,Rlen,app,event)
pause("on")

RLen = length(R);  
LLen = length(L);  
r = RLen+LLen;
M= zeros(1,r); 


j = 1;
i= 1;
for k = 1:r
 if app.isWorking==1
     pause(app.projectSpeed)
  if j > RLen
   
    M(k) = L(i); 
     i = i + 1;
     bar(app.UIAxes, x)
     drawnow update
  elseif i > LLen
    
    M(k) = R(j); 
    j = j + 1;
    bar(app.UIAxes,x)
    drawnow update
  elseif R(j) <= L(i)
    
     M(k) = R(j); 
     j = j + 1;
     bar(app.UIAxes,x)
     drawnow update
  else
    
    M(k) = L(i); 
    i = i + 1;
    bar(app.UIAxes,x)
    drawnow update
  end
 else
     app.randomArray = x;
     break
end
end
end

