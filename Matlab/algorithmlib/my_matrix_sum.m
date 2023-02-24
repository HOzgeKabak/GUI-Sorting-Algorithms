function [C] = my_matrix_sum(A,B,app,event)
[m n]=size(A)
[k l]=size(B)
C=zeros(m,l);
for i=1:m;
    for j=1:l;
        for p=1:n;
            C(i,j)=C(i,j)+ A(i,p)+B(p,j);
        end            
    end
end
end