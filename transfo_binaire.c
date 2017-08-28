//essai du code c sous gcc et linux
#include <stdio.h>
#include<stdlib.h>
 
int main()
{int i ;
	char buffer[100];
	while(fgets(buffer,100,stdin)){
		i=atoi(buffer);
		fwrite(&i,sizeof(int),1,stdout);
	}
	
 return 0;
 }
