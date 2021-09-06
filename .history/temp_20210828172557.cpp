#include<bits/stdc++.h>
using namespace std;


int solve()
{

}

itn main()
{
    int n;
    cin>>n;

    int t;
    cin>>t;

    vector<vector<int>> task(n,vector<int>(2));

    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            cin>>task[i][j];
        }
    }

    int dp[n+1][t+1];

    for(int i=0;i<=n;i++)
    {
        for(int j=0;j<=t;j++)
        {   
            if(i==0 || j==0)
            {
                dp[i][j]=0;
            }
            // task[i][0]->location, value array
            // task[i][1]->time taken, weight array
            else if(task[i][0])

        }
    }


}