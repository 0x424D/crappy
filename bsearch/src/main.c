# Binary search algorithm. Written without referencing any pseudocode.
# Copyright (C) 2017 0x424D (www.github.com/0x424D)

#include <stdio.h>
#include <stdlib.h>

int search(int value, int values[], int low, int high, int* pfound);

int main(int argc, char* argv[])
{
    if (argc != 2)
    {
        printf("\nUsage: ./bsearch n\n\n");
        return 1;
    }
    
    int n = atoi(argv[1]);
    int toSearch[n];
    int searchee;
    int j = 0;
    
    for (int i = 0; i < n; i++)
    {
        printf("\nsearch[%d]: ", i);
        scanf("%d", &j);
        toSearch[i] = j;
    }
    
    for (int i = 1, size = sizeof(toSearch) / sizeof(int); i < size; i++)
    {
        if (toSearch[i] < toSearch[i - 1])
        {
            printf("\nError: Array elements must be numerical order, ascending.\n\n");
            return 2;
        }
    }
    
    printf("\nNumber to search for: ");
    scanf("%d", &searchee);
    
    int found = 0;
    int* pfound = &found;
    
    
    if (search(searchee, toSearch, 0, sizeof(toSearch) / sizeof(int) - 1, pfound))
    {
        printf("\nSuccess! Found %d\n\n", searchee);
    }
    else
    {
        printf("\nFailure. Didn't find %d\n\n", searchee);
    }
}

int search(int value, int values[], int low, int high, int* pfound)
{
    if (low > high)
    {
        return 0;
    }
    
    int mid = (high + low) / 2;
    
    if (values[mid] == value)
    {
        *pfound = 1;
    }
    else if (values[mid] > value)
    {
        // search left half
        search (value, values, 0, mid - 1, pfound);
    }
    else if (values[mid] < value)
    {
        // search right half
        search(value, values, mid + 1, high, pfound);
    }
    return *pfound;
}
