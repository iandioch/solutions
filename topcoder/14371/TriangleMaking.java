import java.util.Arrays;

public class TriangleMaking{
	public static void main(String[] args) {
		TriangleMaking t = new TriangleMaking();
		System.out.println(t.maxPerimeter(1, 2, 3));
		System.out.println(t.maxPerimeter(2, 2, 2));
		System.out.println(t.maxPerimeter(1, 100, 1));
		System.out.println(t.maxPerimeter(41, 64, 16));
	}

	public int maxPerimeter(int a, int b, int c) {
		int[] d = new int[]{a, b, c};
		Arrays.sort(d);

		while(d[2] >= d[0] + d[1]) {
			d[2] = d[0] + d[1] - 1;
			Arrays.sort(d);
		}
		
		return d[0] + d[1] + d[2];
	}
}
