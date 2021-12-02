#include <stdio.h>
#include <limits.h>
 
 int main() {
     
    FILE* datoteka = fopen("input.txt", "r");
    char c = 's';
    int prejsnjeStevilo = INT_MIN;
    int stevec = 0;

    while(c != EOF) {
        c = fgetc(datoteka);
        int stevilo = 0;
        while(c != '\n') {
            stevilo += 10*stevilo + (c - '0');
            c = fgetc(datoteka);
        }
        if(stevilo > prejsnjeStevilo) {
            stevec++;
        }
        prejsnjeStevilo = stevilo;
    }

    printf("%d\n", stevec);

    fclose(datoteka);


    return 0;
 }