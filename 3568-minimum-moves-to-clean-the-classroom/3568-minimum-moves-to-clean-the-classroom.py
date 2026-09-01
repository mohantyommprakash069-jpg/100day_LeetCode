from collections import deque

class Solution:
    def minMoves(self, classroom, energy):
        m = len(classroom)
        n = len(classroom[0])

        sx = sy = 0
        litter_id = {}
        k = 0

        # Find S and give each L an ID
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    sx, sy = i, j
                elif classroom[i][j] == 'L':
                    litter_id[(i, j)] = k
                    k += 1

        if k == 0:
            return 0

        full_mask = (1 << k) - 1

        # best[(x, y, mask)] = maximum energy reached
        best = {}

        q = deque()
        q.append((sx, sy, energy, 0))

        best[(sx, sy, 0)] = energy

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        moves = 0

        while q:

            for _ in range(len(q)):
                x, y, e, mask = q.popleft()

                if mask == full_mask:
                    return moves

                if e == 0:
                    continue

                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy

                    # Outside grid
                    if nx < 0 or nx >= m or ny < 0 or ny >= n:
                        continue

                    # Wall
                    if classroom[nx][ny] == 'X':
                        continue

                    new_energy = e - 1
                    new_mask = mask

                    # Recharge
                    if classroom[nx][ny] == 'R':
                        new_energy = energy

                    # Collect litter
                    if classroom[nx][ny] == 'L':
                        bit = litter_id[(nx, ny)]
                        new_mask |= (1 << bit)

                    state = (nx, ny, new_mask)

                    # If we have already reached this state
                    # with equal or greater energy, skip it
                    if state in best and best[state] >= new_energy:
                        continue

                    best[state] = new_energy
                    q.append((nx, ny, new_energy, new_mask))

            moves += 1

        return -1