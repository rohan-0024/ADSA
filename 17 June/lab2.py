from collections import deque

class KnightShortestPath:
    def __init__(self, N: int):
        """
        Initializes the board size and the 8 possible L-shaped moves for a knight.
        """
        self.N = N
        # The 8 relative moves a knight can make
        self.moves = [
            (-2, -1), (-2, 1), (-1, -2), (-1, 2),
            (1, -2), (1, 2), (2, -1), (2, 1)
        ]

    def _is_valid(self, r: int, c: int) -> bool:
        """
        Helper method to check if a coordinate is within the board boundaries.
        """
        return 0 <= r < self.N and 0 <= c < self.N

    def find_min_moves(self, sr: int, sc: int, tr: int, tc: int) -> int:
        """
        Finds the minimum number of moves from start (sr, sc) to target (tr, tc)
        using Breadth-First Search (BFS). Returns -1 if unreachable.
        """
        # Quick boundary check for inputs
        if not self._is_valid(sr, sc) or not self._is_valid(tr, tc):
            return -1

        # If the start is already the target, 0 moves are needed
        if sr == tr and sc == tc:
            return 0

        # Queue stores elements as: (row, col, moves_count)
        queue = deque([(sr, sc, 0)])
        
        # 2D list to keep track of visited squares
        visited = [[False] * self.N for _ in range(self.N)]
        visited[sr][sc] = True

        # BFS loop
        while queue:
            r, c, moves = queue.popleft()

            # Explore all 8 possible knight moves
            for dr, dc in self.moves:
                nr, nc = r + dr, c + dc

                # Check if the target is reached
                if nr == tr and nc == tc:
                    return moves + 1

                # If the move is valid and hasn't been visited yet
                if self._is_valid(nr, nc) and not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr, nc, moves + 1))

        # Target is unreachable
        return -1


knight = KnightShortestPath(8)
print("Moves:", knight.find_min_moves(0,0,7,7))