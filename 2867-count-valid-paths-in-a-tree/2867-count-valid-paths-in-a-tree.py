
class Solution(object):
    def countPaths(self, n, edges):

        adj = [[] for _ in range(n + 1)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        prime = [True] * (n + 1)
        prime[0] = False
        prime[1] = False

        for i in range(2, n + 1):
            if prime[i]:
                j = i * 2

                while j <= n:
                    prime[j] = False
                    j += i

        visited = [False] * (n + 1)
        comp = [-1] * (n + 1)
        sizes = []

        # Find non-prime connected components
        for i in range(1, n + 1):

            if not prime[i] and not visited[i]:

                stack = [i]
                visited[i] = True
                count = 0
                cid = len(sizes)

                while stack:
                    node = stack.pop()
                    comp[node] = cid
                    count += 1

                    for nei in adj[node]:
                        if not prime[nei] and not visited[nei]:
                            visited[nei] = True
                            stack.append(nei)

                sizes.append(count)

        ans = 0

        # Count valid paths for every prime node
        for i in range(1, n + 1):

            if prime[i]:

                total = 0

                for nei in adj[i]:

                    if not prime[nei]:

                        count = sizes[comp[nei]]

                        ans += count
                        ans += total * count

                        total += count

        return ans
