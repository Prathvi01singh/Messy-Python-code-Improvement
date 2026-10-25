# Project 2: Messy Code Improvement (Python)

Shows a messy Python program and the improved version of the same logic, with the improvements explained.

## Description
The top of the file keeps the original messy snippet in comments. The code below it does the same job (total, average, highest mark, and grade for a list of marks) but is organized into small, well-named functions.

## Technologies
- C++17
- Standard library: `iostream`, `vector`, `algorithm`, `numeric`

## What Was Improved
- Clear names instead of single letters (`marks` instead of `a`, `calculateTotal` instead of `s`)
- Separate functions for total, average, highest mark, and grade
- No magic number: the size comes from the vector instead of a hard-coded 5
- Correct average using `double` instead of integer division
- Labeled output instead of bare numbers
- Consistent spacing and formatting

## Setup and Run
```
g++ -std=c++17 project2_messy_code_improvement.cpp -o improved
./improved
```

## Example Output
```
Total marks : 324
Average     : 64.8
Highest mark: 90
Grade       : B
```

## Notes
The messy snippet is an example I wrote to demonstrate the technique. If your assignment needs your own original messy script, replace the "BEFORE" comment and the code with yours.

## Author
Prathvi Singh
