#if !defined(AUTOCOMPLETE_H)
#define AUTOCOMPLETE_H

typedef struct term{
    char term[200]; // assume terms are not longer than 200
    double weight;
} term;


int get_number(char *line);
const char* get_name(const char *line);
void read_in_terms(term **terms, int *pnterms, char *filename);
int lowest_match(struct term *terms, int nterms, char *substr);
int highest_match(struct term *terms, int nterms, char *substr);
void autocomplete(struct term **answer, int *n_answer, struct term *terms, int nterms, char *substr);

#endif