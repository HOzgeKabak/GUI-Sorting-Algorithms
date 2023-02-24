function [c,Array] = partition(Array,p,q,app,~)
    x=Array(p);
   
    i=p;
     b = bar(app.UIAxes,Array,'FaceColor','flat');
            b.CData(p,:) = [0 0 1];
            drawnow update
    for j=p+1:q
     
        if Array(j)<=x
            
            i=i+1;
            key=Array(i);
            Array(i)=Array(j);
            Array(j)=key;
            bar(app.UIAxes, Array)
            b = bar(app.UIAxes,Array,'FaceColor','flat');
            b.CData(j,:) = [1 0 0];
            drawnow update
            pause(app.projectSpeed)
        end
        
    end
    
    key=Array(p);
    Array(p)=Array(i);
    Array(i)=key ;
    c=i;
    b = bar(app.UIAxes,app.randomArray,'FaceColor','flat');
    b.CData(j-1,:) = [0 0 1];
end
