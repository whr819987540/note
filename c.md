获取毫秒级计数

```cpp
#include <time.h>
using namespace std;
int main()
{
	clock_t start,end;
    start=clock();
    ******
    end=clock();
    单位为ms
}
```

vector可以传引用，也可以按值传递

将vector的值打乱顺序（shuffle）

```cpp
#include <iostream>
#include <vector>
#include <random> // std::default_random_engine
#include <chrono> // std::chrono::system_clock
using namespace std;
int main(int argc, char* argv[])
{
    std::vector<int> v;
    for (int i = 0; i < 10; ++i) {
        v.push_back(i);
    }
    // obtain a time-based seed:
    unsigned seed = chrono::system_clock::now().time_since_epoch().count();
    shuffle(v.begin(), v.end(), default_random_engine(seed));

    for (int i = 0; i < v.size(); i++)
        cout << v[i] << " ";
    return 0;
}
```

stl中和sort有关的库函数

[(4条消息) 整理：STL sort排序算法详细介绍_一苇以航-CSDN博客_stl排序算法](https://blog.csdn.net/bat67/article/details/52046679)

