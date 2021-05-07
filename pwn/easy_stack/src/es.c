#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>
#include <unistd.h>
#include <inttypes.h>
char flag[256];
void giveFlag(){
    puts(flag);
}
int danger(){
    char input[256];
    char s[]="You enter the dangerous area,I think this is what you need...\n";
    write(1,s,512);
    short len;
    puts("please input the len of your voice:");
    scanf("%d",(int*)&len);
    if(len>256){
        puts("You are dangerous!");
        exit(0);
    }
    puts("please input what you want to shout out:");
    read(0,s,(uint16_t)len);
    puts("Ok,we can leave the dangerous area");
    return 0;
}
int main(){
    FILE *f=fopen("flag.txt","r");
    fscanf(f,"%s",flag);
    fclose(f);
    danger();
}