#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// 1. Define the structure
struct Symbol {
    char name[20];
    char type[20];
    int addr;
} table[100];

int n = 0; // Current count of symbols

// Function to Insert
void insert() {
    printf("Enter Name, Type, and Address: ");
    scanf("%s %s %d", table[n].name, table[n].type, &table[n].addr);
    n++; // Increase count
    printf("Symbol Inserted!\n");
}

// Function to Search
void search() {
    char key[20];
    printf("Enter symbol to search: ");
    scanf("%s", key);
    
    int i;
    for(i = 0; i < n; i++) {
        if(strcmp(table[i].name, key) == 0) { // 0 means strings are equal
            printf("Found: %s is of type %s at address %d\n", table[i].name, table[i].type, table[i].addr);
            return;
        }
    }
    printf("Symbol Not Found.\n");
}

// Function to Display all
void display() {
    printf("\nName\tType\tAddress\n");
    int i;
    for(i = 0; i < n; i++) {
        printf("%s\t%s\t%d\n", table[i].name, table[i].type, table[i].addr);
    }
}

int main() {
    int choice;
    while(1) {
        printf("\n1. Insert\n2. Search\n3. Display\n4. Exit\nEnter choice: ");
        scanf("%d", &choice);
        
        switch(choice) {
            case 1: insert(); break;
            case 2: search(); break;
            case 3: display(); break;
            case 4: exit(0);
            default: printf("Wrong choice\n");
        }
    }
    return 0;
}