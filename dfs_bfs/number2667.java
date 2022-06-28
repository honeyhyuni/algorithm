//https://www.acmicpc.net/problem/2667
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class number2667 {
    static int dx[] = {0, 0, -1, 1};
    static int dy[] = {-1, 1, 0, 0};
    static int arr[][];
    static boolean visited[][];
    static int n;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        n = Integer.parseInt(br.readLine());

        ArrayList<Integer> result = new ArrayList<>();
        arr = new int[n][n];
        visited = new boolean[n][n];
        int apartNum = 0;
        for(int i = 0; i < n; i ++){
            st = new StringTokenizer(br.readLine());
            String s = st.nextToken();
            for(int j = 0; j < n; j ++){
                arr[i][j] = Integer.parseInt(String.valueOf(s.charAt(j)));
                visited[i][j] = false;
            }
        }
        for(int i = 0; i< n; i ++){
            for(int j = 0; j < n; j ++){
                if(arr[i][j] == 1 && visited[i][j] == false){
                    visited[i][j] = true;
                    int a= bfs(i, j);
                    apartNum++;
                    result.add(a);
                }
            }
        }
        Collections.sort(result);
        System.out.println(apartNum);
        for(int i = 0; i < apartNum; i++){
            System.out.println(result.get(i));
        }
    }
    public static int bfs(int x, int y){
        int cnt = 1;
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{x, y});
        while (!q.isEmpty()){
            int xx = q.peek()[0];
            int yy = q.peek()[1];
            q.poll();
            for(int i = 0; i < 4; i++){
                int nx = xx + dx[i];
                int ny = yy + dy[i];
                if(nx >= 0 && nx < n && ny >= 0 && ny<n && visited[nx][ny] == false && arr[nx][ny] == 1){
                    visited[nx][ny] = true;
                    q.add(new int[] {nx, ny});
                    cnt++;
                }
            }
        }

        return cnt;
    }
}
