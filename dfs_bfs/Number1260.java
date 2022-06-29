// https://www.acmicpc.net/problem/1260
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Number1260 {
    static int[][] arr;
    static ArrayList<Integer> temp_dfs = new ArrayList<>();
    static boolean[] dfs_visited;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int start = Integer.parseInt(st.nextToken());

        arr = new int[n+1][n+1];
        dfs_visited = new boolean[n+1];

        for(int i = 0; i < m; i ++){
            st = new StringTokenizer(br.readLine(), " ");
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            arr[a][b] = 1;
            arr[b][a] = 1;
        }
        dfs(start);

        for(int i = 0; i< temp_dfs.size(); i++){
            System.out.print(temp_dfs.get(i) + " ");
        }
        System.out.println();
        ArrayList<Integer> bfs_result = bfs(start);
        for(int i = 0; i< bfs_result.size(); i++){
            System.out.print(bfs_result.get(i) + " ");
        }
    }

    private static ArrayList<Integer> bfs(int start){
        Queue<Integer> q = new LinkedList<>();
        ArrayList<Integer> result = new ArrayList<>();
        boolean[] visited = new boolean[arr.length];
        visited[start] = true;
        result.add(start);
        q.add(start);
        while (!q.isEmpty()) {
            int x = q.poll();
            for (int i = 0; i < arr.length; i++) {
                if (!visited[i] && arr[x][i]==1){
                    visited[i] = true;
                    q.add(i);
                    result.add(i);
                }
            }
        }

        return result;
    }

    private static void dfs(int node){
        temp_dfs.add(node);
        dfs_visited[node] = true;
        for (int i = 0; i < arr.length; i++){
            if (!dfs_visited[i] && arr[node][i] == 1){
                dfs(i);
            }
        }
    }
}
