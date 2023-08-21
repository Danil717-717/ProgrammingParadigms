public class Task01 {
    public static void main(String[] args) {
        char[][] testcase1 = {
            {'1','1','1','1','1','1','1','1','1','1','1'},
            {'1','0','0','0','0','0','0','0','0','1','0'},
            {'1','0','1','0','1','1','0','1','0','1','1'},
            {'1','0','1','0','0','0','0','1','0','1','1'},
            {'1','1','1','0','1','1','0','1','0','0','1'},
            {'0','0','0','0','1','1','0','0','0','0','1'},
            {'1','1','1','1','1','1','1','1','1','0','1'},
            {'1','0','0','0','1','1','0','0','1','0','1'},
            {'1','0','0','1','0','0','1','0','0','0','1'},
            {'1','0','0','0','0','0','1','0','1','1','1'},
            {'1','1','1','1','1','1','1','0','1','1','1'}};
        
        String testcase12 = "0:5,7:10";
    
               
            Task01 testInstance = new Task01();
            boolean result = testInstance.findPath(testcase1,testcase12);
            System.out.print("Result is "+result);      
        }   
    
        public boolean findPath(char[][] maze, String points)
        {
            char [][] inputMaze = maze;
    
            int row = maze.length;
            int col = maze[0].length;
    
            // Getting start and end points
            String[] parts1 = points.split(":");
            String[] parts2 = parts1[1].split(",");
    
            int startX = Integer.valueOf(parts1[0]);
            int startY = Integer.valueOf(parts2[0]);
    
            int endX = Integer.valueOf(parts2[1]);
            int endY = Integer.valueOf(parts1[2]);
    
            char[][] visited = new char[row][col];      
    
            boolean result = path(inputMaze, startX, startY, endX, endY, visited);
            if(!result)
                return false;
            else
                return true;
        }
    
    
        public boolean path(char[][] inputMaze,int startX, int startY, int endX, int endY, char[][] visited)
        {
            if((startX == endX) && (startY == endY))
            {
                return true;
            }
            if((startX > inputMaze.length-1) || (startY > inputMaze[0].length-1) && (startX < 0 || startY < 0))
            {
                return false;
            }
            if((inputMaze[startX][startY] == ' ') && (visited[startX][startY] != '*'))
            {
                visited[startX][startY] = '*';
            }
            else
            {
                return false;
            }
            boolean u = path(inputMaze, startX-1, startY, endX, endY, visited);
            boolean d = path(inputMaze, startX+1, startY, endX, endY, visited);
            boolean r = path(inputMaze, startX, startY+1, endX, endY, visited);
            boolean l = path(inputMaze, startX, startY-1, endX, endY, visited);
    
            return u || d|| l || r;
        }   
    }

