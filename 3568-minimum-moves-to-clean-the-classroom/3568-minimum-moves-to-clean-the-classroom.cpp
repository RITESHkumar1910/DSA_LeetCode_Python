class Solution {
public:
    int minMoves(vector<string>& classroom, int energy) {
        int m = classroom.size();
        int n = classroom[0].size();

        // id[i][j] = bit number of litter at (i,j)
        vector<vector<int>> id(m, vector<int>(n, -1));

        int sr = 0, sc = 0;
        int litter = 0;

        // Find starting position and assign bits to litter
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (classroom[i][j] == 'S') {
                    sr = i;
                    sc = j;
                }
                else if (classroom[i][j] == 'L') {
                    id[i][j] = litter++;
                }
            }
        }

        // No litter
        if (litter == 0)
            return 0;

        int totalMasks = 1 << litter;

        /*
            State:
            (row, col, energy, mask)

            mask:
            1 -> litter still needs to be collected
            0 -> litter already collected
        */

        // visited[row][col][energy][mask]
        vector<vector<vector<vector<bool>>>> visited(
            m,
            vector<vector<vector<bool>>>(
                n,
                vector<vector<bool>>(
                    energy + 1,
                    vector<bool>(totalMasks, false)
                )
            )
        );

        queue<tuple<int, int, int, int>> q;

        int fullMask = (1 << litter) - 1;

        q.push({sr, sc, energy, fullMask});
        visited[sr][sc][energy][fullMask] = true;

        int dr[] = {-1, 1, 0, 0};
        int dc[] = {0, 0, -1, 1};

        int moves = 0;

        while (!q.empty()) {

            int sz = q.size();

            while (sz--) {

                auto [r, c, currEnergy, mask] = q.front();
                q.pop();

                // All litter collected
                if (mask == 0)
                    return moves;

                // Cannot move if energy is zero
                if (currEnergy == 0)
                    continue;

                for (int d = 0; d < 4; d++) {

                    int nr = r + dr[d];
                    int nc = c + dc[d];

                    // Boundary check
                    if (nr < 0 || nr >= m ||
                        nc < 0 || nc >= n)
                        continue;

                    // Obstacle
                    if (classroom[nr][nc] == 'X')
                        continue;

                    int newEnergy;

                    // Reset area
                    if (classroom[nr][nc] == 'R') {
                        newEnergy = energy;
                    }
                    else {
                        newEnergy = currEnergy - 1;
                    }

                    int newMask = mask;

                    // Collect litter
                    if (classroom[nr][nc] == 'L') {
                        int bit = id[nr][nc];
                        newMask &= ~(1 << bit);
                    }

                    // Avoid repeated states
                    if (!visited[nr][nc][newEnergy][newMask]) {

                        visited[nr][nc][newEnergy][newMask] = true;

                        q.push({
                            nr,
                            nc,
                            newEnergy,
                            newMask
                        });
                    }
                }
            }

            moves++;
        }

        return -1;
    }
};