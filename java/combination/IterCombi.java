import	java.util.HashSet;
import	java.util.Set;

class IterCombi	{
	private final int	N;
	private final int	R;

	public IterCombi(final int N, final int R)	{
		this.N	=	N;
		this.R	=	R;
		combination();
	}

	public void printNum(final int[] num)	{
		for ( final int n : num )
			System.out.print("[" + n + "]");
		System.out.println();
	}

	public void combination()	{
		if ( R == 1 )	{
			for ( int i = 0; i < N; ++i )
				System.out.println("[" + i + "]");
			return	;
		}

		int	idx	=	0;
		int[]	num	=	new int[R];

		while ( 0 <= idx )	{
			if ( 0 == idx )	{
				if ( num[idx] <= N - (R - idx) )	{
					++idx;
					num[idx]	=	num[idx - 1] + 1;
				}	else	{
					--idx;
				}
			}	else if ( R - 1 == idx )	{
				printNum(num);

				if ( num[idx] < N - (R - idx) )	{
					++num[idx];
				}	else	{
					--idx;
					++num[idx];
				}
			}	else	{
				if ( num[idx] <= N - (R - idx) )	{
					++idx;
					num[idx]	=	num[idx - 1] + 1;
				}	else	{
					--idx;
					++num[idx];
				}
			}
		}
	}

	public static void main(final String[] args)	{
		if ( 2 != args.length )	{
			System.out.println("Usage: java IterCombi [N] [R]");
			System.exit(1);
		}

		IterCombi	c	=
			new IterCombi(Integer.valueOf(args[0]), Integer.valueOf(args[1]));
	}
}

