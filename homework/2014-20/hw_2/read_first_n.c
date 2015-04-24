#include <stdio.h>
#include <stdlib.h>
#define USAGE "./read.x nbases"

int main(int argc, char **argv){
  int n_read;
  FILE *in;
  char *s;
  int i;

  /*checks the number of arguments*/
  if(argc!=2){
    printf("USAGE %s\n", USAGE);
    exit(1);
  }

  /*converts to an integer the first argument*/
  n_read = atoi(argv[1]);

  /*opens the file*/
  if(!(in=fopen("Vibrio_cholerae.txt", "r"))){
    printf("problem opening the file\n");
    exit(1);
  }
  
  /*memory allocation for the number of characters I need*/
  s = malloc((n_read) * sizeof(char));

  /*reads the first N characters*/
  i=0;
  do{
    s[i] = fgetc(in);
    i++;
  }while(i<n_read);
  
  /*prints them to screen to test*/
  for(i=0;i<n_read;i++){
    printf("%c", s[i]);
  }
  printf("\n");

  /*prints their ascii code*/
  for(i=0;i<n_read;i++){
    printf("[%d]", s[i]);
  }
  printf("\n");

  return 0;
}
