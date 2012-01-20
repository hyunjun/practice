package com.practice.interview;

import	java.util.ArrayList;
import	java.util.List;

public class Postfix
{
	private Stack<String>	opStack	=	null;
	private Queue<String> resQueue	=	null;
	private Stack<Integer>	intStack	=	null;

	public Postfix()	{}

	private int isOp(final char c)	{
		switch ( c )	{
		case '*':
		case '/':
			return	3;
		case '+':
		case '-':
			return	2;
		case '(':
		case ')':
			return	1;
		default:
			return	0;
		}
	}

	public String[] getTokens(final String infix)	{
		List<String>	list	=	new ArrayList<String>();
		int	prevOp	=	-1, curOp	=	-1;
		for ( int i = 0; i < infix.length(); ++i )	{
			if ( 0 != isOp(infix.charAt(i)) )	{
				curOp	=	i;
				if ( 1 < curOp - prevOp )
					list.add(infix.substring(prevOp + 1, curOp));
				list.add(infix.substring(curOp, curOp + 1));
				prevOp	=	curOp;
			}
		}
		if ( curOp != infix.length() - 1 )
			list.add(infix.substring(curOp + 1, infix.length()));
		return	list.toArray(new String[list.size()]);
	}

	public void convert(final String infix)	{
		final String[]	tokens	=	getTokens(infix);
		opStack	=	new Stack<String>(tokens.length);
		intStack	=	new Stack<Integer>(tokens.length);
		resQueue	=	new Queue<String>();
		for ( final String token : tokens )	{
			if ( 1 == token.length() && 0 != isOp(token.charAt(0)) )	{
				if ( opStack.isEmpty() )	{
					//System.out.println("op token: " + token + " and stack empty. push to stack");
					opStack.push(token);
				}	else	{
					switch ( token.charAt(0) )	{
					case '(':
						//System.out.println("op token: " + token + " push to stack");
						opStack.push(token);
						break;
					case ')':
						//System.out.println("op token: " + token + " pop till '('");
						String	temp	=	opStack.pop();
						//System.out.println("\tpop " + temp + "\tadd this to queue");
						resQueue.add(temp);
						String	temp2	=	opStack.pop();
						//System.out.println("\tpop " + temp + "\tremove");
						break;
					default:
						String	top	=	opStack.pop();
						//System.out.println("\top from stack: " + top);
						if ( isOp(token.charAt(0)) <= isOp(top.charAt(0)) )	{
							//System.out.println("\t" + token + " <= " + top + "\tadd " + top + " to queue");
							resQueue.add(top);
						}	else	{
							//System.out.println("\t" + token + " > " + top + "\tpush " + top + " to stack");
							opStack.push(top);
						}
						//System.out.println("push " + token + " to stack");
						opStack.push(token);
						break;
					}
				}
			}	else	{
				//System.out.println("number token: " + token + " add to Queue");
				resQueue.add(token);
			}
		}
		while ( false == opStack.isEmpty() )
			resQueue.add(opStack.pop());
		resQueue.print();
	}

	public int calc()	{
		String	token	=	null;
		while ( null != (token = resQueue.remove()) )	{
			if ( 0 < isOp(token.charAt(0)) )	{
				char	op	=	token.charAt(0);
				int	right	=	intStack.pop().intValue();
				int	left	=	intStack.pop().intValue();
				int	result	=	0;
				switch ( op )	{
				case '*':	result	=	left * right;	break;
				case '/':	result	=	left / right;	break;
				case '+':	result	=	left + right;	break;
				case '-':	result	=	left - right;	break;
				}
				intStack.push(new Integer(result));
			}	else	{
				intStack.push(Integer.parseInt(token));
			}
		}
		//System.out.println("result: " + intStack.pop());
		return	intStack.pop();
	}

    public static void main( String[] args )
    {
        System.out.println( "Hello World!" );
    }
}
