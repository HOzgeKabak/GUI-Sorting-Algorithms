function [C] = matrixsubstraction(A,B)
%A and B is matrix and C is a new matrix
n=size(A,2);
C=zeros(n); %Initial value of C matrix
    for i=1:n
        for j=1:n
            C(i,j)=0;
            for k=1:n
                C(i,j)=C(i,j)+ A(i,k)-B(k,j);
            end            
        end
    end
    
end