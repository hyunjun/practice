#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Foo
{
    size_t size;
    int data[]; // FLA == data[0] == data[1]
};
typedef struct Foo Foo_t;

int main(int argc, char** argv)
{
    const size_t SIZE = 100;
    int i;

    fprintf(stdout, "sizeof(Foo->size) = %lu\n", sizeof(size_t));
    fprintf(stdout, "sizeof(Foo) = %lu\n", sizeof(Foo_t));

    Foo_t *p = (Foo_t*) malloc(sizeof(Foo_t) + sizeof(int) * (SIZE - 1)); // variable size == SIZE - 1 <-- why is this possible?
    //Foo_t *p = (Foo_t*) malloc(sizeof(Foo_t) + sizeof(int) * (SIZE)); // variable size == SIZE
    p->size = SIZE;
    for (i = 0; i < p->size; ++i) {
        p->data[i] = i;
    }
    for (i = 0; i < p->size; i++) {
        fprintf(stdout, "%d ", p->data[i]);
    }
    fprintf(stdout, "\n");

    long address = (long)&(p->data[0]);
    printf("address : %ld\n", address);

    for( int i=0; i<10; i++)
    {//print p->data[0] ~ p->data[9]
        printf("value : %d\n", *( (int*)address + i ));
    }

    for( int i=0; i<10; i++)
    {//print p->data[20] ~ p->data[29]
        printf("value : %d\n", *( (int*)address + 20 + i ));
    }

    free(p);

    return 0;
}
