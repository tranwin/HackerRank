read b
read c

if [[ $a -eq $b && $a -eq $c ]]
then 
echo "EQUILATERAL";

elif [[ $a -ne $b && $b -ne $c && $a -ne $c ]]
then 
echo "SCALENE";

else 
echo "ISOSCELES";

fi
