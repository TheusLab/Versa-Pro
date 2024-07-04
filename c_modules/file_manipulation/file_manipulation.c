// c_modules/file_manipulation/file_manipulation.c
#include "file_manipulation.h"

void save_file(const char *filename, const char *data) {
    FILE *file = fopen(filename, "w");
    if (file) {
        fwrite(data, 1, strlen(data), file);
        fclose(file);
    }
}
