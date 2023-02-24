function [belements,btimes]=comp_bucket(belements,btimes,app,event)
belements=[];
btimes=[];


for i=1:10
    a = randi([1 10000],1,1000*i);
    tic
    bucketsorting(a);
    bf=toc;
      
    belements(i)=length(a);
    btimes(i)=bf;
end
