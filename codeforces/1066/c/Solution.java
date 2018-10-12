import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) throws Exception {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(in.readLine());

        int minn = 1;
        int maxn = -1;
        HashMap<Integer, Integer> shelf = new HashMap<>();
        for (int i = 0; i < t; i++) {
            String inp = in.readLine();
            //System.out.println("i = " + i + ", in = " + inp);
            String[] s = inp.split("\\s+");
            char c = s[0].charAt(0);
            int id = Integer.parseInt(s[1]);
            if (c == 'L') {
                int pos = minn - 1;
                minn = pos;
                maxn = Math.max(maxn, pos);
                shelf.put(id, pos);
            } else if (c == 'R') {
                int pos = maxn + 1;
                maxn = pos;
                minn = Math.min(minn, pos);
                shelf.put(id, pos);
            } else {
                int pos = shelf.get(id);
                int l = Math.abs(pos - minn);
                int r = Math.abs(maxn - pos);
                //System.out.println(shelf.toString());
                //System.out.println(maxn + " " + minn + " " + pos);
                System.out.println(Math.min(l, r));
            }
        }
    }
}
