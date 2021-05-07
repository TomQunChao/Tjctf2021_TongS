

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <memory.h>
#include <string.h>

void main(){
    char *a=malloc(0x10);
    char *b=malloc(0x10);
    char *c=malloc(0x10);
    char *target=malloc(0x10);
    FILE *f=fopen("flag.txt","r");
    fread(target,16,1,f);
    fclose(f);
    malloc(0x80);
    free(c);
    free(b);
    char payload[0x30];
    // puts("please input the payload:");
    read(0,payload,0x22);
    // char payload[0x30]="AAAAAAAAAAAAAAAAAAAAAAAA\x21\x00\x00\x00\x00\x00\x00\x00\x60";
    memcpy(a,payload,0x21);
    // read(a,payload,0x21);
    
    char *d=malloc(0x10);
    char *e=malloc(0x10);
    write(1,e,0x10);

}