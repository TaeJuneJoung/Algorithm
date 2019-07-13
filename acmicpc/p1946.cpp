#include <iostream>
#include <algorithm>

using namespace std;
int T, N;
struct st {
	int a, b;
}TEMP[100005];
bool cmp(const st &l, const st &r) {
	return l.a < r.a;
}
int main() {
	scanf("%d", &T);
	while (T--) {
		scanf("%d", &N);
		for (int i = 0; i < N; i++) {
			int a, b;
			scanf("%d %d", &a, &b);
			TEMP[i].a = a;
			TEMP[i].b = b;
		}
		sort(TEMP, TEMP + N, cmp);
		int limit = TEMP[0].b;
		int cnt = 1;
		for (int i = 1; i < N; i++) {
			if (limit > TEMP[i].b) {
				cnt++;
				limit = TEMP[i].b;
			}
		}
		printf("%d\n", cnt);
	}
	return 0;
}