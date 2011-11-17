import	java.util.HashSet;
import	java.util.Set;

class IterCombi	{
	private final int	N;
	private final int	R;
	private final int	ROW;
	private int[][]	num;

	public static long factorial(int n)	{
		int	ret	=	n;
		for ( int i = n - 1; i > 1; --i )	{
			ret	*=	i;
		}
		return	ret;
	}

	public static int combination(int N, int R)	{
		if ( N == R )	return	1;
		int	ret	=	N;
		for ( int i = N - 1; i > R; --i )	{
			ret *= i;
		}
		ret	/= factorial(N - R);
		return	ret;
	}

	public IterCombi(final int N, final int R)	{
		this.N	=	N;
		this.R	=	R;
		this.ROW	=	combination(N, R);
		this.num	=	new int[ROW][R];
		combination();
	}

	public String toString()	{
		StringBuffer	sb	=	new StringBuffer();
		sb.append("combination(" + N + ", " + R + ") = ");
		for ( int i = 0; i < ROW; ++i )	{
			sb.append("[");
			for ( int j = 0; j < R; ++j )	{
				sb.append(" " + num[i][j]);
			}
			sb.append("]");
		}
		return	sb.toString();
	}

	private void printRow(int row)	{
		System.out.print("num[" + row + "]\t");
		for ( int i = 0; i < R; ++i )
			System.out.print(num[row][i]);
		System.out.println();
	}

	private void combination()	{
		if ( N == R )	{
			for ( int i = 0; i < R; ++i )
				num[0][i]	=	i;
			return	;
		}
		if ( R == 1 )	{
			for ( int i = 0; i < ROW; ++i )
				num[i][0]	=	i;
			return	;
		}

		int	row	=	0;
		int	idx	=	0;
		while ( row < ROW )	{
			if ( 0 == idx )	{
				System.out.printf("%d-C-%d: [%d][%d]\n", N, R, row, idx);
				if ( num[row][idx] == N - R )	{
					//printRow(row);
					++row;
					//	종료
				}	else	{
					++idx;
					num[row][idx]	=	num[row][idx - 1] + 1;
				}
			}	else if ( R - 1 == idx )	{
				while ( num[row][idx] < N )	{
					//	저장
					//printRow(row);
					System.arraycopy(num[row], 0, num[row + 1], 0, R);
					++row;
					++num[row][idx];
				}
				--num[row][idx];
				//System.out.print("\t");	printRow(row);
				--idx;
				++num[row][idx];
			}	else	{
				if ( num[row][idx] == idx + N - R + 1 )	{
					--num[row][idx];
					--idx;
					++num[row][idx];
				}	else	{
					++idx;
					num[row][idx]	=	num[row][idx - 1] + 1;
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
		System.out.println(c);
	}
}

