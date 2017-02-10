#include "estring.h"
#include "stdio.h"

int main(int argc, const char * argv[]) {
    estring str("您好");
    printf("%s", str.to_utf8().c_str());
    return 0;
}
