/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Codec {
    string in_order_traversal(TreeNode* root) {
        if (root == NULL) {
            return "#";
        }
        string res = in_order_traversal(root->left);
        res += in_order_traversal(root->right);
        return to_string(root -> val) +  ","  +  res;
    }
    int index = 0;
    string data="";
    TreeNode* helper(){
        if (index >= data.size() )  return NULL;
        if (data[index] == '#') {
            index += 1;
            return NULL;
        }
        string num = "";
        while ( index <  data.size() && (isdigit(data[index]) ||  data[index] == '-' )) {
            num += data[index];
            index++;
        }
        index++;
        cout << num << " " << index << endl;
        if (num != "") {
            int number = stoi(num);
            TreeNode* numu = new TreeNode(number);
            numu->left = helper();
            numu->right = helper();
            return numu;

        }else {
            return NULL;
        }
            
    }
public:
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        cout << in_order_traversal(root) << endl;
        return in_order_traversal(root);
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string serialized_data) {
        data = serialized_data;
        return helper();
    }
};

// Your Codec object will be instantiated and called as such:
// Codec ser, deser;
// TreeNode* ans = deser.deserialize(ser.serialize(root));