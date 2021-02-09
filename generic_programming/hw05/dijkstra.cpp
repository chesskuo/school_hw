#include <bits/stdc++.h>

using namespace std;

#define SIZE 10000+5

int n, start;
int from, to , dis;

int w[SIZE][SIZE];
int d[SIZE];
int father[SIZE];
bool visit[SIZE];

struct Node
{
	int id;
	int d;

	// bool operator<(const Node& rs) const
	// {
	// 	return d > rs.d;
	// }
};

void init()
{
	memset(w, 0, sizeof(w));
	memset(father, -1, sizeof(father));
	memset(visit, 0, sizeof(visit));
	for(int i=0; i<=n; i++) d[i] = 1e9;
}

void dfs(int now)
{
	if(now == -1) return;
	dfs(father[now]);
	cout << now << "->";
	return;
}

void dijkstra(int root)
{
	auto cmp = [](Node& ls, Node& rs)
	{
		if(ls.d == rs.d) return ls.id < rs.id;;
		return ls.d > rs.d;
	};

	priority_queue<Node, vector<Node>, decltype(cmp)> pq(cmp);

	d[root] = 0;
	pq.push((Node){root, d[root]});

	while(!pq.empty())
	{
		int now = pq.top().id;
		pq.pop();

		if(visit[now]) continue;

		if(now != start)
		{
			dfs(father[now]);
			cout << now << ' ' << d[now] << '\n';
		}

		visit[now] = true;

		for(int i=1; i<=n; i++)
		{
			if(!visit[i] && w[now][i] != 0 && d[i] > d[now] + w[now][i])
			{
				d[i] = d[now] + w[now][i];
				father[i] = now;
				pq.push((Node){i, d[i]});
			}
		}
	}
}

int main(int argc, char const *argv[])
{
	#ifdef DBG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	#endif

	ios::sync_with_stdio(false);
	cin.tie(NULL);

	// ----------------------------------------

	while(cin >> n >> start)
	{
		init();
		while(cin >> from >> to >> dis) w[from][to] = dis;
		dijkstra(start);
	}

	exit(0);
}
