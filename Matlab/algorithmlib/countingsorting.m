function B=countingsorting(x,app,event)
n=length(x);
r=n;
C=zeros(r,1);
for i=1:r
    C(i)=0;
end
for j=1:n
    C(x(j))=C(x(j))+1;
end
for i=2:r
    C(i)=C(i)+C(i-1);
end
B=nan(n,1);
for j=n:-1:1
    B(C(x(j))) = x(j);
    C(x(j)) = C(x(j)) - 1;
end
end

