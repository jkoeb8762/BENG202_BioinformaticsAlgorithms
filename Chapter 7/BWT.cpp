#include <string>
#include <vector>
#include <algorithm>
#include "BWT.h"
using namespace std;

string bwt(const string & s) {
    vector<string> working;
    string ans;
    for (unsigned int i = 0; i < s.length(); i++){
        working.push_back(s.substr(i) + s.substr(0, i));
    }
    sort(working.begin(), working.end());
    for (unsigned int i = 0; i < s.length(); i++){
        ans.append(working[i].substr(s.length()-1));
    }
    return ans;
}
