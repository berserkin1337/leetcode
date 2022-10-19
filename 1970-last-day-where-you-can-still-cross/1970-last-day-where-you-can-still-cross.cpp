#define ll long long
class Solution
{
public:
  
  bool enough(int day, vector<vector<int>> &cells, int row, int col)
  {
    queue<pair<int, int>> q;
    vector<vector<bool>> visited(row, vector<bool>(col, false));
    vector<int> dx = {0, 0, 1, -1};
    vector<int> dy = {1, -1, 0, 0};
    vector<vector<int>> grid(row,vector<int>(col,0));
    for(int i=0;i<day;i++){
        grid[cells[i][0]-1][cells[i][1] - 1] = 1;
    }
    for (int i = 0; i < col; ++i)
    {
      if (grid[0][i] == 0 )
      {
        q.push(make_pair(0, i));
      }
    }
    while (!q.empty())
    {
      int a, b;
      a = q.front().first;
      b = q.front().second;
      q.pop();
      if (visited[a][b])
        continue;
      if (a == row - 1)
        return true;
      visited[a][b] = true;
      for (int i = 0; i < 4; ++i)
      {
        int x = a + dx[i];
        int y = b + dy[i];
        if (x >= 0 && x < row && y >= 0 && y < col && grid[x][y] == 0  && !visited[x][y])
        {
          q.push(make_pair(x, y));
        }
      }
    }

    return false;
  }
  int latestDayToCross(int row, int col, vector<vector<int>> &cells)
  {
    map<pair<int, int>, int> lookup;
    for (int i = 0; i < cells.size(); ++i)
    {
      lookup[{cells[i][0] - 1, cells[i][1] - 1}] = i;
    }
    int low = 1, high = cells.size();
    while (low <= high)
    {
      int mid = low + (high - low) / 2;
      if (enough(mid, cells, row, col))
      {
        low = mid + 1;
      }
      else
      {
        high = mid - 1;
      }
    }
    return high;
  }
};
