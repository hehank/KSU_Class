function factorial_loop(num)
{
	var sum = 1;
	
	if (num == 0)
	{
		sum = 0;
		return sum;
	}
	else if (num == 1)
	{
		return sum;
	}
	else
	{
		for (let i = 1; i <= num; i++)
		{
			sum *= i;
		}
	}
	
	return sum;
}

function factorial_recursive(num, sum)
{
	if (num == 0)
	{
		return sum;
	}
	
	return factorial_recursive(num - 1, sum * num);
}
