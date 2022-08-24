read n  
count=$n
sum=0

while [ $n -ne 0 ]
do
    read t
    sum=$(($sum+$t))
    n=$(($n-1))
done

printf "%.3f" $(echo $sum/$count | bc -l)


