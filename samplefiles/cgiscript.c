#include <stdio.h>

int main(void) {
    // CGI scripts must output the content-type header followed by a blank line
    printf("Content-Type: text/html\r\n\r\n");

    // HTML content
    printf("<html>\n");
    printf("<head><title>Hello CGI</title></head>\n");
    printf("<body>\n");
    printf("<h1>Hello from C CGI script!</h1>\n");
    printf("</body>\n");
    printf("</html>\n");

    return 0;
}
