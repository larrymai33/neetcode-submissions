class Solution {
public:
    int maxSumDistinctTriplet(vector<int>& x, vector<int>& y) {
        unordered_map<int,int> mp;
        for (int i = 0; i < x.size(); i++) {
            int key = x[i], val = y[i];
            mp[key] = max(mp[key], val);
        }
        if (mp.size() < 3) return -1;
        vector<int> vals;
        for (auto &p : mp) vals.push_back(p.second);
        sort(vals.begin(), vals.end());
        int n = vals.size();
        return vals[n-1] + vals[n-2] + vals[n-3];
    }
};