function A=radixsorting(A)
r=max(A);
base=1;
while r/base>0
    A=countingSort_2(A);
    base=base*10;

end
end
 