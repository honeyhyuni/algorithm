// https://www.acmicpc.net/problem/2580
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Number2580 {
    static int[][] arr;
    static ArrayList<int[]> blank;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        arr = new int[9][9];
        blank = new ArrayList<>();
        for(int i =0; i<9; i++){
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            for(int j = 0; j<9; j++){
                arr[i][j] = Integer.parseInt(st.nextToken());
                if(arr[i][j] == 0){
                    blank.add(new int[]{i, j});
                }
            }
        }
        back(0);
        for (int i = 0; i < 9; i++){
            for(int j = 0; j<9; j++){
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
    }
//    x 좌표 확인
    private static boolean horizontal(int x, int target) {
        for(int i = 0; i < 9; i++){
          if(arr[x][i] == target)return false;
        }
        return true;
    }
//    y좌표 확인
    private static boolean vertical(int y, int target){
        for(int i = 0; i<9; i++){
            if(arr[i][y] == target)return false;
        }
        return true;
    }

//    3*3 분할 확인
    private static boolean division(int x, int y, int target){
        int nx = (x / 3) * 3;
        int ny = (y / 3) * 3;
        for(int i = 0; i < 3; i ++){
            for(int j = 0; j< 3; j++){
                if(arr[nx+i][ny+j] == target){
                    return false;
                }
            }
        }
        return true;
    }

//    빈칸 개수만큼 돌면서 모두 충족시킬시 return true
    private static boolean back(int depth) {
        if (depth == blank.size()){
            return true;
        }
        int xx[] = blank.get(depth);
        int x = xx[0];
        int y = xx[1];
        for(int i = 1; i<10; i++){
            if (division(x, y, i) && horizontal(x, i) && vertical(y, i)){
                arr[x][y] = i;
                if (back(depth+1)) return true;
                else arr[x][y] = 0;
            }
        }
        return false;
    }
}
