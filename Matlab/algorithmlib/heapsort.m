function x=heapsort(x,app,~)
 pause('on')
Y=x;
bar(app.UIAxes,Y);
                     
    for i=1:1:length(x)
        text(app.UIAxes, i:i, Y(i)', num2str(Y(i)','%0.2f'),'HorizontalAlignment','center','VerticalAlignment','bottom')
                            
    end
    function x = siftDown(x,root,theEnd)
        while (root * 2) <= theEnd

            child = root * 2;
            if (child + 1 <= theEnd) && (x(child) < x(child+1))
                child = child + 1;
            end

            if x(root) < x(child)
                x([root child]) = x([child root]); %Swap
                root = child;
            else
                return
            end

        end %while
    end %siftDown

    count = numel(x);

    %Because heapify is called once in pseudo-code, it is inline here
    start = floor(count/2);

    while start >= 1
        x = siftDown(x, start, count);
        start = start - 1;
    end
    %End Heapify

    while count > 1
        if app.isWorking == 1
            pause(app.projectSpeed)
        x([count 1]) = x([1 count]); %Swap
        count = count - 1;
        x = siftDown(x,1,count);
         bar(app.UIAxes, x)
         Y=x;
        bar(app.UIAxes,Y);
                     
            for i=1:1:length(x)
                text(app.UIAxes, i:i, Y(i)', num2str(Y(i)','%0.2f'),'HorizontalAlignment','center','VerticalAlignment','bottom')

            end
            
            drawnow update
        else
             app.randomArray = x;
             Y=x;
            bar(app.UIAxes,Y);

                for i=1:1:length(x)
                    text(app.UIAxes, i:i, Y(i)', num2str(Y(i)','%0.2f'),'HorizontalAlignment','center','VerticalAlignment','bottom')

                end
            break
        end
    end

end