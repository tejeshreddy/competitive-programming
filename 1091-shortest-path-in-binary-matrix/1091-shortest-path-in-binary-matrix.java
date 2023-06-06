class Solution {
    public int shortestPathBinaryMatrix(int[][] grid) {
        
        if (grid[0][0] == 1) {
            return -1;
        }
        
        int dim = grid.length;
        
        int[][] directions = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}, {1, 1}, {1, -1}, {-1, 1}, {-1, -1}};
        Set<String> visited = new HashSet<>();
        Queue<Pair<Integer, Pair<Integer, Integer>>> queue = new LinkedList<>();
        queue.add(new Pair<>(1, new Pair<>(0, 0)));
        
        while(!queue.isEmpty()) {
            Pair<Integer, Pair<Integer, Integer>> current = queue.poll();
            int count = current.getKey();
            int r = current.getValue().getKey();
            int c = current.getValue().getValue();
            
            if (r == dim - 1 && c == dim - 1) {
                return count;
            }
            
            for (int[] dir: directions) {
                int dr = dir[0] + r;
                int dc = dir[1] + c;
                
                if (dr >= 0 && dr < dim && dc >= 0 && dc < dim && grid[dr][dc] == 0 && !visited.contains(dr + "," + dc)) {
                    queue.add(new Pair<>(count + 1, new Pair<>(dr, dc)));
                    visited.add(dr + "," + dc);
                }
            }
        }
        return -1;
    }
}