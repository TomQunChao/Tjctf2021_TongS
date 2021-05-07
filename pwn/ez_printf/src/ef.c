#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <inttypes.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <sys/types.h>

uint64_t secret;

void danger(){
    char name[256];
    
    // puts("please input your name:");
    // scanf("%s",name);
    // puts("your name is:");
    // printf(name);

    int fd=open("/dev/urandom",O_RDONLY);
    read(fd,&secret,sizeof(secret));
    close(fd);

    // printf("\n%llx\n",secret);

    puts("please input your address:");
    scanf("%s",name);
    printf(name);
    puts("please input the secret:");
    uint64_t input_secret;
    scanf("%lld",&input_secret);
    if(secret==input_secret){
        system("cat flag.txt");
    }else{
        puts("You don\'t have secret");
    }

}

int main(){
    danger();
    return 0;
}