package net.practice.jun;

import java.util.Iterator;
import java.util.List;

public class MyClass implements Iterable<String> {
  public final int i;
  public final List<String> strs;
  public int cursor;

  public MyClass(final int i, final List<String> strs)  {
    this.i = i;
    this.strs = strs;
    this.cursor = 0;
  }

  @Override
  public Iterator<String> iterator()  {
    Iterator<String> it = new Iterator<String>()  {
      @Override
      public boolean hasNext()  {
        return cursor < strs.size() && strs.get(cursor) != null;
      }

      @Override
      public String next()  {
        return strs.get(cursor++);
      }
    };
    cursor = 0;
    return it;
  }

  public boolean isFirst()  {
    return this.cursor == 0;
  }
}

//  just for practice, actually useless
class MyClassList<MyClass> implements Iterable<MyClass> {
  //private MyClass[] myClassList;
  private List<MyClass> myClassList;
  private int currentSize;

  //public MyClassList(MyClass[] myClassList) {
  public MyClassList(List<MyClass> myClassList) {
    this.myClassList = myClassList;
    //this.currentSize = myClassList.length;
    this.currentSize = myClassList.size();
  }

  @Override
	public Iterator<MyClass> iterator() {
    Iterator<MyClass> it = new Iterator<MyClass>()  {
		  private int cursor = 0;

      @Override
		  public boolean hasNext()  {
		    //return this.cursor < currentSize && myClassList[cursor] != null;
		    return this.cursor < currentSize && myClassList.get(cursor) != null;  // && this.listCursor < myClassList.get(cursor).strs.size() && myClassList.get(cursor).strs.(listCursor) != null;
		  }

      @Override
		  public MyClass next() {
        //return myClassList[cursor++];
        return myClassList.get(cursor++);
		  }
	  };
    return it;
  }
}
