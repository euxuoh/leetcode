#include<iostream>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;

//创建子串数组
void makeStrVector(const string &str, vector<string> &v)
{
    int len = str.length();
    for (int i = 0; i < len; i++)
    {
        string substr = str.substr(i, len - i);
        v.push_back(substr);
    }
}

//比较两子串，返回从头开始连续相同字符个数
int strcmp_eqlen(const string &str1, const string &str2)
{
    int len = 0;
    while (str1[len] == str2[len])
    {
        len++;
    }
    return len;
}

int main()
{
    vector<string> v_str;
    string str;
    //cin >> str;   //此法输入字符串遇到空格就结束了
    getline(cin, str);  //可接受空格，遇到\n换行符结束
    makeStrVector(str, v_str);
    //对子串进行排序
    sort(v_str.begin(), v_str.end());
    //遍历数组比较前后两个子串相同字符个数
    int max_len = 0, index = 0;
    int length = v_str.size();
    for (int i = 0; i < length-1; i++)
    {
        //可优化的地方，进去寻找最长子串前，可以跳过比当前max_len更短的子串。
        if (v_str[i].length() <= max_len)
        {
            continue;
        }
        if (v_str[i+1].length() <= max_len)
        {
            i++;    //虽然当前子串长度>max_len，但是后一子串长度不够，因此又可以直接跳过这个和下一个子串
            continue;
        }
        int eqlen = strcmp_eqlen(v_str[i], v_str[i + 1]);
        if (eqlen>max_len)
        {
            max_len = eqlen;
            index = i;
        }
    }
    cout << max_len << endl;
    cout << v_str[index].substr(0, max_len) << endl;
    return 0;
}
