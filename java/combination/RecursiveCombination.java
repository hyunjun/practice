import	java.util.HashSet;
import	java.util.Set;

class RecurCombi	{
	private final int	N;
	private final int	R;
	private Set<Set<Integer>>	set;

	public RecurCombi(final int N, final int R)	{
		this.N	=	N;
		this.R	=	R;
		this.set	=	new HashSet<Set<Integer>>();
		combination();
	}

	public String toString()	{
		return	"combination(" + N + ", " + R + ") = " + set;
	}

	private void combination()	{
		if ( 1 == R || N == R )	{
			combination(N, R, 0, new HashSet<Integer>());
		}	else	{
			for ( int i = 0; i < N - R + 1; ++i )	{
				Set<Integer>	tmp	=	new HashSet<Integer>();
				tmp.add(i);
				//System.out.printf("------------------------------\ncombination(%d, %d, %d, %s)\n", N - i - 1, R - 1, i + 1, tmp);
				combination(N - i - 1, R - 1, i + 1, tmp);
			}
		}
	}

	private void combination(int n, int r, int start, Set<Integer> prev)	{
		if ( 1 == r )	{
			for ( int i = start; i < N; ++i )	{
				Set<Integer>	tmp	=	new HashSet<Integer>();
				tmp.add(i);
				tmp.addAll(prev);
				//System.out.println(tmp);
				set.add(tmp);
			}
		}	else if ( n == r )	{
			Set<Integer>	tmp	=	new HashSet<Integer>();
			for ( int i = start; i < N; ++i )	{
				tmp.add(i);
			}
			tmp.addAll(prev);
			//System.out.println(tmp);
			set.add(tmp);
		}	else	{
			for ( int i = start; i < n - r + 1 + start; ++i )	{
				Set<Integer>	tmp	=	new HashSet<Integer>();
				tmp.add(i);
				tmp.addAll(prev);
				//System.out.printf("combination(%d, %d, %d, %s)\n", n - i - 1 + start, r - 1, i + 1, tmp);
				combination(n - i - 1 + start, r - 1, i + 1, tmp);
			}
		}
	}

	public Set<Set<Integer>> getSet()	{
		return	set;
	}

	public static void main(final String[] args)	{
		if ( 2 != args.length )	{
			System.out.println("Usage: java RecurCombi [N] [R]");
			System.exit(1);
		}

		RecurCombi	c	=
			new RecurCombi(Integer.valueOf(args[0]), Integer.valueOf(args[1]));
		System.out.println(c.getSet());
	}
}

