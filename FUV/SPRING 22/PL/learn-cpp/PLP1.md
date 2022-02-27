FUV Spring 22 - CS308 - Programming Languages
Student: Tran Ngoc Anh - ID: 200154
Instructor: Nanette Simenas 
---- 

# PLP1: History and Hello World
C++ is a general purpose programming language created by Bjarne Stroustrup.

## History ## 
C++ was created by Bjarne Stroustrup in the 1980s with a motivation to add object-oriented programming into the C language. 

C++ is widely used for large software structures and seen in a variety of industries. For example, C++ is used for back-end services of popular web browsers such as  Google Chrome, Mozilla Firefox, Safari, and Opera to retrieve database information and render code to interactive webpages. C++ also helps Google search engine render quick search result. 

To learn C++, I will use following resources: 

C++ documentation: https://www.cplusplus.com/doc/tutorial/ 
FreeCodeCamp Youtube tutorial: https://www.youtube.com/watch?v=8jLOx1hD3_o 
Learn Cpp: https://www.learncpp.com/ 
 

## Getting Started ## 

### Installation ###

According to my learning materials, Visual Studio Code supports C++ for both Windows, Linux and MacOS. I installed C/C++ Extension on VSCode. 

For me, I use MacOS with already install compiler for C++.  

### Run a C++ file ###

**Compile with Terminal:** Type `g++` followed by the `.cpp` file name in the terminal and press Enter. 

**Execute file:** type `./` followed by the file name. 

### Write comments ###

**Single-line comment:** Single-line comments are created using two consecutive forward slashes `\\`.

**Multiple-line comment:** Multi-line comments are created using `/*` to begin the comment, and `*/` to end the comment.

### Run Hello World ###

1. Create a source file hello.cpp in text editor:

```
#include <iostream>

using namespace std;

int main()
{
    std::cout << "Hello World" << std::endl;
}
```
2. Open Terminal window, run `clang++` or `g++` + `hello.cpp` to compile
3. Type `./a.out` to run the program.

## References ##
[1] History of C++ - C++ Information. (n.d.). Retrieved from https://www.cplusplus.com/info/history/ 
[2] Xiao, L. (2021, October 28). What is C++ used for? Retrieved from https://www.codecademy.com/resources/blog/what-is-c-plus-plus-used-for/ 
[3] https://www.codecademy.com/learn/learn-c-plus-plus/modules/learn-cpp-hello-world/cheatsheet 