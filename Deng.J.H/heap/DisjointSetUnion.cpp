#include <iostream>
#include <vector>
using namespace std;

class DisjointSetUnion {
private:
    vector<int> parent;  // 存储每个元素的父节点

public:
    // 构造函数：初始化并查集
    // 参数 size 是元素的数量，我们将元素编号为 1 到 size
    DisjointSetUnion(int size) : parent(size + 1) {
        // 初始化：每个元素的父节点是自己
        // 这表示开始时每个元素都在单独的集合中
        for (int i = 1; i <= size; i++) {
            parent[i] = i;
        }
    }

    // 查找元素所属的集合（带路径压缩）
    // 返回元素所在集合的根节点
    int find(int element) {
        // 如果元素的父节点是自己，说明找到了根节点
        if (parent[element] == element) {
            return element;
        }
        // 递归查找父节点，同时进行路径压缩
        // 路径压缩：将查找路径上的所有节点直接连接到根节点，加速后续查找
        return parent[element] = find(parent[element]);
    }

    // 合并两个元素所在的集合
    void unite(int element1, int element2) {
        int root1 = find(element1);  // 找到 element1 所在集合的根
        int root2 = find(element2);  // 找到 element2 所在集合的根
        // 如果两个元素不在同一个集合，则合并它们
        if (root1 != root2) {
            // 将 root1 所在的集合合并到 root2 所在的集合
            // 这里可以优化：按秩合并可以使树的高度更加平衡
            parent[root1] = root2;
        }
    }

    // 判断两个元素是否在同一个集合
    bool isSameSet(int element1, int element2) {
        // 如果两个元素的根节点相同，则它们在同一个集合中
        return find(element1) == find(element2);
    }
};

int main() {
    int n, m;
    cin >> n >> m;  // n为元素数量，m为操作数量

    DisjointSetUnion dsu(n);  // 创建一个大小为n的并查集

    // 处理m个操作
    for (int i = 0; i < m; i++) {
        int operation, a, b;
        cin >> operation >> a >> b;

        if (operation == 1) {
            // 操作1：合并集合
            // 将元素a和元素b所在的集合合并
            dsu.unite(a, b);
        } else {
            // 操作2：查询是否在同一集合
            // 判断元素a和元素b是否在同一个集合中
            if (dsu.isSameSet(a, b)) {
                cout << "Y" << endl;  // 在同一个集合中
            } else {
                cout << "N" << endl;  // 不在同一个集合中
            }
        }
    }

    return 0;
}