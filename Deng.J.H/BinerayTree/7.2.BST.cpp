struct Node
{
    /* data */
    int val;
    Node* left;
    Node* right;
    Node* parent;
    int size;
    Node():size(1){}
    Node(int v, Node* par):val(v), left(nullptr), right(nullptr),parent(par),size(1){}
};
Node* search(Node* root, const int& target, Node* & parent){
    /*
    常规调用过程：search(root, val, parent = nullptr)
    */
    if(root == nullptr || (target == root->val)) return root;
    parent = root;
    return search((target < root->val) ? root->left : root->right, target, parent);
}

Node* insert(const int& target, Node* root){
    /*
    普通二叉搜索树的实现
    */
    Node* temp_parent = nullptr;
    if(!root){
        return new Node(target, temp_parent);
    }
    Node* x = search(root, target, temp_parent);
    if(x){
        return x;
    }else{
        x = new Node(target,temp_parent);
        if(target < temp_parent->val){
            temp_parent->left = x;
        }else{
            temp_parent->right = x;
        }
        Node* cur = x;
        while(cur->parent){
            cur->parent->size ++;
            cur = cur->parent;
        }
    }
    return x;
}
Node* get_succ(Node* op){
    if(op == nullptr) return nullptr;
    if(op->right){
        Node* cur = op->right;
        while(cur->left)
            cur = cur->left;
        return cur;
    }else{
        Node* par = op->parent;
        while(par && par->right == op){
            op = par;
            par = par->parent;
        }
        return par;
    }
}
void b_to_a(Node* a, Node* b){
    /*
    用b代替a的位置，并清理a的内存
    */
    if(!a) return;
    if(!b){
        if(a->parent){
            if(a->parent->left == a){
                a->parent->left = nullptr;
            }else{
                a->parent->right = nullptr;
            }
            // 更新祖先节点的 size
            Node* current = a->parent;
            while(current){
                current->size--;
                current = current->parent;
            }
        }
        delete a;
        a = nullptr;
        return;
    }
    if(!a->parent){
        b->parent = nullptr;
    }else{
        if(a->parent->left == a){
            a->parent->left = b;
        }else{
            a->parent->right = b;
        }
        b->parent = a->parent;
        Node* current = b->parent;
        while(current){
            current->size--;
            current = current->parent;
        }
    }
    delete a;
    a = b;
}
bool remove(const int& target, Node* root){
    if(!root) return false;

    Node* parent = nullptr;
    Node* ask = nullptr;
    Node* temp = search(root, target, parent);
    if(!temp) return false;
    //两种单边的情况都不需要修改父树的size
    if(!temp->left){
        ask = temp->right;
        b_to_a(temp, ask);
    }else if(!temp->right){
        ask = temp->left;
        b_to_a(temp, ask);
    }else{
        ask = get_succ(temp);
        int sw_temp = temp->val;
        temp->val = ask->val;
        ask->val = sw_temp;
        
        // 递归删除后继节点
        Node* succ_parent = ask->parent;
        //把要删除的后继节点的父亲的指向进行改变
        //注意 要删除的节点一定没有左子树
        if(succ_parent->left == ask){
            succ_parent->left = ask->right;
            //把孩子进行一个传递
        }else{
            succ_parent->right = ask->right;
        }

        if(ask->right){
            //把孩子的父亲指针进行修改
            ask->right->parent = succ_parent;
        }
        
        // 更新 size
        Node* current = succ_parent;
        while(current){
            current->size--;
            current = current->parent;
        }
        
        delete ask;
    }
    return true;
}


