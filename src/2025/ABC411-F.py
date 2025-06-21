import sys

sys.setrecursionlimit(3 * 10**5 + 10)

def main():
    N, M = map(int, input().split())
    edges = [(0, 0)] 
    adj_comp = [set() for _ in range(N + 1)]    
    for _ in range(M):
        U, V = map(int, input().split())
        edges.append((U, V))
        adj_comp[U].add(V)
        adj_comp[V].add(U)

    Q = int(input())
    queries = list(map(int, input().split()))

    parent = list(range(N + 1))

    def find(i):
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])
        return parent[i]

    current_edges = M

    for x in queries:
        u_piece, v_piece = edges[x]

        u_root = find(u_piece)
        v_root = find(v_piece)

        if u_root != v_root and v_root in adj_comp[u_root]:
            
            if len(adj_comp[u_root]) < len(adj_comp[v_root]):
                u_root, v_root = v_root, u_root

            common_neighbors_count = len(adj_comp[u_root] & adj_comp[v_root])
            
            lost_edges = 1 + common_neighbors_count
            current_edges -= lost_edges
            
            parent[v_root] = u_root
            
            v_neighbors_snapshot = list(adj_comp[v_root])

            adj_comp[u_root].update(v_neighbors_snapshot)
            adj_comp[u_root].discard(u_root)
            adj_comp[u_root].discard(v_root)

            for neighbor in v_neighbors_snapshot:
                if neighbor != u_root:
                    adj_comp[neighbor].remove(v_root)
                    adj_comp[neighbor].add(u_root)
            
            adj_comp[v_root] = set()

        print(current_edges)

if __name__ == "__main__":
    main()

"""
PythonではとおらないのでC++で出した

#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

int find(int i, vector<int>& parent) {
    if (parent[i] == i) return i;
    return parent[i] = find(parent[i], parent);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    vector<pair<int, int>> edges = {{0, 0}};
    vector<set<int>> adj_comp(N + 1);

    for (int i = 0; i < M; ++i) {
        int U, V;
        cin >> U >> V;
        edges.emplace_back(U, V);
        adj_comp[U].insert(V);
        adj_comp[V].insert(U);
    }

    int Q;
    cin >> Q;
    vector<int> queries(Q);
    for (int i = 0; i < Q; ++i) {
        cin >> queries[i];
    }

    vector<int> parent(N + 1);
    for (int i = 0; i <= N; ++i) {
        parent[i] = i;
    }

    int current_edges = M;

    for (int x : queries) {
        int u_piece = edges[x].first;
        int v_piece = edges[x].second;

        int u_root = find(u_piece, parent);
        int v_root = find(v_piece, parent);

        if (u_root != v_root && adj_comp[u_root].count(v_root)) {
            if (adj_comp[u_root].size() < adj_comp[v_root].size()) {
                swap(u_root, v_root);
            }

            int common_neighbors_count = 0;
            for (int neighbor : adj_comp[v_root]) {
                if (adj_comp[u_root].count(neighbor)) {
                    ++common_neighbors_count;
                }
            }

            int lost_edges = 1 + common_neighbors_count;
            current_edges -= lost_edges;

            parent[v_root] = u_root;

            vector<int> v_neighbors_snapshot(adj_comp[v_root].begin(), adj_comp[v_root].end());

            for (int neighbor : v_neighbors_snapshot) {
                adj_comp[u_root].insert(neighbor);
            }

            adj_comp[u_root].erase(u_root);
            adj_comp[u_root].erase(v_root);

            for (int neighbor : v_neighbors_snapshot) {
                if (neighbor != u_root) {
                    adj_comp[neighbor].erase(v_root);
                    adj_comp[neighbor].insert(u_root);
                }
            }

            adj_comp[v_root].clear();
        }

        cout << current_edges << '\n';
    }

    return 0;
}

"""