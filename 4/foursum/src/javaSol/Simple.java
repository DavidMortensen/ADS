import java.util.Scanner;

public class Simple
{
    public static void main(String[] args)
    {
	Scanner S= new Scanner(System.in);
	int N = Integer.parseInt(S.nextLine());
	long[] vals = new long[N];
	for(int i= 0; i < N; i+= 1) {
		vals[i] = Long.parseLong(S.nextLine());
	}

        // your code goes here and uses the following
		for(int i= 0; i< N; i+= 1) {
			for(int j= i+1; j< N; j+= 1) {
				for(int k= j+1; k< N; k+= 1) {
					for(int l= k+1; l< N; l+= 1) {
						if (vals[i] + vals[j] + vals[k] + vals[l] == 0) 
							{
								System.err.println(i+" "+j+" "+k+" "+l);
								System.out.println(true);
								System.exit(0);
							}
					}
				}
			}
		}
			
        System.out.println(false);
    }
}