class Solution {
public:
    vector<string> removeInvalidParentheses(string s) {
        n = s.size();
        this->s = s;

        // minimum removals
        int l = 0, r = 0;
        for (char ch : s) {
            if (ch == '(') l++;
            else if (ch == ')') {
                if (l > 0) l--;
                else r++;
            }
        }

        // suffix counts: sufOpen[i] / sufClose[i] = count in s[i:]
        sufOpen.assign(n + 1, 0);
        sufClose.assign(n + 1, 0);
        for (int i = n - 1; i >= 0; i--) {
            sufOpen[i] = sufOpen[i + 1] + (s[i] == '(');
            sufClose[i] = sufClose[i + 1] + (s[i] == ')');
        }

        dfs(0, l, r, 0, "");
        return vector<string>(res.begin(), res.end());
    }

private:
    int n;
    string s;
    vector<int> sufOpen, sufClose;
    unordered_set<string> res;

    void dfs(int i, int l, int r, int open, string path) {
        // pruning
        if (open > sufClose[i] || l > sufOpen[i] || r > sufClose[i]) return;

        if (i == n) {
            if (l == 0 && r == 0 && open == 0) res.insert(path);
            return;
        }

        char ch = s[i];
        if (ch != '(' && ch != ')') {
            dfs(i + 1, l, r, open, path + ch);
            return;
        }

        // group the run of identical parentheses
        int j = i;
        while (j < n && s[j] == ch) j++;
        int k = j - i;

        for (int rem = 0; rem <= k; rem++) {   // remove `rem` of the `k`
            int keep = k - rem;
            if (ch == '(') {
                if (rem > l) break;
                dfs(j, l - rem, r, open + keep, path + string(keep, ch));
            } else {
                if (rem > r) break;
                if (keep > open) continue;
                dfs(j, l, r - rem, open - keep, path + string(keep, ch));
            }
        }
    }
};