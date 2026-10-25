// Project 2: Messy Code Improvement
// Shows a messy program and the improved, readable version of the same logic.
//
// ---------- BEFORE (messy) ----------
//   int main(){int a[5]={55,78,90,34,67};int s=0;int m=a[0];
//   for(int i=0;i<5;i++){s=s+a[i];if(a[i]>m)m=a[i];}
//   cout<<s<<" "<<s/5<<" "<<m;}
//
// Problems: no spacing, unclear names, magic number 5, integer division,
// no functions, no labels on the output.
//
// ---------- AFTER (improved, below) ----------
#include <algorithm>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;

int calculateTotal(const vector<int>& marks) {
    return accumulate(marks.begin(), marks.end(), 0);
}

double calculateAverage(const vector<int>& marks) {
    if (marks.empty()) return 0.0;
    return static_cast<double>(calculateTotal(marks)) / marks.size();
}

int findHighest(const vector<int>& marks) {
    return *max_element(marks.begin(), marks.end());
}

char gradeFor(double average) {
    if (average >= 75) return 'A';
    if (average >= 60) return 'B';
    if (average >= 40) return 'C';
    return 'F';
}

int main() {
    const vector<int> marks = {55, 78, 90, 34, 67};

    cout << "Total marks : " << calculateTotal(marks) << "\n";
    cout << "Average     : " << calculateAverage(marks) << "\n";
    cout << "Highest mark: " << findHighest(marks) << "\n";
    cout << "Grade       : " << gradeFor(calculateAverage(marks)) << "\n";
    return 0;
}
