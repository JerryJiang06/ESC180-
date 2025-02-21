#include "autocomplete.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>



int get_number(char *line){
    return atoi(line);
}



char* get_name(const char *line){
    while (*line == ' ' || *line == '\t' || (*line >= '0' && *line <= '9')) 
    {
        line++;
    }
    char *res = malloc(200 * sizeof(char));
    int i = 0;
    while (*line != '\n' && *line != '\0' && i < 199) 
    {
        res[i++] = *line++;
    }
    res[i] = '\0';
    return res;
}



void read_in_terms(term **terms, int *pnterms, char *filename)
/* The function takes in a pointer to a pointer to term, a pointer to an int, and the name of a file that
is formatted like cities.txt.
The function allocates memory for all the terms in the file and stores a pointer to the block in *terms.
The function stores the number of terms in *pnterms. The function reads in all the terms from filename,
and places them in the block pointed to by *terms.
The terms should be sorted in lexicographic order. */
{
    char line[200];
    FILE *fp = fopen(filename, "r");

    fgets(line, sizeof(line), fp);
    *pnterms = atoi(line);
    *terms = malloc(sizeof(term)*(*pnterms));

    // int i;
    // fgets(line, sizeof(line), fp);
    // const char *name = get_name(line);
    // strcpy((*terms)[0].term, name);
    // (*terms)[0].weight = get_number(line);

    int i = 0;
    while (fgets(line, sizeof(line), fp)) {
        char *name = get_name(line);
        strncpy((*terms)[i].term, name, 199);
        (*terms)[i].term[199] = '\0'; 
        (*terms)[i].weight = get_number(line);
        free(name);  // Free allocated memory, this might be the issue
        i++;
    }

    fclose(fp);

    // Sorting terms 
    for (int x = 0; x < *pnterms - 1; x++) {
        for (int y = x + 1; y < *pnterms; y++) {
            if (strcmp((*terms)[x].term, (*terms)[y].term) > 0) {
                term temp = (*terms)[x];
                (*terms)[x] = (*terms)[y];
                (*terms)[y] = temp;
            }
        }
    }

    // while (fgets(line, sizeof(line), fp))
    // {
    //     i = 0;
    //     name = get_name(line);

    //     while (i < *pnterms && strcmp((*terms)[i].term, name) < 0) // might be > tbh
    //     {

    //         i++;
    //     }

    //     memmove(&((*terms)[i + 1]), &((*terms)[i]), sizeof(term) * (*pnterms - i - 1));

    //     strcpy((*terms)[i].term, name);  // Copy name into term struct array
    //     free((void *)name);  // Free allocated memory after copying

    //     (*terms)[i].weight = get_number(line);
    // }
}



int starts_with(char *string, char * substring)
// returns 0 if string does not start with substring and 1 otherwise
{
    int len = strlen(substring);
    for (int i = 0; i < len; i++)
    {
        if (string[i] != substring[i])
        {
            return 0;
        }
    }
    return 1;
}

int lowest_match(term *terms, int nterms, char *substr)
/* The function returns the index in terms of the first term in lexicographic ordering that matches the
string substr.
This function must run in O(log(nterms)) time, where nterms is the number of terms in terms.
You can assume that terms is sorted in ascending lexicographic order. Hashtag yolo.*/
{
    int left = 0, right = nterms - 1;
    int result = -1;  // Store the first found match index

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (starts_with(terms[mid].term, substr)) {
            result = mid;  // Store potential lowest match
            right = mid - 1;  // Search left for an earlier match
        } else if (strcmp(terms[mid].term, substr) < 0) {
            left = mid + 1;  // Move right
        } else {
            right = mid - 1;  // Move left
        }
    }
    return result;
}



int highest_match(term *terms, int nterms, char *substr)
/* The function returns the index in terms of the last term in lexicographic order that matches the string
substr.
This function must run in O(log(nterms)) time, where nterms is the number of terms in terms.
You can assume that terms is sorted in increasing lexicographic order.*/
{
    int left = 0, right = nterms - 1;
    int result = -1;  // Store the last found match index

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (starts_with(terms[mid].term, substr)) {
            result = mid;  // Store potential highest match
            left = mid + 1;  // Search right for a later match
        } else if (strcmp(terms[mid].term, substr) < 0) {
            left = mid + 1;  // Move right
        } else {
            right = mid - 1;  // Move left
        }
    }
    return result;  // Return last match found or -1 if not found
}

int compare_by_weight(const void *a, const void *b)
{
    double result = ((const term *)a)->weight - ((const term *)b)->weight;
    if (result < 0)
    {
        return -1;
    }
    if (result > 0)
    {
        return 1;
    }
    return 0;
}

void autocomplete(term **answer, int *n_answer, term *terms, int nterms, char *substr)
{
    int lowest_index = lowest_match(terms, nterms, substr);
    int highest_index = highest_match(terms, nterms, substr);
    *n_answer = highest_index - lowest_index + 1;
    int size = sizeof(*n_answer) / sizeof(term);
    memmove(*answer, &(terms[lowest_index]), *n_answer*sizeof(term));
    qsort(*answer, size, sizeof(term), compare_by_weight);
}
