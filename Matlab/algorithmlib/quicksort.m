function Array=quicksort(Array,p,r,app,event)
if p<r
    if app.isWorking == 1
    [q,Array]=partition(Array,p,r,app,event);
    Array=quicksort(Array,p,q-1,app,event);
    Array=quicksort(Array,q+1,r,app,event);
    else
        return
    end
end
end

