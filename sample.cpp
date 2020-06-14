#include<bits/stdc++.h>
using namespace std;
int main()
{
	int n;
	cin>>n;
	long arr[n];
	for(int i=0;i<n;i++)
	{
		cin>>arr[i];
	}

	int curr=0,cost=0;
	while(curr<n-1)
	{
		int next=curr+1;
		while(next<n-1)
		{
			if(abs(arr[curr])>abs(arr[next])||abs(arr[curr])==abs(arr[next])&&arr[curr]>=0)
			{
				break;
			}
			else
				next++;
		}
		cost+=(next-curr)*arr[curr]+(next*next-curr*curr)*arr[curr]*arr[curr];
		curr=next;
	}
	cout<<cost;
	return 0;
}
