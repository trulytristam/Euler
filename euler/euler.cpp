// euler.cpp : This file contains the 'main' function. Program execution begins and ends there.
//


#include <iostream>
using namespace std;
int main()
{
	
	int number = 0;

	while(true)
	{
		number += 20;
		bool Alltrue = true;

		for(int i=19; i> 0; i-=1)
		{
			if(number % i != 0)
			{
				Alltrue = false;
				break;
			}
		}
			
		if (number % 1000000==0)
		{
			cout<< number << endl; 
		}

		if (Alltrue)
		{
			cout<< "ANSWER: " << number<< endl;
			break;

		}
			

	}
		
}
