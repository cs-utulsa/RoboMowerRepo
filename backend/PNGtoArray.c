#include <png.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>
#include <stdlib.h>
#include <stdarg.h>

static void fatal_error(const char *message, ...)
{
    va_list args;
    va_start(args, message);
    vfprintf(stderr, message, args);
    va_end(args);
    exit(EXIT_FAILURE);
}

int main()
{
    //initialize variables
    const char *png_file = "image.png";
    png_structp png_ptr;
    png_infop info_ptr;
    FILE *fp;
    png_uint_32 width;
    png_uint_32 height;
    int bit_depth;
    int color_type;
    int interlace_method;
    int compression_method;
    int filter_method;
    int j;
    png_bytepp rows;

    //open PNG file
    fp = fopen(png_file, "rb");
    if (!fp)
    {
        fatal_error("Cannot open '%s': %s\n", png_file, strerror(errno));
    }
    png_ptr = png_create_read_struct(PNG_LIBPNG_VER_STRING, NULL, NULL, NULL);
    if (!png_ptr)
    {
        fatal_error("Cannot create PNG read structure");
    }
    info_ptr = png_create_info_struct(png_ptr);
    if (!png_ptr)
    {
        fatal_error("Cannot create PNG info structure");
    }

    //initialize and read PNG
    png_init_io(png_ptr, fp);
    png_read_png(png_ptr, info_ptr, 0, 0);
    png_get_IHDR(png_ptr, info_ptr, &width, &height, &bit_depth,
                 &color_type, &interlace_method, &compression_method,
                 &filter_method);
    rows = png_get_rows(png_ptr, info_ptr);
    printf("Width is %d, height is %d\n", width, height);
    int rowbytes;
    rowbytes = png_get_rowbytes(png_ptr, info_ptr);
    printf("Row bytes = %d\n", rowbytes);

    //create the final array
    int arr[height][rowbytes];
    int i;
    for (j = 0; j < height; j++)
    {
        int i;
        png_bytep row;
        row = rows[j];
        for (i = 0; i < rowbytes; i++)
        {
            png_byte pixel;
            pixel = row[i];
            if (pixel < 128) // blacks gets uncut (0)
            {
                arr[j][i] = 0;
            }
            else if (pixel > 128) // white gets cut (1)
            {
                arr[j][i] = 1;
            }
            
        }
    }

    //prints out how the array looks like

    // for (j = 0; j < height; j++)
    // {
    //     for (i = 0; i < rowbytes; i++)
    //     {
    //         printf("%d", arr[j][i]);
    //         if (i == rowbytes-1)
    //         {
    //             printf("\n");
    //         }
    //     }
    // }


    // write array into a txt file
    remove(png_file);

    fp = fopen("ProcessedArray.txt", "w+");
    for (j = 0; j < height; j++)
    {
        for (i = 0; i < rowbytes; i++)
        {
            fprintf(fp, "%d", arr[j][i]);
        }
        fprintf(fp, "\n");
    }

    return 0;
}
