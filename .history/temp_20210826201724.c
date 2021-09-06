

// #include<bits/stdc++.h>
// using namespace std;

// int row[4]={0,-1,0,1};
// int col[4]={-1,0,1,0};

// bool isValid(vector<vector<int>> vec , int i, int j, int n , int m)
// {
//     return (i>=0 && i<n && j>=0 && j<m && vec[i][j]==10);
// }

// void dfs(vector<vector<int>> arr , int x, int y, int n , int m,int *count)
// {
//     arr[x][y]=-1;

//     for(int i=0;i<4;i++)
//     {
//         if(isValid(arr,x+row[i],y+col[i],n,m))
//         {
//             (*count)++;
//             dfs(arr,x+row[i],y+col[i],n,m,count);
//         }
//     }
// }

// int main()
// {
//     int n,m;
//     cin>>n>>m;

//     vector<vector<int>> arr(n,vector<int>(m,0));

//     for(int i=0;i<n;i++)
//     {
//         for(int j=0;j<m;j++)
//         cin>>arr[i][j];
//     }

//     int maxi=INT_MIN;
//     for(int i=0;i<n;i++)
//     {
//         for(int j=0;j<m;j++)
//         {
//             if(isValid(arr,i,j,n,m))
//             {
//                 int count=0;
//                 dfs(arr,i,j,n,m,&count);
//                 cout<<count<<" ";
//                 maxi=max(maxi,count);
//             }
//         }
//     }
//     cout<<maxi;
//     return 0;

// }




#include<stdio.h>
#include<stdlib.h>

int function(void)
{
    char i;
    for(i=0;i<0xff;i++)
    {
        if(i%2==0)
        printf("%d\n",i);
    }
    return 0;
}

int main()
{
    int a=function();
    printf("%d");
    return 0;
    
}